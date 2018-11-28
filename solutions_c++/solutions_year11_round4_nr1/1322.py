#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

struct node{
	int s,e,v;
}way[3000];

bool  cmp1(node a,node b){
	if(a.s < b.s) return 1;
	return 0; 
}
bool cmp2(node a, node b){
	return a.v < b.v;
}
int main(){
	int T,X,S,R,N,wayN;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	double t;
	scanf("%d",&T);
	for(int Cas = 1; Cas <= T ; Cas ++){
		wayN = 0;
		scanf("%d %d %d %lf %d",&X,&S,&R,&t,&N);
		
		for(int i = 0; i < N; i ++){
			scanf("%d %d %d",&way[wayN].s,&way[wayN].e,&way[wayN].v);
			wayN ++;
		}
		
		
		sort(way,way+wayN,cmp1);
		
	
		int s = 0;
		int n = wayN;
		for(int i = 0; i < n; i ++){
			if(s <= way[i].s) {
				way[wayN].s = s;
				way[wayN].e = way[i].s;
				way[wayN++].v = 0;
				s=way[i].e;
			}
		}
		if(s != X){
			way[wayN].s = s;
			way[wayN].e = X;
			way[wayN++].v = 0;
		}
		
		sort(way,way + wayN ,cmp2);
		double tot = 0;
		for(int i = 0; i < wayN ; i ++){
			double a;
			if(t > 0) {
				if((way[i].v + R) * t >= (way[i].e - way[i].s)){
					a = (way[i].e - way[i].s)*1.0/(way[i].v + R);
					tot += a;
					t -= a;
				}else{
					a = (way[i].e - way[i].s - (way[i].v + R) * t) / (way[i].v+S);
					tot += t;
					tot += a;
					t = 0;
				}
			}
			else {
				a = (way[i].e - way[i].s) * 1.0/ (way[i].v + S);
				tot += a;
			}
		}
		printf("Case #%d: %.6lf\n",Cas,tot);
	}
	return 0;
}
