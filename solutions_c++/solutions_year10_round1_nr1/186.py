#include<iostream>
#include<stdio.h>
using namespace std;
int yes[5];
int a[100][100],n,k,last,l;

int work()
{
	yes[0]=0; yes[1]=0; yes[2]=0;
	for (int i=1;i<=n;i++)
	{
		last=0; l=0;
	    for (int j=1;j<=n;j++)
		  {
				if (a[i][j]==last) l++;
				else {last=a[i][j]; l=1; }
				if (l>=k) yes[last]=1;
			}
	}
	for (int j=1;j<=n;j++)
	{
		last=0; l=0;
	    for (int i=1;i<=n;i++)
		  {
				if (a[i][j]==last) l++;
				else {last=a[i][j]; l=1; }
				if (l>=k) yes[last]=1;
			}
	}
	if ((yes[1])&&(yes[2])) return 0;
	for (int x=1-n;x<=n-1;x++)
	{
		last=0; l=0;
	 	for (int i=1;i<=n;i++)
		{
			int j=i-x;
			if ((j<1)||(j>n)) continue;
			if (a[i][j]==last) l++;
			else {last=a[i][j]; l=1; }
			if (l>=k) yes[last]=1;
		}
	}
	if ((yes[1])&&(yes[2])) return 0;
	for (int x=2;x<=n+n;x++)
	{
		last=0; l=0;
	 	for (int i=1;i<=n;i++)
		{
			int j=x-i;
			if ((j<1)||(j>n)) continue;
			if (a[i][j]==last) l++;
			else {last=a[i][j]; l=1; }
			if (l>=k) yes[last]=1;
		}
	}
	return 0;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	long testcase;
	scanf("%ld",&testcase);
	for (int ttt=1;ttt<=testcase;ttt++)
	{
		scanf("%ld %ld",&n,&k);
		scanf("\n");
		for (int i=1;i<=n;i++)
		{
		  for (int j=1;j<=n;j++)
	      { char x; scanf("%c",&x); if (x=='.') a[i][j]=0; else if (x=='B') a[i][j]=1; else a[i][j]=2;}
		  scanf("\n");
		  int p=0;
		  for (int j=n;j>0;j--)
		  {
				if (a[i][j]==0) p++;
				else { a[i][j+p]=a[i][j]; if (p>0) a[i][j]=0; }
			}
   		}
		work();
		printf("Case #%ld: ",ttt);
		if (yes[1]&yes[2]) printf("Both \n");
		else if (yes[1]) printf("Blue \n");
		else if (yes[2]) printf("Red \n");
		else printf("Neither \n");
	}
}
