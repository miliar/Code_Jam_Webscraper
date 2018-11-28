#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int C,N,M,A;
int p,q,r,s;
int px1,px2,px3,py1,py2,py3;

int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	cin>>C;
	for(int time=0;time<C;++time){
		cin>>N>>M>>A;
		bool find=false;
		for(p=-M;p<=M;++p){
			for(q=-M;q<=M;++q){
				for(r=-N;r<=N;++r){
					for(s=-N;s<=N;++s){
						if(p*r+q*s!=A) continue;
						int lower=max(max(-r,-s),0);
						int upper=min(min(N-r,N-s),N);
						if(lower<=upper){
							px3=lower;
							px1=px3+r;
							px2=px3+s;
							lower=max(max(-p,q),0);
							upper=min(min(M-p,M+q),M);
							if(lower<=upper){
								py3=lower;
								py1=py3-q;
								py2=py3+p;
								find=true;
								break;
							}
						}
					}
					if(find) break;
				}
				if(find) break;
			}
			if(find) break;
		}
		cout<<"Case #"<<time+1<<":";
		if(find){
			cout<<' '<<px1<<' '<<py1<<' '<<px2<<' '<<py2<<' '<<px3<<' '<<py3<<endl;
		}else cout<<" IMPOSSIBLE"<<endl;
	}
	return 0;
}
