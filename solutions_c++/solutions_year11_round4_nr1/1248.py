#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<math.h>
using namespace std;
int MAX=999999999;
double b[20000],e[20000],w[20000],p[20000],k[20000];
int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin>>T;
	for (int q=0; q<T; q++){
		int n;
		double t,c,x,r;
		cin>>x>>c>>r>>t>>n;
		for (int i=0; i<n; i++){
			cin>>b[i]>>e[i]>>w[i];
			p[i]=b[i];
			k[i]=b[i];
		}
		for (int i=0; i<n; i++)
			for (int j=i+1; j<n; j++)
				if (b[j]<b[i]){
					swap(w[i],w[j]);
					swap(e[i],e[j]);
					swap(b[i],b[j]);
				}
		double ans=0;
		double t1=(b[0])/r;
		if (t1<=t){
			t-=t1;
			ans+=t1;
		}else{
			ans+=(b[0]-r*t)/c;
			ans+=t;
			t=0;
		}

		for (int i=1; i<n; i++){
			double t1=(b[i]-e[i-1])/r;
			if (t1<=t){
				t-=t1;
				ans+=t1;
			}else{
				ans+=(b[i]-e[i-1]-r*t)/c;
				ans+=t;
				t=0;
			}
		}
		t1=(x-e[n-1])/r;
		if (t1<=t){
			t-=t1;
			ans+=t1;
		}else{
			ans+=(x-e[n-1]-r*t)/c;
			ans+=t;
			t=0;
		}
		for (int i=0; i<n; i++)
			for (int j=i+1; j<n; j++)
				if (w[j]<w[i]){
					swap(w[i],w[j]);
					swap(e[i],e[j]);
					swap(b[i],b[j]);
				}
		for (int i=0; i<n; i++){
			double t1=(e[i]-b[i])/(w[i]+r);
			if (t1<=t){
				t-=t1;
				ans+=t1;
			}else{
				ans+=(e[i]-b[i]-(r+w[i])*t)/(c+w[i]);
				ans+=t;
				t=0;
			}
		}

		cout<<"Case #"<<q+1<<": ";
		printf("%.7f\n",ans,t);

	}
    return 0;
}