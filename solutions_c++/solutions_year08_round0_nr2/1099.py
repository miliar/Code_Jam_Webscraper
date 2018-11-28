// B.cc

#include <stdio.h>
#include <string.h>
#include <algorithm>
#define maxn 128

using namespace std;

int A1[maxn],A2[maxn];
int B1[maxn],B2[maxn];
int NA,NB,N,T;

int myget(int a[],int b[],int na,int nb){
	int i,j,res;
	res=nb;
	for (i=0,j=0;i<na;i++){
		while (j<nb){
			if (a[i]<=b[j]){
//				printf("a[%d]=%d b[%d]=%d\n",i,a[i],j,b[j]);
				res--;
				j++;
				break;
			}
			j++;
		}
	}
	return res;
}

void solve(int cas){
	int i,hh,mm,l,r;
	scanf("%d%d%d",&T,&NA,&NB);
	for (i=0;i<NA;i++){
		scanf("%d:%d",&hh,&mm);
		A1[i]=hh*60+mm;
		scanf("%d:%d",&hh,&mm);
		A2[i]=hh*60+mm+T;
	}
	for (i=0;i<NB;i++){
		scanf("%d:%d",&hh,&mm);
		B1[i]=hh*60+mm;
		scanf("%d:%d",&hh,&mm);
		B2[i]=hh*60+mm+T;
	}
	sort(A1,A1+NA);
	sort(A2,A2+NA);
	sort(B1,B1+NB);
	sort(B2,B2+NB);
	l=myget(B2,A1,NB,NA);
	r=myget(A2,B1,NA,NB);
	printf("Case #%d: %d %d\n",cas,l,r);
}

int main(){
	int cas;
//	freopen("B-large.in","r",stdin);
//	freopen("B-large.out","w",stdout);
	scanf("%d",&N);
	for (cas=1;cas<=N;cas++)
		solve(cas);
	return 0;
}
