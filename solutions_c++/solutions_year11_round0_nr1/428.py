#include <stdio.h>
#include <iostream>
using namespace std;
char ch[128];
int di[128];
int n;
int tot;
int funabs(int a)
{
	if(a<0)return (-a);else return a;
}
int find()
{
	int ans=0;
	int posO=1;
	int posB=1;
	int O1=0;
	int B1=0;
	int time=0;
	while(O1<n||B1<n)
	{
		while(ch[O1]!='O'&&O1<n)O1++;
		while(ch[B1]!='B'&&B1<n)B1++;
		int dO=funabs(posO-di[O1]);
		int dB=funabs(posB-di[B1]);
		if(B1<O1)
		{
			time+=dB;
			posB=di[B1];
			time++;
			B1++;
			if(dO<=dB+1)posO=di[O1];else
			{
				if(di[O1]<posO)posO-=(dB+1);
					else posO+=(dB+1);
			}
		}else
		{
			time+=dO;
			posO=di[O1];
			time++;
			O1++;
			if(dB<=dO+1)posB=di[B1];else
			{
				if(di[B1]<posB)posB-=(dO+1);
					else posB+=(dO+1);
			}
		}
	}
	return time;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&tot);
	for(int i=1;i<=tot;i++)
	{
		scanf("%d",&n);
		for(int j=0;j<n;j++)scanf(" %c %d",&ch[j],&di[j]);
		printf("Case #%d: %d\n",i,find());
	}
	return 0;
}
