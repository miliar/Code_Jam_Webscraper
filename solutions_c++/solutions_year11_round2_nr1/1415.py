#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define all(a) (a).begin(),(a).end()
#define sz(a) ((int) (a).size())
#define pb push_back
#define CL(a,b) memset((a),(b),sizeof(a))

#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;
int N;
		string vs[105];		int op[105];
				double WP[105],OWP[105],OOWP[105];
void go()
{
REP(i,N)
{
	

			double sum=0;
			int di=0;

			REP(j,N)
			{
				char c=vs[i][j];//
				if(c!='.')op[di++]=j;
			}
			REP(j,di)
			{
				int w=0,l=0;
				REP(k,N)
				{
					if(k==i)continue;
					if(vs[op[j]][k]=='1')w++;
					else if(vs[op[j]][k]=='0')l++;
				}
				sum+=w*1.0/(w+l);
			}
			sum/=di;
			OWP[i]=sum;
			
}
	
}
int main() {
 	freopen("A.txt","r",stdin);
 	freopen("AOUT.txt","w",stdout);
	int T, cI=1;
	cin >> T;
	while (T--)
	{

		cin>>N;
	
		REP(i,N)cin>>vs[i];
		cout<<"Case #"<<cI++<<":"<<endl;

		REP(i,N)
		{
			int w=0,l=0;
			REP(j,N)if(vs[i][j]=='1')w++;else if(vs[i][j]=='0')l++;
			WP[i]=w*1.0/(w+l);
			go();

			int di=0;
			REP(j,N)
			{
				if(vs[i][j]!='.')op[di++]=j;
			}

			double sm=0;
			REP(j,di)
			{
				if(i==op[j])continue;
				sm+=OWP[op[j]];
			}
			sm/= di;
			OOWP[i]=sm;
			double RPI=0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i];
			cout<<RPI<<endl;
		}
	}
    
	return 0;
}
