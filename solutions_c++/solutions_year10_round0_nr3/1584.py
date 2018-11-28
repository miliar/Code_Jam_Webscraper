//Author: suh_ash2008
#include <iostream>
#include <cstdio>
#include <cctype>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cassert>
#include <string.h>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LL t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define SET(x,a) memset(x,a,sizeof(x));
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define tr(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define pb push_back
#define sz(a) (int)(a.size())
#define INF (int)1e9
#define EPS (double)1e-12
#define is istringstream
#define os ostringstream
#define lb lower_bound
#define ub upper_bound
#define bs binary_search

typedef long long LL;
typedef unsigned long long ULL;
typedef pair< int,int > ii;
typedef vector< ii > vii;
typedef vector < vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;
typedef vector< string > vs;

#define MAXN 1000+5
int seen[MAXN], next_inx[MAXN];
int weight[MAXN], cost[MAXN];

int main(){
	ifstream fin("C.in");
	ofstream fout("C.out");
	int _, kase = 0;
	fin >> _;
	while(_--){
		kase++;
		int R, k, N;
		fin >> R >> k >> N;
		REP(i, N)    fin >> weight[i];
		SET(cost, 0);
		SET(seen, -1);
		// generate cost and next index to go to - O(N^2)
		REP(i, N){
			cost[i] = weight[i];
			int j = (i + 1) % N;
			while( 1 ){
				if(j == i){
					next_inx[i] = j;
					break;
				}
			    if(cost[i] + weight[j] <= k)    cost[i] += weight[j], (j += 1) %= N;
			    else{
					next_inx[i] = j;
					break;
				}
			}
		}
		// simulate until we find a cycle
		// cycle is obtained in atmost 'N' iterations
		LL ans = 0;
		int round = 0, inx = 0;
		while( 1 ){
			if(round == R)    break;
		    if(seen[inx] == -1){
				// no cycle yet, continue
			    seen[inx] = round;
			    ans += cost[inx];
			    inx = next_inx[inx];
			    round++;
			}
			else{
			    // found a cycle
				int cycle_len = round - seen[inx];
				int cur = next_inx[inx];
				LL cycle_weight = cost[inx];
				while(cur != inx){
				    cycle_weight += cost[cur];
					cur = next_inx[cur];	
				}
				int rem_rounds = R - round;
				ans += (rem_rounds / cycle_len) * cycle_weight;
				rem_rounds -= (rem_rounds / cycle_len) * cycle_len;
				round = R - rem_rounds;
				while( 1 ){
				    if(round == R)    break;
				    ans += cost[inx];
				    inx = next_inx[inx];
				    round++;
				}
				break;
			}
		}
		fout << "Case #" << kase << ": " << ans << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
