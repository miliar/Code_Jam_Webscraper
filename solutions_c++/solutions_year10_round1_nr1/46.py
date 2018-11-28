#include<stdio.h>

char s[51][51];
char ss[51][51];
int n,k;

bool check(char x)
{
	int i,j,r;
	for (i=0;i<n;i++)
		for (j=0;j<n;j++)
		{
			if (i+k-1<n)
			{
				for (r=0;r<k;r++)
					if (s[i+r][j]!=x) break;
				if (r==k) return true;
			}
			if (j+k-1<n)
			{
				for (r=0;r<k;r++)
					if (s[i][j+r]!=x) break;
				if (r==k) return true;
			}
			if (i+k-1<n&&j+k-1<n)
			{
				for (r=0;r<k;r++)
					if (s[i+r][j+r]!=x) break;
				if (r==k) return true;
			}
			if (i+k-1<n&&j-(k-1)>=0)
			{
				for (r=0;r<k;r++)
					if (s[i+r][j-r]!=x) break;
				if (r==k) return true;
			}
		}
	return false;
}

int main()
{
	int t,p;
	int i,j,r;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for (p=1;p<=t;p++)
	{
		scanf("%d%d",&n,&k);
		for (i=0;i<n;i++)
			scanf("%s",ss[i]);
		for (j=0;j<n;j++)
		{
			r=n-1;
			for (i=n-1;i>=0;i--)
				if (ss[n-1-j][i]=='B'||ss[n-1-j][i]=='R')
				{
					s[r][j]=ss[n-1-j][i];
					r--;
				}
			for (;r>=0;r--)
				s[r][j]='.';
		}
		bool f1=check('B');
		bool f2=check('R');
		if (f1&&f2) printf("Case #%d: Both\n",p);
		if ((!f1)&&f2) printf("Case #%d: Red\n",p);
		if (f1&&(!f2)) printf("Case #%d: Blue\n",p);
		if ((!f1)&&(!f2)) printf("Case #%d: Neither\n",p);
	}
	return 0;
}