#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
	int T,t;
	long long n,A,B,C,D,x,y,M;
	int i,j,k;

	cin >> t;
	for(T=1;t--;T++) {
		vector<pair<long long, long long> > v;

		cin >> n >> A >> B >> C >> D >> x >> y >> M;

		v.push_back(make_pair(x,y));
		for(i=1;i<=n-1;i++) {
			x = (A*x+B) % M;
			y = (C*y+D) % M;
			v.push_back(make_pair(x,y));
		}

		
		int cnt=0;
		for(i=0;i<v.size();i++) {
			for(j=i+1;j<v.size();j++) {
				for(k=j+1;k<v.size();k++) {
					if(
						((v[i].first + v[j].first + v[k].first)%3==0) &&
						((v[i].second + v[j].second + v[k].second)%3==0)) cnt++;
				}
			}
		}

		printf("Case #%d: %d\n", T,cnt);
	}

	return 0;
}