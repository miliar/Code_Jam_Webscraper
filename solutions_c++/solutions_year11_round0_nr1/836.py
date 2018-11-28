#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <map>
#include <set> 
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
#define REP(i,a) for(int i=0;i<a;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define SIZE(c) (int)c.size()
#define ALL(c) (c).begin(),(c).end() 
typedef pair<int, int> PII;
const int INF = 1000000000;
const int MAXN = 105;
int T, N, move[MAXN], turn[MAXN], x[5];
char tmp;
int solve(){
	x[0] = x[1] = 1; 
	int t = turn[0], idx = 0, ret = 0;
	while(idx < N){
		int tot = 0;
		while(idx < N && turn[idx] == t){
			tot += abs(x[0] - move[idx]) + 1;
			x[0] = move[idx];
			idx ++;
		}
		if(idx < N){
			int need = abs(move[idx] - x[1]);
			if(need > tot){
				x[1] = move[idx] - (need - tot);
			}
			else{
				x[1] = move[idx];
			}
			swap(x[0], x[1]);
			t ^= 1;
		}
		ret += tot;
	}
	return ret;
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);
	cin>>T;
	REP(t, T){
		cin>>N;
		REP(i, N){
			cin>>tmp;
			if(tmp == 'O') turn[i] = 0;
			else turn[i] = 1;
			cin>>move[i];
		}
		cout<<"Case #"<<(t+1)<<": ";
		cout<<solve()<<endl;
	}
	return 0;
}
