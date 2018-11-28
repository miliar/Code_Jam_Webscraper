#include<stdio.h>
#include<memory.h>
#include<iostream>
#include<algorithm>
using namespace std;

int n;
int a[100],h[10];
char line[100];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int i,j,T,T1;
	scanf("%d\n",&T);
	for(T1=1;T1<=T;T1++)
	{
		printf("Case #%d: ",T1);
		int n=0;
		gets(line);
		for(i=0;line[i]!='\0';i++)
		{
			a[++n]=line[i]-'0';
		}
		
		a[0]=0;
		memset(h,0,sizeof(h));
		for(i=n;i>=0;i--)
		{
			for(j=a[i]+1;j<=9;j++)
			{
				if(h[j]) break;
			}
			if(j!=10)
			{
				swap(a[i],a[h[j]]);
				sort(a+i+1,a+1+n);
				break;
			}
			h[a[i]]=i;
		}

		if(i==0) i=0;
		else i=1;
		for(;i<=n;i++)
		{
			printf("%d",a[i]);
		}
		printf("\n");
	}
	return 0;
}