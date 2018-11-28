#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
const int MaxN=5000;
const double Eps=1e-10;

using namespace std;
struct node{
	int s,t,w;
};
int cmp(node A,node B){
	return A.s<B.s;
}
node p[MaxN],q[MaxN];
int Len,T,S,R,ti,N,tot;
double Ans;
int cmps(node A,node B){
	return A.w<B.w;
}
void work(){
	tot=0;
	R-=S;
	double LeftT=ti;
	if (p[0].s>0){
		q[tot].s=0;
		q[tot].t=p[0].s;
		q[tot].w=0;
		tot++;
	}
	for (int i=0;i+1<N;i++)
	if (p[i].t<p[i+1].s){
		q[tot].s=p[i].t;
		q[tot].t=p[i+1].s;
		q[tot].w=0;
		tot++;
	}
	if (p[N-1].t<Len){
		q[tot].s=p[N-1].t;
		q[tot].t=Len;
		q[tot].w=0;
		tot++;
	}
	for (int i=0;i<tot;i++)
	p[N++]=q[i];
	sort(p,p+N,cmps);
	for (int i=0;i<N;i++){
		double Len=p[i].t-p[i].s;
		double v=S+R+p[i].w;
		double TSR=Len*1.0/v;
//cout << i << " " << Ans << " " << p[i].s << " " << p[i].t << " " << p[i].w << " " << Len << " " << v << " " << TSR << " " << LeftT << endl;
		if (TSR<LeftT+Eps){
			LeftT-=TSR;
			Ans+=TSR;
			continue;
		}else{
			Ans+=LeftT;
			Len-=LeftT*v;
			v=S+p[i].w;
			double Tim=Len/v;
			Ans+=Tim;
			LeftT=0;
		}
	}
}
int main(){
freopen("A.in","r",stdin);
freopen("A.out","w",stdout);
	cin >> T;
	for (int t=1;t<=T;t++){
		printf("Case #%d: ", t);
		scanf("%d %d %d %d %d", &Len, &S, &R, &ti, &N);
		for (int i=0;i<N;i++)
		scanf("%d %d %d", &p[i].s, &p[i].t, &p[i].w);
		sort(p,p+N,cmp);
		Ans=0;
		work();
		printf("%.9lf\n", Ans);
	}
	return 0;
}
