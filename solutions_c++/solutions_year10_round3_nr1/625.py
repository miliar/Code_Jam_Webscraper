#include<stdio.h>
#include<iostream>
#include<cstring>
#include<string.h>

#define MAX 1010

int Nokta[MAX][2];
int S;

int Ekle(int a,int b)
	{
	int i,ans=0;
	for(i=0; i<S; i++)
		{
		if(Nokta[i][0]<a && Nokta[i][1]>b)ans++;
		else if(Nokta[i][0]>a && Nokta[i][1]<b)ans++;	
		}
	Nokta[S][0]=a;
	Nokta[S][1]=b;
	S++;
	return ans;
	}

int main()
	{
	int T,N,a,b,ans;
	scanf(" %d",&T);;	
	for(int i=1; i<=T; i++)
		{
		ans=S=0;
		scanf(" %d",&N);
		
		for(int j=0; j<N; j++)
			{
			scanf(" %d %d",&a,&b);
			ans+=Ekle(a,b);
			}
		printf("Case #%d: %d\n",i,ans);
		}
	return 0;
	}
