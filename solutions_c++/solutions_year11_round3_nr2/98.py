#include <iostream>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <string>
using namespace std;
typedef __int64 ll;
const int N=1100000;
ll tests,t,r,c;
ll n,l,a[N],isl[N];
int main () {
#ifndef ONLINE_JUDGE
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
#endif
	cin>>tests;
	for (int numt=1; numt<=tests; numt++) {
		cin>>l>>t>>n>>c;
		for (int i=0; i<c; i++) {
			ll tmp=0;
			cin>>tmp;
			tmp*=2;
			for (int j=0; j*c+i+1<=n; j++) a[j*c+i]=tmp; 
		}
		ll sum=0;
		for (int i=0; i<n; i++) sum+=a[i];
		cout<<"Case #"<<numt<<": ";
		ll st=0,curt=0,cur=0;
		for (int i=0; i<n; i++)
			if (curt+a[i]<t) curt+=a[i];
			else {
				a[i]-=(t-curt);
				curt=t;
				for (int i=0; i<=n; i++) a[i]*=-1;
				sort(a+i,a+n);
				for (int i=0; i<=n; i++) a[i]*=-1;
				for (int col=1; col<=l; col++) 
					if (i+col-1<n) a[i+col-1]/=2;
				for (int j=i; j<n; j++) curt+=a[j];
				break;
			}
		cout<<curt<<endl;
	}
}