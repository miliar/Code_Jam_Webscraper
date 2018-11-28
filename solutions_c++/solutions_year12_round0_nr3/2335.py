#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <queue>
#include <algorithm>
#include <cmath>
#include <sstream>
using namespace std;
#define PB push_back
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FORE(i,x) for(__typeof((x).begin()) i=(x).begin();i != (x).end();++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,w) memset((x),w,sizeof (x))
#define X first
#define Y second
typedef long long int lli;
typedef pair<int, int> P;
typedef vector<int> VI;

int pot;

inline int rec(int x){
	return (x%10) * pot + x / 10;
}

int T,A,B,res;

int main(){
    cin >> T;
	FOR(cas, 1, T){
		cin >> A >> B;
		pot = 1;
		while(10 * pot <= B)
			pot *= 10;
		res = 0;
		FOR(i,A,B)
			for(int j=rec(i); j != i; j=rec(j))
				res += (i < j && j <= B);
		cout << "Case #" << cas << ": " << res << endl;
	}
    return 0;
}
