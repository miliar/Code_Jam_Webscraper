// 2011_2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

FILE * in, * out;

#define fo(a,b,c) for(int a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )

int ri() { int a; fscanf(in, "%d", &a ); return a; }
double rf() { double a; fscanf(in, "%lf", &a ); return a; }
char sbuf[100005]; string rs() { fscanf(in, "%s", sbuf ); return sbuf; }
long long rll() { long long a; fscanf(in, "%lld", &a ); return a; }


vector<int> prime;

void countPrime()
{
	for(int i = 2; i<=2000; i++)
	{
		bool found = false;;
		fk(prime.size()) if( (i%prime[k]) == 0 ) { found = true; break; }
		if(!found) prime.push_back(i);
	}
}

int numPrimes(int in)
{
	fk(prime.size()) if(prime[k] > in) return k;
	return 0;
}
vector<int> getPrimes(int in)
{
	vector<int> res(prime.size());
	fk(prime.size()) 
	{
		while((in%prime[k]) == 0) { res[k]++; in /= prime[k]; }
	}
	return res;
}

int countPlain(int in)
{
	vector<int> prime_count(prime.size());
	int res = 1;
	fi(in) 
	{
		vector<int> v = getPrimes(i+1);
		bool found = false;
		fj(v.size())
		{
			if(v[j] > prime_count[j])
			{
				found = true;
				prime_count[j] = v[j];
			}
		}

		if(found) res++;
	}
	return res;
}

int _tmain(int argc, _TCHAR* argv[])
{
	in	= fopen("C-small-attempt1.in","rt");
	out	= fopen("s_out.txt","wt");
	countPrime();
	
	int T = ri(); 
	for(int i = 0; i<T; i++)
	{
		int X = ri();
		int res;

		if(X == 1) res = 0;
		else if(X == 2) res = 1;
		else
		{
			res = countPlain(X) - numPrimes(X);
		}
		fprintf(out, "Case #%d: %d\n",i+1, res);
	}

	fclose(in);
	fclose(out);
	return 0;
}

