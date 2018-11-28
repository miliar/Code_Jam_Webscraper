#include<iostream>
#include<vector>
#include<queue>
#include<set>
#include<cstdio>
#include<algorithm>
#include<string>
#include<map>
#include<cmath>
#include<cstdlib>
#include<ctime>
using namespace std;


int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t; cin >> t;
	for (int k=0;k<t;k++) {
		int ret=0;
		vector<pair<int,int> > times;
		int l=0,r=0;
		int p1=1,p2=1;
		vector<vector<int> > p (2);
		int m; cin >> m;
		for (int i=0;i<m;i++) {
			char c; int pos;
			cin >> c >> pos;
			if (c=='O') {
				p[0].push_back(pos);
				times.push_back(make_pair(pos,0));
			}
			else {
				p[1].push_back(pos);
				times.push_back(make_pair(pos,1));
			}
		}
		for (int i=0;i<m;i++) {
			if (times[i].second==0) {
				if (p1<=p[0][l]) {
					for (;p1!=p[0][l];p1++) {
						ret++;
						if (r<p[1].size()) {
							if (p2<p[1][r]) p2++;
							else if (p2>p[1][r]) p2--;
						}
					}
				} else {
					for (;p1!=p[0][l];p1--) {
						ret++;
						if (r<p[1].size()) {
							if (p2<p[1][r]) p2++;
							else if (p2>p[1][r]) p2--;
						}
					}
				}
				ret++; l++;
				if (r<p[1].size()) {
					if (p2<p[1][r]) p2++;
					else if (p2>p[1][r]) p2--;
				}
			} else {
				if (p2<=p[1][r]) {
					for (;p2!=p[1][r];p2++) {
						ret++;
						if (l<p[0].size()) {
							if (p1<p[0][l]) p1++;
							else if (p1>p[0][l]) p1--;
						}
					}
				} else {
					for (;p2!=p[1][r];p2--) {
						ret++;
						if (l<p[0].size()) {
							if (p1<p[0][l]) p1++;
							else if (p1>p[0][l]) p1--;
						}
					}
				}
				ret++; r++;
				if (l<p[0].size()) {
					if (p1<p[0][l]) p1++;
					else if (p1>p[0][l]) p1--;
				}
			}
		}
		printf("Case #%d: %d\n",k+1,ret);
	}
	return 0;
}
