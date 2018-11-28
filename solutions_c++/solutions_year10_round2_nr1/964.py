#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
//	freopen("A.in","r",stdin);freopen("A.outs","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.ans","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int T,N,M;
	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> N >> M;
		set <string> exists;
		exists.insert("/");
		string str;
		int total=0;
		for (int i=0; i<N; i++) {
			cin >> str;
			int pos=0;
			while ((pos=str.find("/",pos+1)) != -1) {
				exists.insert(str.substr(0,pos));
			}
			exists.insert(str);
		}
		for (int i=0; i<M; i++) {
			cin >> str;
			int pos=0;
			while ((pos=str.find("/",pos+1)) != -1) {
				if (exists.find(str.substr(0,pos)) == exists.end()) {
					exists.insert(str.substr(0,pos));
					total++;
				}
			}
			if (exists.find(str) == exists.end()) {
				exists.insert(str);
				total++;
			}
		}
		cout << "Case #" << t << ": " << total << endl;
	}

}