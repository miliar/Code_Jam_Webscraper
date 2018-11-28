
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

typedef long long ll;
int main(){
	int nn;scanf("%d",&nn);
	for(int npr=1;npr<=nn;npr++){
		int c,d;scanf("%d%d",&c,&d);
		ll p[c],v[c];
		for(int i=0;i<c;i++)scanf("%lld%lld",p+i,v+i);

		d*=2;
		for(int i=0;i<c;i++)p[i]*=2;

		ll high=1LL<<60,low=0;
		while(high!=low){
			ll mid=(high+low)/2;
			ll pos=-(1LL<<61);
			int ng=0;

			for(int i=0;i<c;i++){
				ll minpos=p[i]-mid;
				ll maxpos=p[i]+mid;
				ll newpos=max(pos+d,minpos);
				pos=newpos+d*(v[i]-1);
				if(maxpos<pos){ng=1;break;}
			}

			//cout<<"mid"<<mid<<" cond"<<(ng?"NG":"OK")<<endl;
			if(ng)low=mid+1;
			else high=mid;
		}

		printf("Case #%d: %lld.%c\n",npr,high/2,(high%2?'5':'0'));
	}
	return 0;
}
