// A.Alien Language.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include"iostream"
using namespace std;
bool hash[6000];
char str[6000][20],s[2000];
int main()
{
	bool flag[26];
	int L,D,N,i,j,ci=1;
	freopen("G:\\A-large.in","r",stdin);
	freopen("G:\\Aout.out","w",stdout);
	while(scanf("%d%d%d",&L,&D,&N)!=EOF){
		for(i=0;i<D;i++)
			scanf("%s",str[i]);
		for(ci=1;ci<=N;ci++){
			int t ,p=0;
			memset(hash,1,sizeof(hash));
			scanf("%s",s);
			for(j=0;j<L;j++){
				memset(flag,0,sizeof(flag));
				if(s[p] == '('){
					p++;
					while(s[p] != ')'){
						flag[s[p++]-'a'] = 1;
					}
					p++;
				}
				else
					flag[s[p++]-'a'] = 1;
				for(i=0;i<D;i++)
					if(!flag[str[i][j]-'a'] )
						hash[i] = 0;
			}
			t = 0;
			for(i=0;i<D;i++)
				if(hash[i])
					t++;
			printf("Case #%d: %d\n",ci,t);
		}
	}
	return 0;
}





