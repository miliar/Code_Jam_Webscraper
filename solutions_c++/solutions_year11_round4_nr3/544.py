#include <iostream>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <string>
using namespace std;
typedef unsigned __int64 ll;
const int N=1100;
int T;
ll gcd (ll a, ll b) {
	if (!b) return a;
	else return gcd (b,a%b);
}
ll lcm (ll a, ll b) {
	return (a*b)/gcd(a,b);
}
int main () {
#ifndef ONLINE_JUDGE
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
#endif
	cin>>T;
	for (int test=0; test<T; test++) {
			int n;
			cin>>n;
			int nok=1,maxi=1,mini=0,tmp;
			for (int i=2; i<=n; i++)  {
				int bad=0;
				for (int j=2; j*j<=i; j++) 
					if (i%j==0) bad=1;
				if (!bad) {
					int curn=i;
					while (curn<=n) {
						maxi++;
						curn*=i;
					}
					mini++;
				}
			}
			if (!mini) mini=1;
			printf("Case #%d: %d\n",test+1,maxi-mini);
	}
}