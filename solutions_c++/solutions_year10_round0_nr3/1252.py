#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <list>
#include <bitset>
#include <cstring>
#include <unistd.h>
#include <stack>
#include <cmath>
#include <map>
#include <streambuf>
#include <ctime>
#include <cstdlib>
#include <cassert>
#include <queue>

using namespace std;
using namespace __gnu_cxx;

typedef unsigned long long int uint64;
typedef long long int int64;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
#define FOR(x,a,e) for(int x=a; x<=(e); ++x)
#define FORL(x,a,e) for(int x=a; x<(e); ++x)
#define FORD(x,a,e) for(int x=a; x>=(e); --x)
#define FORDG(x,a,e) for(int x=a; x>(e); --x)
#define REP(x,n) for(int x =0;x<(n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) (c).begin(),(c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i,c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

struct group{
	
	uint64 number;
	uint64 count;
	
	group(uint64 _n, uint64 _c){
		number = _n;
		count  = _c;
	}
};

int main(){
	
	int C;
	cin >> C;
	FOR(i,1,C){
		cout<<"Case #"<<i<<": ";
		uint64 R,k,N;
		cin >> R >> k >> N;
		queue<group> q;
		FOR(j,1,N){
			uint64 g;
			cin >> g;
			group gg((uint64)j, g);
			q.push(gg);
		}
		uint64 res = 0;
		FOR(i,1,R){
			uint64 current = 0;
			group first = q.front();
			uint64 counter = 0;
			for(;;){
				++counter;
				group next = q.front();
				if (current+next.count > k || (next.number == first.number && counter > 1)) break;
				q.pop();
				current += next.count;
				q.push(next);
			}
			res += current;
		}
		cout<<res<<endl;
	}
	return 0;
}
