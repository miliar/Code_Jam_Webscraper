#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;

bool c[1200000];
struct aa{
	double l,r,s;
} a[10011];
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;
	cin >>t;

		long long ttt=1100000;
			for (int i=2;i<=ttt;i++) if (!c[i]) {
			//	cout <<i<<endl;
				for (int j=2;j<=ttt;j++) {
					if (i*j>ttt) break;
					c[i*j]=true;			
				}			
			}	
		
	
	for (int tt=1;tt<=t;tt++){
			long long n;
			cin >>n;
			long long maxx,minn;
			maxx=0;
			minn=0;
			long long ans=0;
			int tttt=int (sqrt(n));
			for (long long i=2;i<=tttt;i++) if (!c[i]){
		
				ans--;
				int oo=1;
				long long tmp=i;
				while (tmp<=n) {tmp*=i;ans++;}
			}
		
		cout <<"Case #"<<tt<<": ";
		if (n==1) cout <<'0'<<endl; else
		printf("%d\n",ans+1);
	}


}
