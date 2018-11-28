#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;


typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

int main() {
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);


	int T;
	long a = 0, b = 0;
	int count = 0,fac,mint = 0;
	cin>>T;
	For(i, 1, T) {
		count = 0;
		mint = 0;
		cin>>a>>b>>fac;
		while(a*fac<b){
      a=a*fac;
      count++;
			}
		while((pow(2,mint)-1)<count){
      mint++;
    }
		
		cout<<"Case #"<<i<<": "<<mint<<endl;
	}
	return 0;
}