#include <iostream>
#include <algorithm>
#include <vector>
#define  rep(i,a,b) for(int i=a; i<=b; i++)

using namespace std ;
vector <long> a; 
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	long c;
	long n; 

	long t; 
	long  s;
	long x, y ; 
	cin >> c; 
	
	rep(k,1,c){
		cin >> n; 
		
		a.clear();
		a.resize(n+1);
		rep(i,1,n){	cin >> a[i]; }
		sort(a.begin(),a.end()); 
		t = a[1];
		x = 0;
		y = 1; 
		rep(i,2,n){
			s=a[
				i];
			x=0;
			y=1; 
			while (t>0||s>0) {
				x += y*((t%2+s%2)%2);
				y *=2; 
				t=t/2;
				s=s/2; 
			}
			t = x; 
		}

		if (t!=0) cout << "Case #" << k << ": " << "NO" << endl; 
		else {
			x = 0;
			rep(i,2,n){x += a[i]; }
			cout << "Case #" << k << ": " << x << endl; 
		}

	}	

	return 0; 
}