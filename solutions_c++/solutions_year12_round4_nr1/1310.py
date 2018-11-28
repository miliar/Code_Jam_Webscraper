#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

typedef long long LL;

int DX[4]={-1,0,1,0};
int DY[4]={0,1,0,-1};


int main() {
	int T;
	cin >> T;


	for (int t=1; t<=T; t++) {
		int N,D;
		cin>>N;
		vector<int> vx,vl;
		vx.resize(N);
		vl.resize(N);
		for (int i=0;i<N; i++) {
			cin>>vx[i]>>vl[i];
		}
		cin>>D;
		cerr<<N<<" vines D="<<D<<endl;

		set<pair<int,int> > vis;
		queue<pair<int,int> > q;
		q.push(make_pair(0,0));
		bool ans=false;
		while (!ans && q.size()) {
			pair<int,int> st=q.front();
			q.pop();
			int x=st.first;
			int vine=st.second;
			cerr<<"I AM AT "<<x<<" GRABBING VINE "<<vine<<endl;
			int limit = vx[vine] + min(vl[vine], vx[vine]-x);
			if (limit >= D) {
				cerr<<"From x="<<x<<" vine "<<vine<<endl;
				ans=true;
			} else {
				int ix=vine+1;
				while (ix<N && vx[ix]<=limit) {
					int newx = vx[vine];
					cerr<<" from "<<vine<<" can grab vine "<<ix<<" at x="<<newx<<endl;
					if (vx[ix]-vl[ix]>newx) {
						newx = vx[ix]-vl[ix];
						cerr<<" ... and clib up, x="<<newx<<endl;
					}
					pair<int,int> newst = make_pair(newx, ix);
					if (vis.find(newst)==vis.end()) {
						cerr<<"push("<<newx<<","<<ix<<")"<<endl;
						q.push(newst);
						vis.insert(newst);
					}
					ix++;
				}
			}
		}
		cout << "Case #" << t << ": " << (ans?"YES":"NO") << endl;
	}


}