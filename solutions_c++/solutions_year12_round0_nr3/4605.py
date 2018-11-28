/*
Yet another code by amrSamir
*/
#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;
typedef long long ll;
typedef long double ld;

int main()
{
	freopen("D.in","rt",stdin);
	freopen("D.out","wt",stdout);
	int tt;
	cin >> tt;
	for (int ii = 0; ii < tt; ++ii) {
		set<pair<int,int> > S;
		int a,b;
		int cnt = 0;
		cin >> a >> b;
		for (int i = a; i <= b; ++i) {
			int j;
			string s;
			stringstream ss;
			ss << i;
			ss >> s;
			string t;
			for (int k = 1; k < s.size(); ++k) {
				t = s.substr(k)+s.substr(0,k);
				//cerr << s << " " << t << endl;
				if(t[0] == '0')
					continue;
				stringstream ss2;
				ss2 << t;
				ss2 >> j;
				if( j <= i || j < a || j > b)
					continue;
				cnt++;
				S.insert(make_pair(j,i));
				//cerr << s << " " << t << endl;
			}
		}
		cout << "Case #" << ii+1 << ": " << S.size() <<endl;
	}
	return 0;
}
