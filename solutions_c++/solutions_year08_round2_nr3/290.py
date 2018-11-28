#include <iostream>
#include <vector>
#include <map>
#include <cctype>
#include <climits>
#include <sstream>
#include <algorithm>
#include <cassert>

#define All(v) (v).begin(),(v).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x))

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)

using namespace std;

static void solve_case(int i);

int main(void){

	int N;
	cin >> N;
	for(int i = 0; i < N; i++){
		solve_case(i+1);
	}

	return 0;
}

void solve_case(int cn){
	int K, n;
	cin >> K >> n;

	vector<int> deck(K+1,0);

	int p = 0;

	REP(i,K){
		int c = i;
		
		while(c != 0){
			while(deck[p] != 0){
				if(++p == K)
					p = 0;
			}
			if(++p == K)
				p = 0;
			c--;
		}
		while(deck[p] != 0){
			if(++p ==K)
				p = 0;
		}
		deck[p] = i+1;
	}

	cout << "Case #" << cn << ": " ;
	REP(i,n){
		int idx;
		cin >> idx;
		cout << deck[idx-1] << " ";
	}
	cout << endl;
}


