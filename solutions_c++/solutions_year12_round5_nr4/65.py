#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
const int maxn=1002;
const int oo=100000;
char str[maxn];
int K,n,cntedge;
map<char,bool> hash;
bool edge[100][100];
int deg[maxn];

void init(){
	scanf("%d%s",&K,str);
	n=strlen(str);
	hash.clear();
	memset(edge,false,sizeof(edge));
	memset(deg,0,sizeof(deg));
	cntedge=0;
	return;
}

void preprocess(){
	hash['o']=0;
	hash['i']=1;
	hash['e']=3;
	hash['a']=4;
	hash['s']=5;
	hash['t']=7;
	hash['b']=8;
	hash['g']=9;
	return;
}

int process(){
	for (int i=0;i<n-1;i++){
		edge[str[i]-'a'][str[i+1]-'a']=true;
		if (hash.find(str[i])==hash.end()){
			if (hash.find(str[i+1])!=hash.end()){
				edge[str[i]-'a'][hash[str[i+1]]+26]=true;
			}
		} else {
			edge[hash[str[i]]+26][str[i+1]-'a']=true;
			if (hash.find(str[i+1])!=hash.end()){
				edge[str[i]-'a'][hash[str[i+1]]+26]=true;
				edge[hash[str[i]]+26][hash[str[i+1]]+26]=true;
			}
		}
	}
	for (int i=0;i<36;i++){
		for (int j=0;j<36;j++){
			if (!edge[i][j]){
				continue;
			}
			cntedge++;
			deg[i]++;
			deg[j]--;
		}
	}
	int ans=oo;
	for (int i=0;i<36;i++){
		for (int j=0;j<36;j++){
			deg[i]++;
			deg[j]--;
			int cur=0;
			for (int k=0;k<36;k++){
				if (deg[k]>0){
					cur+=deg[k];
				}
			}
			if (ans>cur){
				ans=cur;
			}
			deg[i]--;
			deg[j]++;
		}
	}
	return cntedge+ans+1;
}

int main(){
	int tcase;
	scanf("%d",&tcase);
	for (int i=1;i<=tcase;i++){
		init();
		preprocess();
		printf("Case #%d: %d\n",i,process());
	}
	return 0;
}