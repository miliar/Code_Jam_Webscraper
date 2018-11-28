#include <cstdio>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>

#include <set>
#include <vector>
#include <utility>
#include <map>

#include <algorithm>

using namespace std;


typedef pair<int,int> pii;
typedef vector<string> VS;
typedef vector<int> VI;

typedef __int64 ll;

#define all(v) (v).begin(),(v).end()
#define foreach(it, v, type) for(type::iterator it = (v).begin(); it != (v).end(); ++it)
#define pb push_back
#define forn(i,N) for(int i=0;i<(N); ++i)

//FILE * f = fopen("a.in","rt",stdin);
//FILE * g = fopen("a-large.out","wt");
ifstream f("a-large.in",ifstream::in);
ofstream g("a-large.out",ofstream::out);

int Sw[1001][101];
int M[1001];
const int Inf = 0x1000000;
int main()
{
	int Tests; f>>Tests;
	string s;

	forn(TestIndex,Tests)
	{
		//fprintf(g,"Case #%d: ",TestIndex+1);
		g<<"Case #"<<TestIndex+1<<": ";
		cout<<"Case #"<<TestIndex+1<<": "<<endl;

		int m; int n;
		f>>m; getline(f,s);
		
		map<string,int> msi;
		
		forn(i,m)
		{
			getline(f,s);
			msi[s]=i;
		};

		f>>n; getline(f,s);
		if (n==0)
		{ 
			g<<"0"<<endl;
			continue;
		}

		VI v(n);
		forn(i,n)
		{
			getline(f,s);
			v[i]=msi[s];
		}
		
		forn(i,n)
		{
			forn(k,m)
			{
				if (v[i]==k) //cannot do that
				{
					Sw[i][k] = Inf;
					continue;
				}
				Sw[i][k] = min(((i>0)?M[i-1]:0)+1, (i>0)?Sw[i-1][k]:0);
			}
			
			M[i]=Sw[i][0];
			forn(k,m) M[i]=min(M[i],Sw[i][k]);
		}
		g<<M[n-1]<<endl;
	}
	return 0;
}