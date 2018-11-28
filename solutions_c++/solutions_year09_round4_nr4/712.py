#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int N;
int x[40];
int y[40];
int r[40];
double best;
double temp;

typedef vector<int> VI;

void plants(long long mask) {
	if(mask==((1<<N)-1)) {
		best=min(best,temp);
		return;
	}
	for (int i=0;i<N;++i) if (!(mask&(1<<i))) {
		for (int j=i;j<N;++j) if (!(mask&(1<<j))) {
			long long mask2=mask;
			double xx=(x[i]+x[j])/2.;
			double yy=(y[i]+y[j])/2.;
			double uvectx=x[j]-x[i];
			double uvecty=y[j]-y[i];
			double uvectnorm=sqrt(uvectx*uvectx+uvecty*uvecty);
			uvectx/=(2*uvectnorm);
			uvecty/=(2*uvectnorm);
			xx-=r[i]*uvectx;
			yy-=r[i]*uvecty;
			xx+=r[j]*uvectx;
			yy+=r[j]*uvecty;
			double rr=(uvectnorm+r[i]+r[j])/2.;
			if (rr>=best) continue;
			mask2|=(1<<i);
			mask2|=(1<<j);
			for (int k=0;k<N;++k) if (!(mask2&(1<<k))) {
				double xxx=xx-x[k];
				double yyy=yy-y[k];
				if (sqrt(xxx*xxx+yyy*yyy)+r[k]<=rr) mask2|=(1<<k);
			}
			if (mask==0) {
				temp=rr;
				plants(mask2);
			}
			else {
				if(mask2==((1<<N)-1)) {
					best=min(best,max(temp,rr));
				}
			}
		}
	}
}

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;++t) {
		cin >> N;
		for (int i=0;i<N;++i) {
			cin >> x[i] >> y[i] >> r[i];
		}
		best=1E10;
		cout.precision(10);
		plants(0);
		cout << "Case #" << t << ": " << best << endl;
	}
}

