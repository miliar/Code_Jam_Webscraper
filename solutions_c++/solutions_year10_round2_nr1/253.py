#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <functional>
#include <string>
#include <cstring>
#include <ctime>
#include <cmath>

using namespace std;

char s[100000];

struct Node{
	map<string,Node*> m;
	string name;
	Node(){};
	Node(string s){
		name=s;
	}
} root;

void purgedata(Node *c){
	for(map<string,Node*>::iterator it=c->m.begin(),ite=c->m.end();it!=ite;it++){
		purgedata(it->second);
		delete it->second;
	}
	c->m.clear();
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int q;
	scanf("%d",&q);
	char s[200];
	gets(s);
	for(int test=1;test<=q;test++){
		int ans=0;
		int n,m;
		scanf("%d%d",&n,&m);
		gets(s);
		string S;
		for(int i=0;i<n;i++){
			gets(s);
			for(int j=0;j<strlen(s);j++)
				if(s[j]=='/')s[j]=' ';
			S=s;
			istringstream is(S);
			Node *c=&root;
			while(is>>S){
				if(c->m[S]==NULL){
					c->m[S]=new Node(S);
				}
				c=c->m[S];
			}
		}
		for(int i=0;i<m;i++){
			gets(s);
			for(int j=0;j<strlen(s);j++)
				if(s[j]=='/')s[j]=' ';
			S=s;
			istringstream is(S);
			Node *c=&root;
			while(is>>S){
				if(c->m[S]==NULL){
					c->m[S]=new Node(S);
					ans++;
				}
				c=c->m[S];
			}
		}
		printf("Case #%d: %d\n",test,ans);
		purgedata(&root);
	}

	return 0;
}
