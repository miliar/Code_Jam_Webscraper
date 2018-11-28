#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;
double x[5],y[5],r[5];

int main() {
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int t; cin>>t;
	cout.precision(6);
	for (int o=0; o<t; o++) {
		int n; cin>>n;
		double res = 0;
		for (int i=0; i<n; i++) {
			cin>>x[i]>>y[i]>>r[i];
			if (r[i]>res)
				res = r[i];
		}
		double rr = 1e10;
		for (int i=0; i<n; i++)
			for (int j=i+1; j<n; j++) { 
				//for (int k=0; k<n; k++){
					double p = (hypot(y[j]-y[i],x[j]-x[i])+r[i]+r[j])/2.;
					if (p<rr) rr = p;
				}
		if (n>2)
		res = max(res,rr);
		cout<<"Case #"<<o+1<<": "<<fixed<<res<<endl;
	}
	return 0;
}