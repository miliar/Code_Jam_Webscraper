#include <cstring>
#include <cmath>
#include <iostream>
#include <cstdio>
#include <algorithm>
#define need(x,y) ((x)/(y)+((x)%(y)!=0))

using namespace std;

int n,m,test,cur = 1;
int Pd,Pg;
long long N,winD,roundD,winG,roundG;

int gcd(int a,int b){
	return (b==0)?a:(gcd(b,a%b));
}
void cul(long long &q,long long &p,int &w){
	if (w==0){
		q = 0;
		p = 1;
	} else{
		int tmp = gcd(w,100);
		q = w/tmp;
		p = 100/tmp;
	}
}
bool check(){
	if (Pd && !Pg) return false;
	if (!Pd && !Pg) return true;
	long long mult;
	cul(winD,roundD,Pd);
	cul(winG,roundG,Pg);
	mult = max(need(winD,winG),need(roundD,roundG));
	if (roundG==winG)
		if ((winG*mult-winD-(roundG*mult-roundD))>0) return false; else return true;
	//mult += need((winG*mult-winD-(roundG*mult-roundD)),(roundG-winG));
	if (roundD<=N) return true; else return false;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	for ( scanf("%d",&test) ; cur <= test ; cur++ ){
		printf("Case #%d: ",cur);
		cin >> N >> Pd >> Pg;
		//scanf("%lld%d%d",&N,&Pd,&Pg);
		if (check()) printf("Possible\n"); else printf("Broken\n");
	}
}
