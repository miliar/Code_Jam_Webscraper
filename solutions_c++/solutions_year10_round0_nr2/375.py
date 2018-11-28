#include<iostream>
#define swap(a,b) (a^=b^=a^=b)
using namespace std;

int in[10],minx;

int gcd(int a,int b){
	if(b<0) b=-b;
	if(a<b) swap(a,b);
	while(b){
		a%=b;
		swap(a,b);
	}
	return a;
}

int main(){
	freopen("pb.out","w",stdout);
	freopen("B-small-attempt0.in","r",stdin);
	int t,tt,n,i,ans;
	cin >> t;
	for(tt=1 ; tt<=t ; tt++){
		cin >> n;
		for(i=0 ; i<n ; i++){
			cin >> in[i];
		}
		minx=in[1]-in[0];
		if(minx<0) minx=-minx;
//		cout << minx << endl;
		for(i=2 ; i<n ; i++){
			minx=gcd(minx,in[i]-in[i-1]);
//			cout << minx << endl;
		}
		ans=minx-(in[0]%minx);
		if(ans==minx) ans=0;
		cout << "Case #" << tt << ": " << ans << endl;
	}
}
