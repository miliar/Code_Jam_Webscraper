#include <stdio.h>
#include <algorithm>
using namespace std;

int scan(){
	int h,m;
	scanf("%d:%d",&h,&m);
	return h*60+m;
}

int cal(int np,int nq,int t,int q[],int p[]){
	int i,j,r=np;
	sort(q,q+nq);
	sort(p,p+np);
	for(i=j=0; i<nq; i++){
		while(j<np&&q[i]+t>p[j]) j++;
		if(j<np){
			r--;
			j++;
		}
	}
	return r;
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("b.txt","w",stdout); 
	const int size=100;
	int nc,c;
	int na,nb,t,ap[size],aq[size],bp[size],bq[size];
	scanf("%d",&nc);
	for(c=1; c<=nc; c++){
		scanf("%d%d%d",&t,&na,&nb);
		for(int i=0; i<na; i++){
			ap[i]=scan();
			aq[i]=scan();
		}
		for(int i=0; i<nb; i++){
			bp[i]=scan();
			bq[i]=scan();
		}
		printf("Case #%d: %d %d\n",c,
			   cal(na,nb,t,bq,ap),
			   cal(nb,na,t,aq,bp));
	}
	return 0;
}
