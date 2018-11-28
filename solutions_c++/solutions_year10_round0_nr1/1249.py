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

int main(){
	
	vector<uint64> powers(31, 0);
	powers[0] = 1;
	FOR(i, 1, 30){
		powers[i] = powers[i-1] << 1;
	}
	
	int T, N, K;
	cin >> T;
	int cc = 0;
	while (T--){
		++cc;
		cout << "Case #"<<cc<<": ";
		cin >> N >> K;
		if (K == 0){
			cout<<"OFF\n";
		}
		else{
			uint64 S = powers[N] - 1;
			uint64 O = powers[N];
			
			if (K == S || (K-S)%O == 0 ) cout<<"ON\n";
			else cout<<"OFF\n";
		}
	}	
	return 0;
}