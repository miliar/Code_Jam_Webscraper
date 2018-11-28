#include <iostream>

using namespace std;

typedef long long ll;

ll gcd(ll a, ll b){
	return (b==0 ? a : gcd(b, a%b));
}
ll lcm(ll a, ll b){
	return (a/gcd(a,b)) * b;
}
int main(){
	int test;
	cin >> test;
	for (int t=1 ; t<=test ; t++){
		cout << "Case #" << t << ": ";
		ll n, d, g;
		cin >> n >> d >> g;
		if (d==0){
			if (g!=100)
				cout << "Possible" << endl;
			else
				cout << "Broken" << endl;
			continue;
		}
		ll l= lcm(d, 100);
		ll res= l / d;
		if (res>n || (g==100 && d!=100) || (g==0 && d!=0))
			cout << "Broken" << endl;
		else
			cout << "Possible" << endl;
	}
	return 0;
}