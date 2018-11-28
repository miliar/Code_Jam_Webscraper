#include <iostream>
#include <fstream>
#include <string>
#include <string.h>

using namespace std;

bool yes[49][40];
char in[6000][49];
char in1[101149];

int l,d,n;

int main()
{
	freopen ("a.in", "r" , stdin);
	freopen ("b.out", "w" , stdout);
	scanf ("%d%d%d" , &l, &d, &n);
	
		gets (in1);
	for (int i=1;i<=d;i++)
	{
		gets(in[i]);
	}
	
	for (int j=1;j<=n;j++)
	{
		int sum=0;

		memset(yes,0 ,sizeof(yes) );

		gets (in1);

		int co=0;
		for (int i=0;i<l;i++)
		{
			if (in1[co]=='(')
			{
				co++;
				while (in1[co]!=')')
				{
					yes[i][in1[co]-'a']=1;
					co++;
				}
			}
			else
			{
				yes[i][in1[co]-'a']=1;
			}
				co++;
		}

		for (int i=1;i<=d;i++)
		{
			bool add=1;
			for (int k=0;k<l;k++)
			{
				if (!yes[k][in[i][k]-'a'])
					add=0;
			}
			sum+=add;
		}

		printf ("Case #%d: %d\n", j, sum);
	}

	return 0;
}
