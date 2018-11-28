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
//FILE * g = fopen("a-small.out","wt");
ifstream f("a-large.in",ifstream::in);
ofstream g("a-large.out",ofstream::out);

ll C[3][3];
#define X(a) ((a)%3)
#define Y(a) ((a)/3)
int main()
{
	int nTests; f>>nTests;
	string s;
	ll a, b, c, d, x0, y0, m;
	int n;
	forn(nTestIndex,nTests)
	{
		f>>n>>a>>b>>c>>d>>x0>>y0>>m;
		memset(C,0,sizeof(C));
		C[x0 % 3][y0 % 3]++;
		ll x = x0, y = y0;
		for(int i=1;i<=n-1;i++)
		{
			x  = (a*x+b)%m;
			y  = (c*y+d)%m;
			C[x%3][y%3]++;
		}
		ll All = 0;
		//count all different
		int p1,p2,p3;
		for(p1=0;p1<9;p1++)
			for(p2=p1+1;p2<9;p2++)
				for(p3=p2+1;p3<9;p3++)
				{
					if (
						((X(p1)+X(p2)+X(p3))%3==0) && ((Y(p1)+Y(p2)+Y(p3))%3==0) ) 
						All += C[X(p1)][Y(p1)]*C[X(p2)][Y(p2)]*C[X(p3)][Y(p3)];
				}
		
		//count 2 idents
		for(p1=0;p1<9;p1++)
			for(p2=0;p2<9;p2++)
			{
				if (p1==p2) continue;
				if (
					((X(p1)+X(p2)+X(p1))%3==0) && ((Y(p1)+Y(p2)+Y(p1))%3==0) ) 
						All += (C[X(p1)][Y(p1)]*(C[X(p1)][Y(p1)]-1)*C[X(p2)][Y(p2)]) / 2;
			}

		for(p1=0;p1<9;p1++)
			All += (C[X(p1)][Y(p1)]*(C[X(p1)][Y(p1)]-1)*(C[X(p1)][Y(p1)]-2))/6;
		

		//fprintf(g,"Case #%d: ",TestIndex+1);
		g<<"Case #"<<nTestIndex+1<<": "<<All<<endl;
		cout<<"Case #"<<nTestIndex+1<<": "<<All<<endl;
		
	}
	return 0;
}
