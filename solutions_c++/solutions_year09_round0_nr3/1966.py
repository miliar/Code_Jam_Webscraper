#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int n,test,i,j,l,ll;
char line[510];
string wcs;
int d[510][25];

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);

	wcs="welcome to code jam";
	l=wcs.length();

	scanf("%d\n",&n);
	for (test=1; test<=n; test++)
	{
		gets(line);
		ll=strlen(line);
		memset(d,0,sizeof(d));
		for (i=0; i<=ll; i++)
		for (j=0; j<=l; j++)
		{
			if (j==0) d[i][j]=1; else
			if (i==0) d[i][j]=0; else
			if (j>i) d[i][j]=0; else
			if (line[i-1]==wcs[j-1]) d[i][j]=(d[i-1][j-1]+d[i-1][j])%10000; else
									 d[i][j]=d[i-1][j];
		}
		printf("Case #%d: ",test);
		i=ll; j=l;
		if (d[i][j]<10) printf("000%d\n",d[i][j]); else
		if (d[i][j]<100) printf("00%d\n",d[i][j]); else
		if (d[i][j]<1000) printf("0%d\n",d[i][j]); else
		if (d[i][j]<10000) printf("%d\n",d[i][j]);
	}

    return 0;
}
