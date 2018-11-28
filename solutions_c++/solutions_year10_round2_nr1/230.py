#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<set>
using namespace std;

int n , m;
int ttt;
set<string> S;
set<string>::iterator it;

char str[200];
char tmpS[200];

void solve(){
	int i,j;
	int len;
	int res;
	scanf("%d%d", &n,&m);
	S.clear();
	for(j=0;j<n;++j){
		scanf("%s",str);
		len = strlen(str);
		str[len]='/';
		for(i=1;i<=len;++i){
			if(str[i]=='/'){
				memcpy(tmpS, str, i);
				tmpS[i]=0;
				S.insert(tmpS);
			}
		}
	}
	
	res=0;
	for(j=0;j<m;++j){
		scanf("%s",str);
		len = strlen(str);
		str[len]='/';
		for(i=1;i<=len;++i){
			if(str[i]=='/'){
				memcpy(tmpS, str, i);
				tmpS[i]=0;
				if(S.find(tmpS)==S.end()){
					S.insert(tmpS);
					++res;
				}
			}
		}
	}
	
	
	printf("Case #%d: %d\n",++ttt,res);
}
int main(){
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);
	int t;scanf("%d",&t);
	ttt=0;
	while(--t>=0) solve();
	return 0;
}
