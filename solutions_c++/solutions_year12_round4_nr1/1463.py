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

typedef pair<int,int> pii;

int main() {
	int t; cin>>t;
	for (int T=1; T<=t; T++) {
		set<pii> st,vis;
		int n; cin>>n;
		queue<pii> q;
		for (int i=0; i<n; i++) {
			int d, l; cin>>d>>l;
			if(!i) q.push(make_pair(d,d));
			st.insert(make_pair(d,l));
		}
		int D; cin>>D;

		string ans="NO";
		while(!q.empty()) {
			pii cur=q.front(); q.pop();
			int x=cur.first, a=cur.second;
// cout << x << " " << a << endl;
			if(x+a>=D) { ans="YES"; break; }
			for(set<pii>::iterator it=st.begin(); it!=st.end(); it++) {
				pii tmp=(*it);
				int y=tmp.first, b=tmp.second, c=min(b,abs(x-y));
				if(abs(x-y)<=a) {
// cout << "##" << y << " " << b << " :: " << c << endl;
					pii nxt=make_pair(y,c);
					if(vis.find(nxt)==vis.end()) {
						vis.insert(nxt);
						q.push(nxt);
					}
				}
			}
		}
		cout << "Case #" << T << ": " << ans << endl;
	}
	return 0;
}
