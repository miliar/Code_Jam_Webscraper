#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

struct WS{
	int b,e,v;
	friend bool operator< (const WS& x,const WS& y){
		return x.b<y.b;
	}
}ws[1005];

bool cmp(const WS& x,const WS& y){
	return x.v<y.v;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("Al.out","w",stdout);
	
	int T,cas=0;
	scanf("%d",&T);
	while(T--){
		int x,s,r,t,n;
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		for(int i=1;i<=n;i++){
			scanf("%d%d%d",&ws[i].b,&ws[i].e,&ws[i].v);
		}
		sort(ws+1,ws+n+1);
		int len=0,ss=0;
		for(int i=1;i<=n;i++){
			if(ss<ws[i].b){
				len+=(ws[i].b-ss);
			}
			ss=ws[i].e;
		}
		len+=x-ss;
		ws[0].b=0;
		ws[0].e=len;
		ws[0].v=0;
		sort(ws,ws+n+1,cmp);
		
		printf("Case #%d: ",++cas);
		double ttt=t;
		double time=0;
		for(int i=0;i<=n;i++){
			double tlen=ws[i].e-ws[i].b;
			if(ttt>0){
				if(ttt*(ws[i].v+r)>=tlen){
					time+=tlen/(ws[i].v+r);
					ttt-=tlen/(ws[i].v+r);
				}else{
					tlen-=ttt*(ws[i].v+r);
					time+=ttt;
					ttt=0;
					time+=tlen/(ws[i].v+s);
				}
			}else{
				time+=tlen/(ws[i].v+s);
			}
		}
		
		printf("%lf\n",time);
	}
}