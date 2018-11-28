#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int i,j,k,l,m,n,t,tt,ttt;
int ww[105];
int w,x,s,r,a,b,sum,ss;

int main(){
	freopen("c:\\A-large.in","r",stdin);
	freopen("c:\\output.txt","w",stdout);
	
	cin>>ttt;
	while(ttt--){
		tt++;
		cout<<"Case #"<<tt<<": ";
		cin>>x>>ss>>r>>t>>n;
		sum=0;
		for (i=0;i<101;i++)
			ww[i]=0;
		for (i=0;i<n;i++){
			cin>>a>>b>>w;
			ww[w]+=b-a;
			sum+=b-a;
		}
		double time=1.0*t;
		double ans=0;
		ww[0]=x-sum;
		for (i=0;i<101;i++)
			if (ww[i]>0){
				double s=ww[i];
				double v=i;
				if (time>=1.0*s/(v+r)){
					ans+=1.0*s/(v+r);
					time-=1.0*s/(v+r);
				} else
				{
					ans+=time;
					s-=time*(v+r);
					ans+=s/(v+ss);
					time=0;
				}
			}
			cout.precision(10);
		cout<<fixed<<ans<<endl;
	}
	return 0;
}