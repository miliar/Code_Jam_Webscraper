#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

typedef vector<int> vi;
typedef unsigned long long uint64;
typedef long long int64;

#define FOR(i,a,b) for(int64 i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int64 i=(a),_b=(b);i>=_b;i--)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)

#define ALL(x) (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 


int main() {

	int T;
	cin >> T;

	FOR(t,1,T){

		int64 R, K, N;
		cin >> R >> K >> N;

		vi G(2*N);
		vi moneyEach(N);
		vi money(N);
		vi nextS(N);
		vi steps(N);
		vi start(N);
		int64 sum = 0;

		FOR(n,0,N-1) {cin >> G[n]; G[N+n] = G[n];}

		int64 i = 0;
		int64 next;
		while (sum < K && i < N) {
			sum+=G[N-1+i];
			i++;
		}
		
		if (sum > K ){
			next = N-1+i-1;
			sum -= G[next];
		}
		else{
			next = N-1+i;
		}
		steps[N-1] = 1;
		moneyEach[N-1] = sum;
		money[N-1] = sum;
		nextS[N-1] = next-N;
		start[N-1] = next-N;
		

		FORD(n,N-2,0){
			sum += G[n];
			i = next-1;
			if (i - n == N) {sum -= G[i];i--; }
			while(sum>K) {sum -= G[i]; i--; }
			next = i+1;
			moneyEach[n] = sum;
			money[n] = (next>N-1 ? sum : sum+money[next]);
			nextS[n] = (next>N-1 ? next - N : next);
			start[n] = (next>N-1 ? next - N : start[next]);
			steps[n] = (next>N-1 ? 1 : steps[next]+1);
		}
		int64 all = 0;

		int64 count = 0;
		int64 index = 0;
		while (count+steps[index] <=R){
			all += money[index];
			count += steps[index];
			index = start[index];
		}

		while(count<R){
			all += moneyEach[index];
			count ++;
			index = nextS[index];
		}

		cout <<"Case #"<<t<<": "<< all <<endl;
	}
		
	return 0;
}
