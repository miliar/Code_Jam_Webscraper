#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <list>
#include <stack>
#include <utility>
#include <cstdlib>
#include <sstream>
#include <fcntl.h>

#include <cmath>
using namespace std;

const int INF=0x7fffffff;

int x[100];
int y[100];
int r[100];

double f1(int i) {
	return double(r[i]);
}
double f2(int i,int j) {
	return (sqrt(double((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]))) + r[i] + r[j]) / 2.0;
}
double f3(int i,int j,int k) {
	double ret = max(f1(i) , f2(j,k));
	ret = min(ret,max(f1(j),f2(i,k)));
	ret = min(ret,max(f1(k),f2(i,j)));
	return ret;
}

int main(int argc,char**argv) {
	int cs;
	scanf("%d",&cs);

	for (int csi=1; csi<=cs; ++csi) {

		int n;
		scanf("%d",&n); 
		for (int i=0; i<n; ++i) {
			scanf("%d%d%d",x+i,y+i,r+i);
		}
		double ret;
		switch (n) {
			case 1:
				ret = f1(0);
				break;
			case 2: ret = max(f1(0),f1(1));
				break;
			case 3: ret = f3(0,1,2);
				break;
			default: ret = -1;
		}
		printf("Case #%d: %.8lf\n",csi,ret );
	}

	return 0;
}
