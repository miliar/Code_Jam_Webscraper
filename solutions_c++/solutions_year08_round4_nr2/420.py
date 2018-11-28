#include <iostream>
using namespace std;


int main(){
	int t,u,a,n,m,x2,y3,x3,y2,ok;
	cin>>t;
	for (u=0; u<t; u++){
		cin>>n>>m>>a;
		ok=0;
		for (x3=1; x3<=n && !ok; x3++){
			for (x2=1; x2<=n && !ok; x2++){
				for (y3=0; y3<=m && !ok; y3++){
					y2=(x2*y3+a)/x3;
					if ((x2*y3+a)%x3==0 && y2>=0 && y2<=m){
						ok=1;
						break;
					}
				}
				if (ok) break;
			}
			if (ok) break;
		}
		if (ok) cout<<"Case #"<<(u+1)<<": 0 0 "<<x2<<" "<<y2<<" "<<x3<<" "<<y3<<endl;
		else cout<<"Case #"<<(u+1)<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}
