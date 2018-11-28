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

char a[100][100];
char temp[20][20];



double wp[100],owp[100],oowp[100],wpx[100];

double WP(int n, char a[], int ignore = -1)
{
	double win = 0, lose = 0;



	FOR (i,0,n)
	{
		if (ignore != -1 && ignore == i)
			continue;

		if (a[i] == '1')
		{
			win++;
		}
		else if (a[i] == '0')
		{
			lose++;
		}
	}

	return win/(win+lose);
}

double OWP (int n, int pos, char b[])
{
	double result = 0.0;
	int count = 0;
	FOR (i,0,n)
	{
		if (b[i] != '.')
		{
			result += WP(n,a[i],pos);
			count++;
		}
	}

	return result/count;
}

double OOWP (int n, int pos, char b[])
{
	double result = 0.0;
	int count = 0;
	FOR (i,0,n)
	{
		if (b[i] != '.')
		{
			result += owp[i];
			count++;
		}
	}

	return result/count;
}

int main (int argv, char* argc[])
{
	freopen("in.txt","r+",stdin);
	freopen("out.txt","w+",stdout);

	int n = 0;
	scanf("%d\n",&n);

	FOR(i,0,n)
	{
		printf("Case #%d:\n",i+1);
		int t = 0;
		scanf("%d\n",&t);
		
		FOR (j,0,t)
		{
			FOR (k,0,t)
			{
				scanf("%c",&a[j][k]);
			}
			char space;
			scanf("%c",&space);
			wp[j] = WP(t,a[j]);
		}

		FOR (j,0,t)
		{
			owp[j] = OWP(t,j,a[j]);
		}

		FOR (j,0,t)
		{
			
			
			printf("%f\n",(0.25*wp[j]) + (0.5*owp[j]) + (0.25*OOWP(t,j,a[j])));
		}
	}


	fclose(stdin);
	fclose(stdout);
}