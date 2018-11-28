#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;
double p[1000];
int v[1000];
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int ttt;
	cin >>ttt;
	for (int tt=1;tt<=ttt;tt++){
		int c;
		double d;
		cin >>c>>d;
		double maxa=0.;
		double now=-10000000000.;
		double tim=0.;
		for (int i=1;i<=c;i++) {
			cin >>p[i]>>v[i];		
		}
		long long l=0;
		long long r=10000000000000ll;
		while (l<r) {
			long long tmp=(l+r)/2;
			double ans=tmp/2.0;
			double last=-1000000000000000ll;
			bool flag=true;
			for (int i=1;i<=c;i++){ for (int j=1;j<=v[i];j++){
				if (p[i]-ans-d>=last) last=p[i]-ans; else
				if (p[i]+ans>=last+d) last+=d; else
				{	flag=false; break;}
			} if (!flag) break;
			}
			if (flag) r=tmp; else l=tmp+1;
			
			
		}
			
		cout <<"Case #"<<tt<<": ";
		double ans=l/2.0;
		printf("%.1lf",ans);
	//	if ((long long) l/2.==l/2.) cout <<".0"; else cout <<".5";
		cout <<endl;
	}
	
	return 0;
}
