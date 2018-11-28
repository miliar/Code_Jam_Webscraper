// Welcome to Code Jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;
char standard[20]="welcome to code jam";
char test[505];
int length=19;
int N;
int ans;
int cnt[505][20];
void DP()
{
	int str_length=strlen(test);
	memset(cnt,0,sizeof(cnt));
	for(int i=str_length;i>=0;i--)
	{
		cnt[i][0]=1;
	}
	for(int k=1;k<=length;k++)
	{
		for(int i=str_length-1;i>=0;i--)
		{
			if(test[i]==standard[length-k]) cnt[i][k]=cnt[i+1][k-1]+cnt[i+1][k];
			else cnt[i][k]=cnt[i+1][k];
			cnt[i][k]=cnt[i][k]%10000;
		}
	}
}
int main()
{
	//freopen("d:\\1.txt","r",stdin);
	freopen("d:\\C-large.in","r",stdin);
	freopen("d:\\C-large.out","w",stdout);
	length=strlen(standard);
	scanf("%d\n",&N);
	for(int t=1;t<=N;t++)
	{
		ans=0;
		cin.getline(test,600);
		DP();
		ans=cnt[0][length];
		printf("Case #%d: ",t);
		if(ans<10) printf("000");
		else if(ans<100) printf("00");
		else if(ans<1000) printf("0");
		printf("%d\n",ans);
	}
	return 0;
}

