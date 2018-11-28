#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;
int C, D, P, V, N;
vector<int> vendor;
int f(double ans) {
	int i;
	double pos = vendor[0] - ans;
	for(i=1;i<N;i++) {
		if(vendor[i] >= pos+D) pos = (vendor[i]-ans<pos+D)?pos+D:vendor[i]-ans;
		else {
			if(vendor[i]+ans<pos+D)return 0;
			else pos = pos+D;			
		}
	}
	return 1;
}
int main() {
	int i, j, T, t;
	freopen("google.in","r",stdin);
	freopen("google.out","w",stdout);
	scanf("%d", &T);
	for(t=0;t<T;t++) {
		scanf("%d %d", &C, &D);
		vendor.clear();
		for(i=0;i<C;i++){
			scanf("%d %d", &P, &V);
			for(j=0;j<V;j++)vendor.push_back(P);
		}
		N = vendor.size();
		double st = 0 , en = 1e15, md;
		for(i=0;i<100;i++) {
			md = (st+en)/2;
			if(f(md)==1)en = md;
			else st = md;
		}
		printf("Case #%d: %lf\n",t+1,md);
	}
	return 0;	
}
