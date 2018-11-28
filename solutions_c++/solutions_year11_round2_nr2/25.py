#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>

using namespace std;

int n,d;
pair<int,int> p[1111];

int check(double mid){
	double last = -1e30;
	for(int i=0;i<n;i++){
		for(int j=0;j<p[i].second;j++){
			if(last+d>p[i].first+mid)
				return 0;
			last=max(last+d,p[i].first-mid);
		}
	}
	return 1;
}

int main(){
	int t;
	scanf("%d", &t);
	for(int c=0;c<t;c++){
		cerr << c << endl;
		scanf("%d%d",&n,&d);
		for(int i=0;i<n;i++)
			scanf("%d%d",&p[i].first,&p[i].second);
		sort(p,p+n);
		double lo=0;
		double hi=1e18;
		for(int k=0;k<100;k++){
			double mid=(lo+hi)/2.0;
			if(check(mid))
				hi=mid;
			else
				lo=mid;
		}
		printf("Case #%d: %.2lf\n", c+1,hi);
	}
	return 0;
}
