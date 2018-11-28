#include <list>
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <sstream>

using namespace std;

typedef unsigned long long int u64;
typedef long long int i64;

vector<pair<int, int> > lol;

int main() {
	int NC;

	cin >> NC;
	
	for(int cs=1;cs<=NC;cs++) {
		lol.clear();
		long double mx=0.0,aux;
		int C,D;
		cin >> C >> D;
		for(int i=0;i<C;i++) {
			int P,V;
			cin >> P >> V;
			pair<int, int> pp(P,V);
			lol.push_back(pp);
		}
		
		sort(lol.begin(),lol.end());
		int N=lol.size(),num;
		for(int i=0;i<N;i++) {
			num=0;
			for(int j=i;j<N;j++) {
				num+=lol[j].second;
				aux=(D*(num-1)-(lol[j].first-lol[i].first))/2.0;
				mx=(aux>mx)?aux:mx;
			}
		}
		
		
	
		cout << "Case #" << cs << ": " <<  mx << endl;
	}
	
	return 0;
}