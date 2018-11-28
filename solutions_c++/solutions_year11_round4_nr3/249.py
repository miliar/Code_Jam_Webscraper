#include<iostream>
#include<string>
#include<vector>
#include<utility>
#include<algorithm>

using namespace std;

typedef long long ll;

ll gcd(ll a,ll b){
	return a ? gcd(b%a,a) : b;
}

vector<ll> p;
int a[1000100];

int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	cin >> T;
	for(ll i=2;i<1000010;i++){
		if(a[i]==0){
			p.push_back(i);
			//cerr << i << endl;
			for(ll j=i*i;j<1000010;j+=i){
				a[j]=1;
			}
		}
	}
	for(int q=0;q<T;q++){
		cout << "Case #" << q+1 << ": ";
		ll n;
		cin >> n;
		ll s=0;
		for(int i=0;i<p.size() && p[i]*p[i]<=n;i++){
			ll k=n;
			ll t=0;
			while(k>=p[i]){
				t++;
				k/=p[i];
			}
			s+=t-1;
		}
		cout << s+1-(n==1) << endl;
	}
	return 0;
}