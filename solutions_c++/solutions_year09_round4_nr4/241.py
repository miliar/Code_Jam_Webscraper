#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;
struct Node{
	double x,y,r;
}list[3];
int n;
double Cal(Node p,Node q){
	double d=sqrt( (p.x-q.x)*(p.x-q.x) + (p.y-q.y)*(p.y-q.y) );
	return (d+p.r+q.r)/2.0;
}
double solve(){
	double res,p,q;
	double min;
	int i,j,k;
	if(n==1) return list[0].r;
	if(n==2){
		res=list[0].r;
		if(res<list[1].r) res=list[1].r;
		return res;
	}
	min=999999;
	res=list[0].r; 
    p=Cal(list[1],list[2]); 
    q=res>p?res:p; 
    if(q<min)min=q;
	res=list[1].r; 
    p=Cal(list[0],list[2]); 
    q=res>p?res:p; 
    if(q<min)min=q;
	res=list[2].r; 
    p=Cal(list[0],list[1]); 
    q=res>p?res:p; 
    if(q<min)min=q;
	return min;
}
int main(){
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int ca,cas,i;
	cin>>cas;
	for(ca=1; ca<=cas; ca++){
		cin>>n;
		for(i=0;i<n;i++) scanf("%lf%lf%lf",&list[i].x,&list[i].y,&list[i].r);
		printf("Case #%d: %.6lf\n",ca,solve());
	}
	return 0;
}
