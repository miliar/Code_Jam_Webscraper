#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<map>
#include<cmath>
#include<algorithm>
using namespace std;
int main() {
	int A,B,T,i,j;
	double a,ok,nok,temp;
	vector<double> st,v;
	scanf("%d",&T);
	for(i=0; i<T; i++) {
		scanf("%d%d",&A,&B);
		ok=1;
		for(j=0; j<A; j++) {
			scanf("%lf",&a);
			ok*=a;
			v.push_back(a);
		}
		temp=ok*(B-A+1);
		temp+=(1-ok)*(2*B-A+2);
		st.push_back(temp);
		for(j=A-1; j>=0; j--) {
			ok/=v[j];
			temp=ok*(2*(A-j)+B-A+1);
			temp+=(1-ok)*(A+2*(B-j+1));
			st.push_back(temp);
		}
		st.push_back(B+2);
		sort(st.begin(),st.end());
		printf("Case #%d: %.6lf\n",i+1,st[0]);
		v.clear();
		st.clear();
	}		
	return 0;
}
