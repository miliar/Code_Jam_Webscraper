#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<cmath>
using namespace std;

#define F(i,n) for(i=0;i<n;i++)
#define FF(i,n) for(i=1;i<=n;i++)

struct node{
	int L, v;
	bool operator<(const node&B)const{
		return v<B.v;
	}
}a[1010];

int X, S, R, n;
double t;

int main(){
     int i, j, T, TT=1, sum;
     freopen("A-large.in","r", stdin);
     freopen("A.out", "w", stdout);
     scanf("%d",&T);
     while(T--){
		scanf("%d%d%d%lf%d",&X,&S,&R,&t,&n);
		sum  = 0;
		F(i,n){
			int fr, to, v;
			scanf("%d%d%d",&fr,&to,&v);
			a[i].L = to - fr;
			a[i].v = v + S;
			sum += a[i].L;
		}
		a[n].L = X - sum;
		a[n].v = S;
		n++;
		sort(a, a+n);
		double ans = 0.0;
		R -= S;
		F(i,n){
//			cout<<a[i].L<<endl;
			double tmp  = (double)a[i].L/(a[i].v+R);
			if(tmp<t){
				ans += tmp;
				t -= tmp;
			}
			else {
				ans += t + (a[i].L-(a[i].v+R)*t)/a[i].v;
				t = 0.0;
			}
		}
		printf("Case #%d: %.10lf\n", TT++, ans);
	}
     
     return 0;
}
