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

using namespace std;

int main() {
	

	map<int,int> mapLine;
	map<int,int>::iterator iter;
	map<int,int>::iterator temp;

	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int T;
	int a = 0, b = 0, n = 0;
	long count=0;
	
	cin>>T;
	For(i, 1, T) {
		
		cin>>n;
		For(j,1,n){
			cin>>a>>b;
			mapLine.insert(pair<int,int>(a,b));
		}
		for(temp=mapLine.begin();temp!=mapLine.end();temp++){
			for(iter=mapLine.begin();iter!=temp;iter++){
				if((iter->second)>(temp->second))
					count++;          
			}
		}
		
		cout<<"Case #"<<i<<": "<<count<<endl;
		mapLine.clear();
		count=0;
	}
	return 0;
}