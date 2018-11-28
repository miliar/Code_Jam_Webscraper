#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
#include <string.h>
#include <cstring>

using namespace std;

int t;
int n;
char s[200];
char p[200];

int srav()
{
	int i;
	for (i=0; i<n; i++)
		if (p[i]>s[i]) return 1; else 
			if (p[i]<s[i]) return 2;

	return 0;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d\n",&t);
	for (int tt=1; tt<=t; tt++)
	{
		memset(s,0,sizeof(s));
		memset(p,0,sizeof(p));
		gets(s);

		n=strlen(s);
		int i,j;

		for (i=0; i<n; i++) p[i]=s[i];

		next_permutation(p,p+n);

		if (srav()!=1)
		{
			p[n]='0';
			sort(p,p+n+1);
			for (j=1; j<=n; j++)
				if (p[j]!='0')
				{
					swap(p[j],p[0]);
					break;
				}
		}

		printf("Case #%d: ",tt);
		puts(p);
	}

	return 0;
}