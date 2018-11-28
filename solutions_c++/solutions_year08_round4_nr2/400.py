#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <utility>
#include <algorithm>

using namespace std;

long long x[3000],y[3000],as;

int main(){
	int t;
	long long n,m,a,res;
	long long ta,xa=0,ya=0,xb,yb;
	bool ok;
	cin>>t;
	//scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		res=0;
		cin>>n>>m>>a;
		as=0;ok=true;
		for(int tx=0;tx<=n;tx++)
		for(int ty=0;ty<=m;ty++){
			x[as]=tx;y[as++]=ty;
		}
		for(int i=0;i<as&&ok;i++)
		for(int j=i+1;j<as&&ok;j++){
			ta=xa*(y[i]-y[j])+x[i]*(y[j]-ya)+x[j]*(ya-y[i]);
			if(ta<0)ta=-ta;
			if(ta==a){
				//cout<<ta<<endl;
				ok=false;
				xb=max(x[i],x[j]);
				yb=max(y[i],y[j]);
				res+=(n-xb+1)*(m-yb+1);
				cout<<"Case #"<<tc<<": "<<xa<<" "<<ya<<" "<<x[i]<<" "<<y[i]<<" "<<x[j]<<" "<<y[j]<<endl;
			}
		}
		if(ok)cout<<"Case #"<<tc<<": IMPOSSIBLE"<<endl;
		//printf("Case #%d: %d\n",tc,res);
		//cout<<"Case #"<<tc<<": "<<res<<endl;
	}
	return 0;
}


