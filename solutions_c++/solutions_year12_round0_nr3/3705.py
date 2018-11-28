#include <iostream>
#include <sstream>
#include <set>
#include <vector>
#include <string>

#define REP(i,n) for(int i = 0; i < n; i++)
#define pb push_back
#define mkp make_pair

using namespace std;

int a, b, tp;
int main() {
	int kases;
	cin >> kases;
	REP(kase,kases) {
		cin >> a >> b;
		set < pair<int,int> > ans;

		int tmp = a;
		tp = 1;
		while(tmp) tp *= 10, tmp /= 10;
		tp /= 10;

		char buf[100];
		string s;
		for(int n = a; n <= b; n++) {
			sprintf(buf, "%d", n);
			s = buf;

			int q = n;
			do {
				s = s.substr(s.size()-1) + s.substr(0,s.size()-1);
				sscanf(s.c_str(), "%d", &q);
        		if(q != n && q >= a && q <= b) {
					int sm = min(n,q), bg = max(n,q);
					ans.insert(mkp(sm,bg));
				}
			}
			while(q != n);
		}

		cout << "Case #" << kase+1 <<": "<< ans.size() << endl;
	}

}