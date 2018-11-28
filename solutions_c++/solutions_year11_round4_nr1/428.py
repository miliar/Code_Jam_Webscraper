
/*Paresh Verma*/
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>
#include<cmath>
#include<list>
#include<map>

#define pub push_back
#define pob pop_back

using namespace std;

typedef struct ll{
	int b,e,s;
}node;

int x,s,r,n;
double t;

bool cmp(node a, node b){
	return a.s<b.s;
}

int main(){
	int i,j,k,l,m,p,T;
	double b,c,d;
	scanf("%d",&T);
	node a[1001];
	for(p=1;p<=T;p++){
		scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
		l=x;
		for(i=0;i<n;i++){
			scanf("%d%d%d",&a[i].b,&a[i].e,&a[i].s);
			l-=a[i].e-a[i].b;
		}
		sort(a,a+n,cmp);
		b=0;
		b=((double)l)/(r);		//b=answer
		if(b<=t){
			t-=b;
			l=0;
		}
		else{
			l-=t*(r);
			b=t;
			t=0;
		}
		b+=((double)l)/s;
		for(i=0;i<n;i++){
			if(t==0){
				b+=((double)(a[i].e-a[i].b))/(a[i].s+s);
			}
			else{
				k=a[i].e-a[i].b;
				c=((double)k)/(r+a[i].s);
				if(c>t){
					b+=t;
					b+=((double)(k-(t*(a[i].s+r))))/(s+a[i].s);	
					t=0;
					
				}
				else{
					b+=c;
					t-=c;
				}
			}
		}
		printf("Case #%d: %.8lf\n",p,b);
	}
	return 0;
}
