// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include"iostream"
using namespace std;
int hash[300],p[300];
int main()
{
	char s[100];
	int t,i,len,used = 0,jinzhi,ci=1;
	__int64 ans,k;
	freopen("G:\\A-large.in","r",stdin);
	freopen("G:\\Aout.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		scanf("%s",s);
		used = 0;
		memset(hash,0,sizeof(hash));
		len = strlen(s);
		for(i=0;i<len;i++)
			hash[s[i]] = 1;
		for(i=0,jinzhi = 0;i<300;i++)
			if(hash[i])
				jinzhi++;
		if(jinzhi == 1)
			jinzhi = 2;
		memset(p,-1,sizeof(p));
		p[s[0]] = 1;
		for(i=1;i<len;i++)
			if(p[s[i]] == -1){
				p[s[i]] = used++;
				if(used == 1)
					used++;
			}
		ans = 0;
		k = 1;
		for(i=len-1;i>=0;i--){
			ans += p[s[i]] * k;
			k *= jinzhi;
		}
		printf("Case #%d: %I64d\n",ci++,ans);
	}
	return 0;
}

		
		
