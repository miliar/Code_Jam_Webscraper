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
char sbuf[100005]; 
string rstr() 
{
	//fscanf(in, "%lf", sbuf); 
	char c;
	char * b = sbuf;
	while(c = fgetc(in))
	{
		if(c == '\n' || c == 255) break;
		*b++=c;
	}
	*b = 0;
	return sbuf; 
}
long long rll() { long long a; fscanf(in, "%lld", &a ); return a; }


bool solve(int * v, int s, int n, int m, int * r, int len)
{
	if(n == 1) 
	{
		if(v[s] > s+1) 
			return false;
		double mn = m;
		for(int i = v[s]+1; i<len; i++)
		{
			double cur = m-(r[i]-m)/(double)(i-v[s])*(i-s);
			if(cur < mn)
				mn = cur;
		}
		
		m = (int)mn;
		r[s] = m;
		return true;
	}

	if(v[s] < n+s)
	{
		if(!solve(v,v[s],n-v[s]+s, m, r, len))
			return false;
		m = r[v[s]];
	}


	if(v[s] > n + s) 
		return false;

	if(v[s] - s == 0) 
		return false;
	
	double mn = m;
	for(int i = v[s]+1; i<len; i++)
	{
		double cur = m-(r[i]-m)/(double)(i-v[s])*(i-s);
		if(cur < mn) mn = cur;
	}
	
	m = (int)mn;
	r[s] = m;
	if(v[s] - s == 1) 
		return true;

	if(!solve(v,s+1,v[s]-s-1,m-1, r, len)) return false;
	
	return true;

}
bool checkIsCorrect(int * v, int * r, int len)
{
	for(int i = 0; i<len-1; i++)
	{
		double ungmax = -1e100;
		int ind = i;
		for(int k = i+1; k<len; k++)
		{
			double ung = (r[k] - r[i])/(double)(k-i);
			if(ung > ungmax)
			{
				ungmax = ung;
				ind = k;
			}
		}
		if(ind != v[i]) 
			return false;
	}
	return true;
}

long _tmain(int argc, _TCHAR* argv[])
{
	in	= fopen("C-small-attempt3.in","rt");
	out	= fopen("s_out.txt","wt");
	
	int T = ri(); 

	__int64 input[1024];
	for(int i = 0; i<T; i++)
	{
		int h = ri(); 
		vector<int> v(h);
		vector<int> r(h);
		fk(h-1) v[k] = ri()-1;
		v[h-1] = h-1;

		fprintf(out, "Case #%d:",i+1);
		printf("Case #%d:",i+1);
		if(!solve(&v[0], 0, h, 1000000000, &r[0], h))
		{
			fprintf(out, " Impossible\n");
			printf(" Impossible\n");
		}
		else
		{
			int mn = 1000000000;
			fk(h) mn = min(r[k],mn);
			checkIsCorrect(&v[0], &r[0], h);
			fk(h) 
			{
				fprintf(out, " %d",r[k]-mn+1);
				printf(" %d",r[k]-mn+1);
			}
			fprintf(out, "\n");
			printf("\n");
		}
	}

	fclose(in);
	fclose(out);
	return 0;
}

