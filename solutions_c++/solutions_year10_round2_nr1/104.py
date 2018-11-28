#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <iostream>
#include <map>
using namespace std;
struct node{
	map<string,node*> child;
};
node* tree;
int n,m,ans;

void insert(node* tree,char* str){
	if (strlen(str)==0){
		return;
	}
	int pos;
	string cur="";
	for (int i=1;;i++){
		if (str[i]=='\0'){
			pos=i;
			break;
		}
		if (str[i]=='/'){
			pos=i;
			break;
		}
		cur+=str[i];
	}
	if (tree->child.find(cur)==tree->child.end()){
		ans++;
		node* for_insert=new node();
		tree->child[cur]=for_insert;
	}
	insert(tree->child[cur],str+pos);
	return;
}

void getinittree(){
	char str[102];
	for (int i=1;i<=n;i++){
		scanf("%s",str);
		insert(tree,str);
	}
	return;
}

void init(){
	tree=new node();
	scanf("%d%d",&n,&m);
	getinittree();
	ans=0;
	return;
}

void process(){
	char str[102];
	for (int i=1;i<=m;i++){
		scanf("%s",str);
		insert(tree,str);
	}
	return;
}

int main(){
	int cse;
	scanf("%d",&cse);
	for (int k=1;k<=cse;k++){
		init();
		process();
		printf("Case #%d: %d\n",k,ans);
	}	
	return 0;
}
