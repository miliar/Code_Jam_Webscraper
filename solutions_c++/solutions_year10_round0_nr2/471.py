#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#define LL long long 

using namespace std;
string ANS[2];

LL gcd(LL  a, LL b){
	if(a<b) {
		a=a+b;
		b=a-b;
		a=a-b;	
	}	
	if(b==0) return a;
	return gcd(a%b, b);
}

int T, n;
LL ans;
LL k;
LL a[3], t[4];
int main(){
	freopen("b.in", "r",stdin);	
	freopen("b.txt", "w",stdout);
	cin>>T;
	int i;
	for(int L=1; L<=T; ++L){
		cin>>n;
		for(i=0; i<n; ++i) cin>>t[i];
		sort(t, t+n);
		switch (n) {
			case 2:
				a[0]=t[1]-t[0];
				ans= t[1]%a[0];
				if (ans!=0) ans=a[0]-ans;
				break;
			case 3:
				a[0]=t[1]-t[0];
				a[1]=t[2]-t[1];
				a[0]=gcd(a[0], a[1]);
				ans= t[1]%a[0];
				if (ans!=0) ans=a[0]-ans;					
		}
		
	
	
	
	
		cout<<"Case #"<<L<<": "<<ans<<endl;
	}	
}
