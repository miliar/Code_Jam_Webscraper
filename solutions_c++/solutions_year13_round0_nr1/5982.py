#include <stdio.h>

const int n=4;
const char res[4][30]={"X won","O won","Draw","Game has not completed"};
int TC,tc;
char a[n][n+1];

int f()
{
	int i,j;
	for(i=0;i<n && (a[i][i]=='X' || a[i][i]=='T');++i);
	if(i==n) return 0;
	for(i=0;i<n && (a[i][n-1-i]=='X' || a[i][n-1-i]=='T');++i);
	if(i==n) return 0;
	for(i=0;i<n;++i)
	{
		for(j=0;j<n && (a[i][j]=='X' || a[i][j]=='T');++j);
		if(j==n) return 0;
		for(j=0;j<n && (a[j][i]=='X' || a[i][j]=='T');++j);
		if(j==n) return 0;
	}
	for(i=0;i<n && (a[i][i]=='O' || a[i][i]=='T');++i);
	if(i==n) return 1;
	for(i=0;i<n && (a[i][n-1-i]=='O' || a[i][n-1-i]=='T');++i);
	if(i==n) return 1;
	for(i=0;i<n;++i)
	{
		for(j=0;j<n && (a[i][j]=='O' || a[i][j]=='T');++j);
		if(j==n) return 1;
		for(j=0;j<n && (a[j][i]=='O' || a[i][j]=='T');++j);
		if(j==n) return 1;
	}
	for(i=0;i<n;++i)
		for(j=0;j<n;++j)
			if(a[i][j]=='.') return 3;
	return 2;
}

int main()
{
	int i;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	for(scanf("%d",&TC),tc=1;tc<=TC;++tc)
	{
		for(i=0;i<n;++i)
			scanf("%s",a[i]);
		printf("Case #%d: %s\n",tc,res[f()]);
	}
	return 0;
}