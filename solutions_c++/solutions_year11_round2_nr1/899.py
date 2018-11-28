#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;
	cin >> t;

	for (int z=0;z<t;z++) {
		int n;
		cin >> n;
		vector <string> v;
		vector < pair <int,double> > wp,owp,oowp;
		v.resize(n);
		wp.resize(n,make_pair(0,0));
		owp.resize(n,make_pair(0,0));
		oowp.resize(n,make_pair(0,0));
		vector <double> W,OW,OOW;
		W.resize(n,0);
		OW.resize(n,0);
		OOW.resize(n,0);
		for (int i=0;i<n;i++) {
			cin >> v[i];
			for (int j=0;j<n;j++) {
				if (i!=j && v[i][j]!='.') {
					wp[i].first++;
					wp[i].second+=v[i][j]=='1' ? 1 : 0;
				}
				W[i]=wp[i].first ? wp[i].second/wp[i].first : 0.0;
			}
		}
		for (int i=0;i<n;i++) {
		/*	for (int j=0;j<n;j++) {
				if (i!=j && v[i][j]!='.') {
					owp[i].first++;
					owp[i].second+=v[i][j]=='1' ? 1 : 0;
				}
			}*/
			int gg= 0;
			for (int j=0;j<n;j++) {
				if (i!=j && v[i][j]!='.') {
					for (int k=0;k<n;k++) {
						if (i!=k && v[j][k]!='.') {
							owp[i].first++;
							owp[i].second+=v[j][k]=='1' ? 1 : 0;
						}

					}
					if (owp[i].first) gg++;
					OW[i]+=owp[i].first ? owp[i].second/owp[i].first : 0.0;
					owp[i]=make_pair(0,0);
				}
			}
			if (gg) OW[i]/=gg;
		}
		for (int i=0;i<n;i++) {
			int gg = 0;
			for (int j=0;j<n;j++) {
				if (i!=j && v[i][j]!='.') {
					gg++;
					OOW[i]+=OW[j];
				}
			}
			OOW[i]/=gg;			
		}
		cout << "Case #" << z+1 << ":" << endl; 
		for (int i=0;i<n;i++)
			printf("%.10lf\n",0.25*W[i] + 0.5*OW[i] + 0.25*OOW[i]);
	}
}