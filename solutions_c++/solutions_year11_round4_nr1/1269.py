#include<iostream>
#include<algorithm>
using namespace std;

int x,s,r,t,n;
struct b{
	int sp;
	int len;
} a[1001];

bool cmp(b x,b y){
	return (x.sp+s)*(x.sp+r) < (y.sp+s)*(y.sp+r);
}

int main(){
	int T;
	cin>>T;
	cout.precision(8);
	for(int i=1;i<=T;i++){
		cin>>x>>s>>r>>t>>n;
		int x2=x;
		double ans=0;
		for(int j=0;j<n;j++){
			int b,e,w;
			cin>>b>>e>>w;
			a[j].len=e-b;
			a[j].sp=w;
			x2-=e-b;
			ans+=(e-b)/(double)(w+s);
		}
		a[n].len=x2;
		a[n].sp=0;
		ans+=x2/(double)s;
		sort(a,a+n+1,cmp);
		double t2=t;
		for(int j=0;j<=n;j++){
			double m=a[j].len/(double)(a[j].sp+r);
			if(m>t2)m=t2;
			ans-=m*((double)(a[j].sp+r)/(double)(a[j].sp+s)-1);
			if((t2-=m)<0.0000000001)break;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}

