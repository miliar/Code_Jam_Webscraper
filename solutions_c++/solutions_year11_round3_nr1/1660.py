//Compiled using Visual Studio C++ 2010 Express - Version 10.0.30319.1 RTMRel
#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <map>
#include <bitset>

using namespace std;

typedef vector<int> IVECTOR;
typedef vector<int>::iterator IVECTOR_ITR;
typedef vector<char> CVECTOR;
typedef vector<float> FVECTOR;
typedef vector<string> SVECTOR;

typedef map<int,int> IIMAP;
typedef map<int,string> ISMAP;
typedef map<string,string> SSMAP;
typedef map<string,int> SIMAP;


#define FOR(i,a,n) for (int i=a;i<n;i++)
#define FORN(i,a,n) for (int i=n-1;i>=a;i--)


#define FOR1(i,a,n) for (int i=a;i<=n;i++)
#define FOR1N(i,a,n) for (int i=n;i>a;i--)

int main (int argv, char* argc[])
{
	freopen("ina.txt","r+",stdin);
	freopen("outa.txt","w+",stdout);

	int n = 0;
	scanf("%d\n",&n);

	FOR(i,0,n)
	{
		int r = 0, c = 0;
		char a[200][200];

		scanf("%d %d\n",&r,&c);

		FOR(j,0,r)
		{
			scanf("%s",&a[j]);
		}

		bool bPossible = true;

		FOR(j,0,r)
		{
			FOR(k,0,c)
			{
				bool bFound = false;
				if (a[j][k] == '#' )
				{
					bFound = true;
					if (a[j][k] == a[j+1][k+1] && a[j][k] == a[j][k+1] && a[j][k] == a[j+1][k])
					{
						a[j][k] = '/';
						a[j][k+1] = '\\';
					    a[j+1][k] = '\\';
						a[j+1][k+1] = '/';
					}
					else
					{
						bPossible = false;
						break;
					}
				}
			}
			if (!bPossible)
			{
				break;
			}
		}
		printf("Case #%d:\n",i+1);

		if (!bPossible)
		{
			printf("Impossible\n");
		}
		else
		{
			FOR(j,0,r)
			{
				FOR(k,0,c)
				{
					printf("%c",a[j][k]);
				}
				printf("\n");
			}
		}

	}


	fclose(stdin);
	fclose(stdout);
}