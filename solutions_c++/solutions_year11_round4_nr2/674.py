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

const double EPS=1e-9;

bool eq(double a,double b) {
	return (abs(a-b)<EPS);
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t; cin >> t;
	for (int kk=0;kk<t;kk++) {
		int n,m,d;
		cin >> n >> m >> d;
		vector<string> s(n);
		for (int i=0;i<n;i++)
			cin >> s[i];
		vector<vector<int> > a (n,vector<int>(m,0));
		vector<vector<pair<double,double> > > z (n,vector<pair<double,double> > (m));
		for (int i=0;i<n;i++) {
			for (int j=0;j<m;j++) {
				a[i][j]=d+(s[i][j]-'0');
				z[i][j].first=(double)(j+0.5)*(double)(a[i][j]);
				z[i][j].second=(double)(i+0.5)*(double)(a[i][j]);
			}
		}
		bool find=false;
		int K;
		for (K=(min(n,m));K>=3;K--) {
			for (int i=0;i<n;i++)
				for (int j=0;j<m;j++)
					if (i+K-1<n && j+K-1<m) {
						double resX=0.0;
						double resY=0.0;
						double mass=0.0;
						for (int ii=i;ii<=i+K-1;ii++)
							for (int jj=j;jj<=j+K-1;jj++) {
								if (ii==i && jj==j) continue;
								if (ii==i+K-1 && jj==j) continue;
								if (ii==i+K-1 && jj==j+K-1) continue;
								if (ii==i && jj==j+K-1) continue;
								resX+=z[ii][jj].first;
								resY+=z[ii][jj].second;
								mass+=a[ii][jj];
							}
						resX/=mass;
						resY/=mass;
						double cX=0.0;
						double cY=0.0;
						if (K%2==0) {
							cY=i+K/2;
							cX=j+K/2;
						} else {
							int zi=i+K/2;
							int zj=j+K/2;
							cY=zi+0.5;
							cX=zj+0.5;
						}
						if (eq(resX,cX) && eq(resY,cY))
							find=true;
					}
			if (find) break;
		}
		printf("Case #%d: ",kk+1);
		if (find) printf("%d\n",K);
		else printf("IMPOSSIBLE\n");
	}

	return 0;
}
