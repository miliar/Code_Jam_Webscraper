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

struct WW
{
	double b,e,s;
	bool operator <(const WW & r)
	{
		if(b < r.b) return true;
		return false;
	}
};

struct WS
{
	double s,b,l;
	bool operator <(const WS & r)
	{
		if(s < r.s) return true;
		return false;
	}
};

int _tmain(int argc, _TCHAR* argv[])
{
	in	= fopen("A-large.in","rt");
	out	= fopen("l_out.txt","wt");
	
	int T = ri(); 
	for(int i = 0; i<T; i++)
	{
		double X = ri();
		double S = ri();
		double R = ri();
		double t = ri();
		int N = ri();


		vector<WW> ww(N);
		fj(N)
		{
			ww[j].b = ri();
			ww[j].e = ri();
			ww[j].s = ri();
		}
		sort(all(ww));
		vector<WS> ws;

		int curb = 0;
		fj(N)
		{
			WS s;
			if(curb != ww[j].b)
			{
				s.b = curb;
				s.s = 0;
				s.l = ww[j].b-curb;
				ws.push_back(s);
			}
			s.b = ww[j].b;
			s.s = ww[j].s;
			s.l = ww[j].e-ww[j].b;
			ws.push_back(s);
			curb = ww[j].e;
		}
		if(curb != X)
		{
			WS s;
			s.b = curb;
			s.s = 0;
			s.l = X-curb;
			ws.push_back(s);
		}
		sort(all(ws));

		double s = 0;
		fj(ws.size())
		{
			if(t > 0)
			{
				double tr = ws[j].l / (ws[j].s+R);
				if(tr <= t) 
				{
					s += tr;
					t -= tr;
					continue;
				}
				else
				{
					s += t;
					ws[j].l -= (ws[j].s+R)*t;
					t = 0;
				}
			}
			s += ws[j].l / (ws[j].s+S);
		}
		fprintf(out,"Case #%d: %f\n",i+1, s);
	}

	fclose(in);
	fclose(out);
	return 0;
}

