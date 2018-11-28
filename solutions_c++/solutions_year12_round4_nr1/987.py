#include <iostream>
#include <fstream>

#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>

#define All(v)			v.begin(),v.end()

#define REP(i,a,b)		for(i=(int)a ; i<=(int)b ; i++)
#define FOR(i,N)		REP(i,0,N-1)

#define VI				vector<int>
#define VVI				vector<VI>

#define VD				vector<double>
#define VVD				vector<VD>

#define fst				first
#define scd				second
#define II				pair<int,int>
#define VII				vector<II>
#define VVII			vector<VII>

using namespace std;

int main(){
	ifstream cin("input.txt");
	ofstream cout("a2.out");
	int T;
	cin >> T;
	int cnt;
	REP(cnt,1,T){
		int i,j,k;
		int N;
		int W;
		VI D,L;
		
		cin >> N;
		D.resize(N); L.resize(N);
		FOR(i,N)
			cin >> D[i] >> L[i];
		cin >> W;

		bool ans = true;

		if(D[0] > L[0]){
			cout <<"Case #"<<cnt<<": NO";
			continue;
		}

		VI dp(N);
		dp[0] = D[0];
		FOR(i,N){
			REP(j,i+1,N-1){
				if(D[j]-D[i] > dp[i])
					break;
				dp[j] = max(dp[j],min(D[j]-D[i],L[j]));
			}
		}

		ans = false;
		FOR(i,N){
			if(W-D[i] <= dp[i]){
				ans = true;
				break;
			}
		}

		if(ans)
			cout<<"Case #"<<cnt<<": YES"<<endl;
		else
			cout<<"Case #"<<cnt<<": NO"<<endl;
	}
}