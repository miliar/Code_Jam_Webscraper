#include<cstdio>
#include<algorithm>
using namespace std;

int Z;
struct cor{
	int b,e,v;
	void read(){
		scanf("%d%d%d",&b,&e,&v);
	}
}a[3005];

bool cmp1(cor a,cor b){
	return a.b<b.b;
}
bool cmp2(cor a,cor b){
	return a.v<b.v;
}

int X,S,R,t,N;


int main(){
	scanf("%d",&Z);
	for (int z=1;z<=Z;++z){
		scanf("%d%d%d%d%d",&X,&S,&R,&t,&N);
		
		for (int i=0;i<N;++i){
			a[i].read();
		}
		
		sort(a,a+N,cmp1);
		
		for (int i=1;i<N;++i){
			a[N+i-1].b = a[i-1].e;
			a[N+i-1].e = a[i].b;
			a[N+i-1].v = 0;
		}
		
		a[2*N-1].b = 0;
		a[2*N-1].e = a[0].b;
		a[2*N-1].v = 0;
		
		a[2*N].b = a[N-1].e;
		a[2*N].e = X;
		a[2*N].v = 0;
		
		sort(a,a+(2*N+1),cmp2);
		
		double ttt = t;
		double ans = 0;
		
		for (int i=0;i<2*N+1;++i){
			if (ttt>1e-20){
				double tmp = (1.0*a[i].e - a[i].b)/(R+a[i].v);
				if (tmp<=ttt){
					ans += tmp;
					ttt -= tmp;
				}else{
					tmp = ((1.0*a[i].e - a[i].b) - (a[i].v+R)*ttt) / (S+a[i].v);
					ans += tmp + ttt;
					ttt = 0;
				}
			}else{
				double tmp = (1.0*a[i].e - a[i].b)/(S+a[i].v);
				ans += tmp;
			}
		}
		
		
		printf("Case #%d: %.9f\n",z,ans);
	}
	return 0;
}
