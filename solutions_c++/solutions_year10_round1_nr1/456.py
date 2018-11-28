#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
#include <iomanip>

using namespace std;

typedef vector <int> VI;
typedef vector <string> VS;
typedef long long LL;
typedef stringstream SS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define PB push_back
#define sz size()
#define MP make_pair
#define two(x) (1<<(x))


/////////////////////////////////////////////////////////////////////////////////

int T,N,K;

char g[55][55];

int dx[]={0,1,1,1};
int dy[]={1,0,1,-1};

int main()
{
	cin>>T;
	REP(index, T)
	{
		cin>>N>>K;
		for(int j=N-1; j>=0; j--) for(int i=0; i<N; i++)  cin>>g[i][j];
		//REP(i,N) {REP(j,N) cout<<g[i][j]; cout<<endl;}
		
		//cout<<"*********"<<endl;
		REP(j,N)
		{
			for(int i=N-1; i>=0; i--) if(g[i][j]!='.')
			{
				int k=i+1;
				while(k<N and g[k][j]=='.') { swap(g[k][j], g[k-1][j]); k++;}
			}
		}
		
		bool red=false, blue=false;

		REP(i,N) REP(j,N) 
		{
			if(g[i][j]=='.') continue;
			char c=g[i][j];

			REP(p,4)
			{
				bool ok=true;
				REP(k,K)
				{
					int nx=i+k*dx[p];
					int ny=j+k*dy[p];

					if(nx<0 or nx>=N or ny<0 or ny>=N or g[nx][ny]!=c) { ok=false; break; }
				}
				if(ok)
				{
					if(c=='R') red=true;
					if(c=='B') blue=true;
				}
			}
		}

		cout<<"Case #"<<index+1<<": ";
		if(red and blue) cout<<"Both";
		else if( red) cout<<"Red";
		else if(blue) cout<<"Blue";
		else cout<<"Neither";
		cout<<endl;
	}

	return 0;
}
