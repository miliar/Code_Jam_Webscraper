#include<iostream>
#include<stdio.h>
#include<memory.h>
using namespace std;
char a[3000];
int q[100],q1[100];
char aa[30]="welcome to code jam";
int main()
{
	int n;
	int ca,i,j;
	freopen("in.txt","r",stdin);
	freopen("small.out","w",stdout);
	scanf("%d",&n);
	gets(a);
	for(ca=1;ca<=n;ca++)
	{
		memset(q,0,sizeof(q));
		gets(a);
		for(i=0;a[i];i++)
		{
			for(j=18;j>0;j--)
			{
				if(aa[j]==a[i])
					q[j]+=q[j-1];
					q[j]%=10000;
			}
			if(aa[0]==a[i])
			{
			q[0]++;q[0]%=10000;
			}
		}
		printf("Case #%d: %04d\n",ca,q[18]);
	}
	return 0;
}
