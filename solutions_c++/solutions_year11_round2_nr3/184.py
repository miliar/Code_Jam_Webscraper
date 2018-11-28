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

bool bruteforse(vector<vector<int>> pol, int nv, int maxf, int cv, vector<int>& r)
{
	if(nv == cv)
	{
		fi(pol.size())
		{
			vector<bool> exists(maxf);
			fj(pol[i].size()) exists[r[pol[i][j]]] = true;
			if(find(all(exists), false) != exists.end()) return false;
		}
		return true;
	}
	for(r[cv] = 0; r[cv] < maxf; r[cv]++)
		if(bruteforse(pol,nv,maxf,cv+1,r)) return true;

	return false;
}

int _tmain(int argc, _TCHAR* argv[])
{
	in	= fopen("C-small-attempt0 (1).in","rt");
	out	= fopen("s_out.txt","wt");
	
	int n = ri(); 
	for(int i = 0; i<n; i++)
	{
		int nv = ri();
		int ns = ri();
		vector<pair<int,int>> t(ns);

		fj(ns)	t[j].first  = ri()-1;
		fj(ns)	t[j].second  = ri()-1;

		vector<vector<int>> pol(1);
		fj(nv)	pol[0].push_back(j);
		fj(ns)	
		{
			fk(pol.size())	
			{
				vector<int>::iterator f = find(all(pol[k]),t[j].first);
				vector<int>::iterator s = find(all(pol[k]),t[j].second);
				if(f != pol[k].end() && s != pol[k].end())
				{
					pol.push_back(vector<int>(f,s+1));
					pol[k].erase(f+1,s);
					break;
				}
			}
		}

		int maxf = 10000;
		fk(pol.size())	
			if(pol[k].size() < maxf) maxf = pol[k].size();

		while(maxf)
		{
			vector<int> r(nv);
			if(bruteforse(pol,nv,maxf,0,r))
			{
				fprintf(out,"Case #%d: %d\n",i+1, maxf);
				fj(nv) 
				{
					fprintf(out,"%d",r[j]+1);
					if(j < nv-1) fprintf(out," ");
					else fprintf(out,"\n");
				}
				break;
			}
		}
	}

	fclose(in);
	fclose(out);
	return 0;
}

