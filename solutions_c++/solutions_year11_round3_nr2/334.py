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


#define mx 1100000
i64 a[mx],tm[mx];


int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	i64 i,j,k,I,T,l,m,tl,n;
	i64 t,sm,r1,r2;
	cin>>T;
	for(I=1;I<=T;I++) {
		cin>>l>>t>>n>>k;
		for(i=0;i<k;i++) {
			cin>>a[i];
			for(j=k+i;j<=n;j+=k) a[j]=a[i];
		}
		//for(i=0;i<=n;i++) cout<<a[i]<<'\n';
		
		sm=0;
		for(i=0;i<n && (sm+(a[i]<<1))<t;i++) {
			sm+=(a[i]<<1);
		}
		j=i;
		//cout<<sm<<' '<<j<<'\n';
		if(j<n) {
		m=0;
		r1=a[i]<<1;
		for(i++;i<n;i++) tm[m++]=a[i];
		sort(tm,tm+m,greater < i64 >());
		tl=l;
		for(i=0;i<m;i++) {
			if(tl>0) {
				tl--;
				r1+=tm[i];
			}
			else r1+=(tm[i]<<1);
		}
		//cout<<r1<<'\n';
		if(!((t-sm)&1) && l){
			m=0;
			r2=(t-sm)+(a[j]-((t-sm)>>1));
			//cout<<r2<<'\n';
			for(i=j+1;i<n;i++) tm[m++]=a[i];
			sort(tm,tm+m,greater < i64 >());
			tl=l-1;
			for(i=0;i<m;i++) {
				if(tl>0) {
					tl--;
					r2+=tm[i];
				}
				else r2+=(tm[i]<<1);
			}
			r1=min(r1,r2);
		}}
		else {
			r1=0;
		}
		
		printf("Case #%Ld: %lld\n",I,sm+r1);
	}
	return 0;
}

