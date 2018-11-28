#include<cstdio>
#include<algorithm>
using namespace std;
struct Point{
    int t,id;
};
Point A[200],B[200];
int nbA,nbB,NA,NB;
bool Cmp(Point A, Point B){
    if(A.t==B.t) return A.id>B.id;
     return A.t<B.t;
}
inline void calc(){
    nbA=nbB=0;
    int act=0;
    for(int i=0;i<NA+NB;i++)
	if(A[i].id){
	    act--;
	}
	else {act++; nbA=max(nbA, act);}
    act=0;
    for(int i=0;i<NA+NB;i++)
	if(B[i].id){
	    act--;
	}
	else {act++; nbB=max(nbB, act);}
}
int main()
{
    int N,T;
    int a,b,c,d;
    Point tmp;
    scanf("%d", &N);
    for(int i=1;i<=N;i++){
	scanf("%d%d%d", &T, &NA, &NB);
	for(int j=0;j<NA;j++){
	    scanf("%d:%d%d:%d", &a, &b, &c, &d);
	    a=a*60+b;
	    c=c*60+d+T;
	    tmp.t=a;
	    tmp.id=0;
	    A[j]=tmp;
	    tmp.t=c;
	    tmp.id=1;
	    B[j]=tmp;
	}
	for(int j=0;j<NB;j++){
	    scanf("%d:%d%d:%d", &a, &b, &c, &d);
	    a=a*60+b;
	    c=c*60+d+T;
	    tmp.t=a;
	    tmp.id=0;
	    B[NA+j]=tmp;
	    tmp.t=c;
	    tmp.id=1;
	    A[NA+j]=tmp;
	}
	sort(A, A+NA+NB, Cmp);
	sort(B, B+NA+NB, Cmp);
	calc();
	printf("Case #%d: %d %d\n", i, nbA, nbB);
    }
    return 0;
}
