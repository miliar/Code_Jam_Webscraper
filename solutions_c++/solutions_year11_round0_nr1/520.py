#include "mylib.h"
int abs(int x)
{
	if(x>=0)return x;
	else return -x;
}
//#define SMALL
#define LARGE
int main() {
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		int N;cin>>N;
		int sa=1,sb=1;
		int ta=0,tb=0;
		int curtime=0;
		for(int i=0;i<N;i++){
			char robot;
			int button;
			cin>>robot>>button;
			if(robot=='O'){
				curtime=(curtime-ta>=abs(button-sa)?0:abs(button-sa)+ta-curtime)+curtime+1;
				ta=curtime;
				sa=button;
			}
			else {
				curtime=(curtime-tb>=abs(button-sb)?0:abs(button-sb)+tb-curtime)+curtime+1;
				tb=curtime;
				sb=button;
			}
		}
		cout<<"Case #"<<t<<": "<<curtime<<endl;
	}
	return 0;
}
