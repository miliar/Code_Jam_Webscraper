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
	for (int z=0;z<t;z++) {
		int n; cin >> n;
		vector<string> a;
		vector<double> res(n,0.0);
		vector<vector<double> > wp(n,vector<double>(n,0.0));
		vector<double> owp(n,0.0);
		vector<double> oowp(n,0.0);
		for (int i=0;i<n;i++) {
			string str; cin >> str; a.push_back(str);
		}
		for (int i=0;i<n;i++) {
			for (int k=0;k<n;k++) {
				int all=0,win=0;
				for (int j=0;j<n;j++) {
					if (j==k) continue;
					if (a[i][j]=='0') {all++;}
					if (a[i][j]=='1') {all++; win++;}
				}
				wp[i][k]=(double)win/(double)all;
			}
		}
		for (int i=0;i<n;i++) {
			int all=0; double cur=0.0;
			for (int j=0;j<n;j++) {
				if (a[i][j]=='0' || a[i][j]=='1') {
					all++;
					cur+=wp[j][i];
				}
			}
			owp[i]=(double)cur/(double)all;
		}
		for (int i=0;i<n;i++) {
			int all=0; double cur=0.0;
			for (int j=0;j<n;j++) {
				if (a[i][j]=='0' || a[i][j]=='1') {
					all++;
					cur+=owp[j];
				}
			}
			oowp[i]=(double)cur/(double)all;
		}

		printf("Case #%d:\n",z+1);
		for (int i=0;i<n;i++) {
			printf("%.6f\n",wp[i][i]*0.25+owp[i]*0.5+oowp[i]*0.25);
		}
	}
	return 0;
}
