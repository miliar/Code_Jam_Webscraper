#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define sqr(x) ((x)*(x))

using namespace std;

typedef long long ll;
typedef long double ld;

const double pi = acos(-1.0);

int a[1000000],c[1000000];

int gcd(int a,int b)
{
	return b?gcd(b,a%b):a;
}

int main()
{
	int T;
	cin >> T;
	for (int I=0;I<T;I++){
		ll L,n;
		int b[100],d=0;
		cin >> L >> n;
		for (int i=0;i<n;i++){
			cin >> b[i];
			d=gcd(d,b[i]);
		}
		if (L%d!=0){
			cout << "Case #" << I+1 << ": IMPOSSIBLE\n";
			continue;
		}
		for (int i=0;i<n;i++)b[i]/=d;
		L/=d;
		int bl=20000;
		for (int i=1;i<=bl;i++){
			a[i]=c[i]=1000000000;
			for (int j=0;j<n;j++)if (i-b[j]>=0)a[i]=min(a[i],a[i-b[j]]+1);
			c[i]=a[i]-a[i-1];
			//cout << c[i] << endl;
		}
		int p=-1;
		for (int t=1;t<=2000;t++){
			bool kpyto=true;
			for (int i=0;i<5000;i++)if (c[bl-i]!=c[bl-i-t]){
				kpyto=false;
				break;
			}
			if (kpyto) {
				p=t;break;
			}
		}
		//if (p>0)cerr << p << " OK\n"; else cerr << "FAIL\n";
		ll S=a[bl]-a[bl-p];
		cout << "Case #" << I+1 << ": " << (ll)a[(bl-bl%p)+L%p-p]+S*(ll)((L/p)-((bl-bl%p)+L%p-p)/p) << endl;
	}
	return 0;
}
