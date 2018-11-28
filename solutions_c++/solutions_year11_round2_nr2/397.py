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


int _tmain(int argc, _TCHAR* argv[])
{
	in	= fopen("B-small-attempt0 (3).in","rt");
	out	= fopen("s_out.txt","wt");
	
	int n = ri(); 
	for(int i = 0; i<n; i++)
	{
		int num = ri();
		int mn = ri();
		vector<pair<int,int>> t(num);

		for(int j = 0; j<num; j++)
		{
			t[j].first  = ri();
			t[j].second = ri();
		}

		sort(all(t));
		double maxt = 0;
		double grsh(num);
		fj(num)
		{
			for(int k = j; k<num; k++)
			{
				int len = 0;
				for(int i = j; i<=k; i++)
					len += t[i].second;
				double ct = (len*mn - (t[k].first-t[j].first+mn))/2.;
				if(ct > maxt) maxt = ct;
			}
		}

		fprintf(out,"Case #%d: %f\n",i+1, maxt);
	}

	fclose(in);
	fclose(out);
	return 0;
}

