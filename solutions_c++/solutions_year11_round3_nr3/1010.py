#include <iostream>
using namespace std;

#define forn(i, n) for(int i=0; i<(int)n; i++)

int a[105];
int n;

bool ok(int num){
	bool ans=true;
	
	forn(i, n){
		if(a[i]%num!=0 && num%a[i]!=0) {ans=false; break;}
	}

	return ans;
}
int main(){
	int T;
	int h, l;

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	
	cin>>T;
	forn(q, T){
		cout<<"Case #"<<q+1<<": ";
		
		cin>>n>>l>>h;

		forn(i, n) cin>>a[i];
		
		int num=l;
		bool b=false;
		for(; num<=h; num++){
			if(ok(num)) {b=true; break;}
		}

		if(b) cout<<num<<endl;
		else cout<<"NO"<<endl;
	}

	return 0;
}