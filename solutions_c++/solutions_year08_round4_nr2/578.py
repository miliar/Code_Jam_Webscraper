#define inFileName "b-small-attempt1.in"
#define outFileName "b-small.out"

#include <cstdio>
#include <iostream>
#include <fstream>

//FILE * f = fopen(inFileName,"rt");
//FILE * g = fopen(outFileName,"wt");
std::ifstream f(inFileName,std::ifstream::in);
std::ofstream g(outFileName,std::ofstream::out);

#include <strstream>
#include <sstream>

#include <cmath>
#include <string>

#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>

#include <utility>
#include <algorithm>

using namespace std;

typedef pair<int,int> pii;
typedef vector<string> VS;
typedef vector<int> VI;
typedef __int64 ll;

#define all(v) (v).begin(),(v).end()
#define foreach(it, v, type) for(type::iterator it = (v).begin(); it != (v).end(); ++it)
#define forn(i,N) for(int i=0;i<(N); ++i)
#define pb push_back

//////////////////////////////////////////////////////////////////////////

VI X(3);
VI Y(3);
int n, m;
int a;

bool form(int ux, int uy, int vx, int vy, VI& X,VI& Y)
{
	int x = max(max(0,-ux),-vx);
	int y = max(max(0,-uy),-vy);
	X[0]=x; Y[0]=y;
	X[1]=ux+x; Y[1]=uy+y;
	X[2]=vx+x; Y[2]=vy+y;
	forn(i,3) if ( (X[i]<0) || (X[i]>n) || (Y[i]<0) || (Y[i]>m)) return false;
	return true;
}

bool solve(int a)
{
	for(int ux=-n;ux<=n;ux++)
		for(int uy=0;uy<=m;uy++)
			for(int vx=-n;vx<=n;vx++)
				for(int vy=0;vy<=m;vy++)
				{
					if ((ux==0)&&(uy==1)&&(vx==1)&&(vy==1))
					{
						ux=ux;
					}
					if (abs(ux*vy-uy*vx)!=a)
						continue;
					if (!form(ux,uy,vx,vy,X,Y))
						continue;
					return true;
				}
	return false;
}

int main()
{
	int nTests; f>>nTests;
	string s;

	forn(TestIndex,nTests)
	{
		//fprintf(g,"Case #%d: ",TestIndex+1);
		g<<"Case #"<<TestIndex+1<<": ";
		cout<<"Case #"<<TestIndex+1<<": ";
		f>>n>>m>>a;
		//a=a*2;

		if (!solve(a))
			g<<"IMPOSSIBLE",
			cout<<"IMPOSSIBLE";
		else
		{
			forn(i,3) g<<X[i]<<" "<<Y[i]<<" ";
			forn(i,3) cout<<X[i]<<" "<<Y[i]<<" ";
		}
		g<<endl;
		cout<<endl;
	}
	return 0;
}
