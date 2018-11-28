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

int g[120][120];

int main()
{
	int T;
	cin>>T;
	string line;
	getline(cin, line);
	REP(index, T)
	{
		cout<<"Case #"<<index+1<<": "<<endl;
		//
		int N;
		cin>>N;
		getline(cin, line);
		REP(i,N) 
		{
			getline(cin, line);
			REP(j,N)
			{
			char tmp=line[j];
			if(tmp=='.') g[i][j]=-1;
			else g[i][j]=tmp-'0';
			}
		}
		//REP(i,N) {REP(j,N) cout<<g[i][j]<<" "; cout<<endl;}
		vector<double> wp(N), owp(N), oowp(N);
		vector<int> tt(N), wins(N);
		REP(i,N)
		{
			int total=0;
			int win=0;
			REP(j,N)
			{
				if(g[i][j]==-1) continue;
				total++;
				if(g[i][j]==1) win++;
			}
			tt[i]=total;
			wins[i]=win;
			wp[i]=win/(double)total;
		}
		//
		REP(i,N)
		{
			int total=0;
			double p=0;
			REP(j,N) if(j!=i and g[j][i]!=-1)
			{
				total++;
				if(g[j][i]==0) p+=(wins[j])/(double)(tt[j]-1);
				else p+=(wins[j]-1)/(double)(tt[j]-1);
			}
			owp[i]=p/total;
		}
		REP(i,N)
		{
			int total=0;
			double p=0;
			REP(j,N) if(g[i][j]!=-1)
			{
				total++;
				p+=owp[j];
			}
			oowp[i]=p/total;
		}
		REP(i,N) 
		{
			//cout<<wp[i]<<" "<<owp[i]<<" "<<oowp[i]<<" ";
			cout<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
		}
	}
	return 0;
}
