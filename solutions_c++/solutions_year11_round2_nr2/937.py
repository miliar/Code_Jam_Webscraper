//BISMILLAHIRRAHMANIRRAHIM



#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cctype>
#include <climits>
#include <cmath>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define pii pair < int , int >
#define i64 long long
#define CLR(x) memset(x,0,sizeof x)
#define SET(x,y) memset(x,y,sizeof x)


#define mx 1100

int ps[500],vn[500],n,db=0;
double d;

bool chk(double tm) {
	i64 i;
	i64 k,j;
	double lp=INT_MIN;
	for(i=0;i<n;i++) {
		//cout<<i<<' '<<lp<<'\n';
		k=vn[i];
		if(lp<ps[i]) {
			lp=max(lp,ps[i]-tm);
			j=(i64)(floor(((ps[i]-lp)/d)+1e-9)+1e-9)+1;
			//cout<<j<<' '<<lp<<' '<<(ps[i]-lp)<<' '<<((ps[i]-lp)/d)<<'\n';
			if(j>=k) {
				k=0;
				lp+=d*vn[i];//cout<<i<<' '<<k<<' '<<lp<<'\n';
			}
			else {
				lp+=j*d;
				k-=j;
			}
		}
		if(!k) continue;
		if(lp>(ps[i]+tm)) return false;
		j=int(floor((ps[i]+tm-lp)/d+1e-9)+1e-9)+1;
		//cout<<'\t'<<i<<' '<<k<<' '<<lp<<' '<<j<<'\n';
		if(j<k) return false;
		lp+=k*d;
	}
	return true;
}

int main() {
	freopen("B-small-attempt4.in","r",stdin);
	freopen("B-small-attempt4.out","w",stdout);
	int i,j,k,I,T;
	double st,fn,md;
	cin>>T;
	for(I=1;I<=T;I++) {
		cin>>n>>d;
		//cout<<n<<' '<<d<<'\n';
		for(i=0;i<n;i++) {
			cin>>ps[i]>>vn[i];
			//cout<<ps[i]<<' '<<vn[i]<<'\n';
		}
		st=0;
		fn=pow(2,300);
		j=1000;
		//cout<<chk(0)<<'\n';//getchar();
		while(j-- || fabs(st-fn)>1e-9) {
			md=(st+fn)/2;
			//cout<<md<<' '<<chk(md)<<'\n';
			
			if(chk(md)) fn=md;
			else st=md;
		}
		//if(I==7) cout<<st<<' '<<fn<<'\n';
		printf("Case #%d: %.7lf\n",I,(st+fn)/2+1e-9);
	}
	return 0;
}

