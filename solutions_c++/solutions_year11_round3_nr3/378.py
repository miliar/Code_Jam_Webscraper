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


int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	cin >> T;
	for(int q=0;q<T;q++){
		cout << "Case #" << q+1 << ": ";
		int n,l,r;
		cin >> n >> l >> r;
		vector<ll> c(n);
		for(int i=0;i<n;i++){
			cin >> c[i];
		}
		vector<ll> ans;
		sort(c.begin(),c.end());
		if(l==1){
			cout << "1\n";
			continue;
		}
		ll a=1;
		for(int i=0;i<n && a<=r;i++){
			a=a*c[i]/gcd(a,c[i]);
		}
		int f=0;
		if(a<=r){
			for(int i=l;i<=r;i++){
				if(i%a==0){
					ans.push_back(i);
					break;
				}
			}
		}
		vector<ll> nod(n),nok(n);
		nod[n-1]=c[n-1];
		for(int i=n-2;i>=0;i--){
			nod[i]=gcd(nod[i+1],c[i]);
		}
		if(nod[0]>=l){
			for(int i=l;i<=r;i++){
				if(nod[0]%i==0){
					ans.push_back(i);
					break;
				}
			}
		}
		if(f)continue;
		nok[0]=1;
		for(int i=1;i<n;i++){
			nok[i]=nok[i-1]*c[i-1]/gcd(nok[i-1],c[i-1]);
			if(nok[i]>r){
				nok[i]=-1;
				break;
			}
		}
		f=0;
		for(int i=0;i<n && !f;i++){
			ll a=nok[i];
			ll b=nod[i];
			if(a==-1){
				break;
			}
			if(a>b){
				continue;
			}
			for(int x=l;x<=r;x++){
				if(b%x==0 && x%a==0){
					ans.push_back(x);
					break;
				}
			}
		}

		if(ans.empty()){
			cout << "NO\n";
		}
		else{
			sort(ans.begin(),ans.end());
			cout << ans[0] << endl;
		}
	}
	return 0;
}