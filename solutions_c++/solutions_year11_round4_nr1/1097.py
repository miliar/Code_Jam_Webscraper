#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

struct Line{
	double w,len;
} line[3000];

int n,m,test,cur = 1;
double L,t,S,R,b,e;

bool cmp(const Line &q,const Line &p){
	return q.w<p.w;
}
void init(){
	scanf("%lf%lf%lf%lf%d",&L,&S,&R,&t,&n);
	for ( int i = 0 ; i < n ; i++ ){
		scanf("%lf%lf%lf",&b,&e,&line[i].w);
		line[i].len = (e-b);
		L -= line[i].len;
	}
	line[n].w = 0;
	line[n++].len = L;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	for ( scanf("%d",&test) ; cur <= test ; cur++ ){
		init();
		sort(line,line+n,cmp);
		double tim = t,ans = 0;
		for ( int i = 0 ; i < n ; i++ ){
			if (tim>0){
				if (tim>=(double)line[i].len/(line[i].w+R)){
					ans += (double)line[i].len/(line[i].w+R);
					tim -= line[i].len/(line[i].w+R);
				} else{
					line[i].len -= tim*(line[i].w+R);
					ans += tim+line[i].len/(line[i].w+S);
					tim = -1;
				}
			} else{
				ans += line[i].len/(line[i].w+S);
			}
		}
		printf("Case #%d: %lf\n",cur,ans);
	}
}
