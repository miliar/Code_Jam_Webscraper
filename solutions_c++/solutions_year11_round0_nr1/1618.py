#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

struct A {
	string r;
	int b;
	A(string s, int i):r(s), b(i){}
};

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N;
		cin >> N;
		int O = 1;
		int B = 1;
		map<string, int> rp;
		rp["O"] = 1;
		rp["B"] = 1;
		vector<A> aseq;
		map<string, vector<int> > am;
		for (int j = 0; j < N; j++) {
			string r;
			int b;
			cin >> r >> b;
			aseq.push_back(A(r,b));
			am[r].push_back(b);
		}
		reverse(am["O"].begin(), am["O"].end());
		reverse(am["B"].begin(), am["B"].end());
		int time = 0;

		for (int k = 0; k < aseq.size(); k++) {
			string r = aseq[k].r;
			string lr = r=="O"?"B":"O";
			int nb = am[r].back();
			am[r].pop_back();
			int secs = abs(nb-rp[r])+1;
			rp[r] = nb;
			time += secs;

			if (am[lr].size() == 0)
				continue;
			int lnb = am[lr].back();
			int d = lnb-rp[lr];
			if (abs(d) <= secs)
				rp[lr] = lnb;
			else if (d < 0)
				rp[lr]-=secs;
			else if (d > 0)
				rp[lr]+=secs;
			
		}
		printf("Case #%d: %d\n", i+1, time);	
			
		
	}
}

