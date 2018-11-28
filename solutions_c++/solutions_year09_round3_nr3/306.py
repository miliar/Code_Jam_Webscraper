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

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)

#define ALL(x) (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

int count_gold(vi Q, int P){
	int res = 0;

	for (int i = 0; i < Q.size(); i++){
		int above = P+1, below = 0;
		for(int j = 0; j <i; j ++){
			if(Q[j]>Q[i] && Q[j]<above) above = Q[j];
			if(Q[j]<Q[i] && Q[j]>below) below = Q[j];
		}
		res += (above - below - 2);
	}

	return res;
}

int main() {

	int C;
	cin >> C;
	int gold, gold_t;

	FOR(c,1,C){

		int P,Q;
		cin >> P >> Q;

		vi Q_map(Q);

		int t;
		for (int i =0; i < Q; i ++){
			cin >> Q_map[i];
		}
		gold = -1;
		do {
			gold_t = count_gold(Q_map, P);
			if (gold == -1 || gold > gold_t) gold = gold_t;	
		
		}while(next_permutation(Q_map.begin(),Q_map.end()));


		cout <<"Case #"<<c<<": "<< gold <<endl;
	}
		
	return 0;
}
