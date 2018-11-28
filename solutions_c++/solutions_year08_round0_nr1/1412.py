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

int main(void) {
	int T;
	int C = 1;
	int S, Q;
	int res = 0;
	//set<string> e;
	set<string> q;
	cin >> T;
	string str;
	int used;
	while(T--){
		res = 0;
		//e.clear();
		scanf("%d\n", &S);
		for(int i = 0; i < S; ++i) {
			getline(cin, str);
			//e.insert(str);
		}
		scanf("%d\n", &Q);
		q.clear();
		used = 0;
		for(int i = 0; i < Q; ++i) {
			getline(cin, str);
			if(q.find(str) != q.end()) continue;
			q.insert(str);
			used++;
			if(used == S) {
				res++;
			//	printf("clearing @ i = %d\n", i);
				q.clear();
				used = 1;
				q.insert(str);
			}
		}
		printf("Case #%d: %d\n", C, res);
		C++;
	}
	return 0;
}
