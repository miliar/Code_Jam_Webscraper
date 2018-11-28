#include<iostream>
using namespace std;
#include<algorithm>
#include<math.h>

struct way{
	int v;
	double len;
	bool operator <(const way &wy) const{
		return v<wy.v;
	}
};

int main(){
	int i,j,k,m,n,r,c,x,walk,run,st,ed,len;
	double trun,t,ans;
	way wy[1003];
	cout.setf(ios::fixed);
	cout.precision(9);
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	cin>>r;
	for(c=1;c<=r;c++){
		cin>>x>>walk>>run>>trun>>n;
		cin>>st>>ed;
		len=st;
		wy[0].len=ed-st;
		cin>>wy[0].v;
		for(i=1;i<n;i++){
			cin>>st;
			len=len+st-ed;
			cin>>ed>>wy[i].v;
			wy[i].len=ed-st;
		}
		wy[n].len=len+x-ed;
		wy[n].v=0;
		n++;
		sort(wy,wy+n);
		ans=0;
		for(i=0;i<n;i++){
			if(trun>0){
				t=wy[i].len/(wy[i].v+run);
				if(t<=trun){
					trun-=t;
					ans+=t;
				}
				else{
					ans=ans+trun+(wy[i].len-(wy[i].v+run)*trun)/(wy[i].v+walk);
					trun=0;
				}
			}
			else
				ans=ans+wy[i].len/(wy[i].v+walk);
		}
		cout<<"Case #"<<c<<": "<<ans<<endl;

	}
}