#include "mylib.h"
//#define SMALL
#define LARGE
int main() {
#ifdef SMALL
	freopen("D-small-attempt2.in","rt",stdin);
	freopen("D-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("D-large.in","rt",stdin);
	freopen("D-large.out","wt",stdout);
#endif
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		int N;
		cin>>N;
		double ans=0.0;
		int diff=0;
		int lastmax=-1;
		for(int i=1;i<=N;i++){
			int tmp;
			cin>>tmp;
			lastmax=max(lastmax,tmp);
			diff+=(tmp!=i);
			if(lastmax>0&&lastmax<=i&&diff>0){
				//ans+=2*(i-last-1);
				ans+=min(diff,2*(diff-1));
				lastmax=-1;
				diff=0;
			}
		}
		cout<<"Case #"<<t<<": "<<fixed<<setprecision(6)<<ans<<endl;
	}

	return 0;
}
