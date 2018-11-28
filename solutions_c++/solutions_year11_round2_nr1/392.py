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

double WP(string & score, int ex)
{
	int win = 0, lose = 0; 
	fi(score.size())
	{
		if(i == ex) continue;
		if(score[i] == '.')  continue;
		if(score[i] == '1')  win++;
		else lose++;
	}
	return double(win)/(lose+win);
}

int _tmain(int argc, _TCHAR* argv[])
{
	in	= fopen("A-large (3).in","rt");
	out	= fopen("out_l.txt","wt");
	
	int n = ri(); 
	for(int i = 0; i<n; i++)
	{
		int num = ri();
		vector<double> rpi(num);
		vector<double> wp(num);
		vector<double> owp(num);
		vector<double> oowp(num);
		
		vector<string> table(num);
		for(int j = 0; j<num; j++)
		{
			table[j] = rs();
		}
		
		for(int j = 0; j<num; j++)
		{
			wp[j] = WP(table[j],-1);
			int q = 0;
			fk(num) if(k != j && table[k][j] != '.') { owp[j] += WP(table[k],j); q++; }
			owp[j] /= q;
		}
		for(int j = 0; j<num; j++)
		{
			int q = 0;
			fk(num) if(k != j && table[k][j] != '.') { oowp[j] += owp[k]; q++; }
			oowp[j] /= q;
		}
		fprintf(out,"Case #%d:\n",i+1);
		for(int j = 0; j<num; j++)
			fprintf(out,"%f\n",wp[j]*0.25+owp[j]*0.5+oowp[j]*0.25);
	}

	fclose(in);
	fclose(out);
	return 0;
}

