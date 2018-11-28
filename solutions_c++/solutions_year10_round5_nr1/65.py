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

ll power(ll a,ll b,ll p)
{
	ll res=1,x=a;
	while (b){
		if (b%2)res=(res*x)%p;
		b/=2;
		x=(x*x)%p;
	}
	return res;
}

bool w[1000001];

int main()
{
	memset(w,true,sizeof(w));
	vector <int> pr;
	for (int i=2;i<=1000000;i++){
		if (w[i]){
			for (int j=i+i;j<=1000000;j+=i)w[j]=false;
			pr.push_back(i);
		}
	}
	int T;
	cin >> T;
	for (int I=0;I<T;I++){
		int d,k;
		cin >> d >> k;
		ll a[11],amax=-1;
		for (int i=0;i<k;i++){
			cin >> a[i];
			//cerr << a[i] << ' ';
			amax=max(amax,a[i]);
		}//cerr << endl;
		ll next=-1;
		if (k==1){
			cout << "Case #" << I+1 << ": I don't know.\n"; 
			continue;
		}
		if (k==2){
			if (a[1]==a[0])cout << "Case #" << I+1 << ": " << a[0] << endl;else {
				cout << "Case #" << I+1 << ": I don't know.\n";
			}
			continue;
		}
		int D=1;
		for (int i=0;i<d;i++)D*=10;
		for (int i=0;i<(int)pr.size();i++)if (pr[i]>amax){
			ll p=pr[i];
			if (p>=D)break;
			if ((a[0]-a[1]+p)%p!=0){
				ll A=((a[1]-a[2]+p)%p*power((a[0]-a[1]+p)%p,p-2,p))%p;
				ll B=((a[1]-A*a[0])%p+p)%p;
				ll C=(a[k-1]*A+B)%p;
				bool kpyto=true;
				for (int j=1;j<k;j++){
					if (a[j]!=(a[j-1]*A+B)%p){
						kpyto=false;
						break;
					}
				}
				if (kpyto){
					if (next==-1||next==C)next=C; else {
						cout << "Case #" << I+1 << ": I don't know.\n";
						next=-1;
						break;
					}
				}
			} else {
				if (next>=0&&next!=a[0]) {
					cout << "Case #" << I+1 << ": I don't know.\n";
					next=-1;
					break;
				} else next=a[0];
			}
		}
		if (next>=0){
			cout << "Case #" << I+1 << ": " << next << endl;
		}
	}
	return 0;
}
