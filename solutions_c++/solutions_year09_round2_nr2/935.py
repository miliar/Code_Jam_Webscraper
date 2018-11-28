#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int cs,k,i,a[1000],l,j;
	char str[1000];
	scanf("%d",&cs);
	getchar();
	for (k=1;k<=cs;k++)
	{
		
		scanf("%s",str);
		l=strlen(str);
		for (i=0;i<l;i++)
			a[i]=str[i]-'0';
		for (i=l-2;i>=0;i--)
			if (a[i]<a[i+1]) break;
		printf("Case #%d: ",k);
		if (i==-1)
		{
			for (i=0;i<l;i++)
				if (a[i]==0) break;
			printf("%d",a[i-1]);
			a[i-1]=0;
			for (i=l-1;i>=0;i--)
				printf("%d",a[i]);
			printf("\n");
		}
		else
		{
			for (j=l-1;j>i;j--)
				if (a[j]>a[i]) 
				{
					swap(a[i],a[j]);
					break;
				}
			sort(a+i+1,a+l);
			for (i=0;i<l;i++)
				printf("%d",a[i]);
			printf("\n");
		}
	}
	return 0;
}
