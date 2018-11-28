//World Cup
#include<cstdio>
#include<algorithm>
using namespace std;
typedef long long LL;
const int MAXN = 1<<12;
const LL OO = (1LL<<30);
const bool dbgRead = 0;
const bool dbg = 0;
int M[MAXN];
int p[MAXN];
int P;
int n;
void read(){
	scanf("%d",&P);
	n = 1 << P;
	for(int i=0;i<n;i++)
		scanf("%d",&M[i]);
	for(int i=n-1;i>0;i--)
		scanf("%d",&p[i]);
	reverse(M,M+n);
	if(dbgRead){
		printf("M:[");
		for(int i=0;i<n;i++)
			printf("%d ",M[i]);
		printf("]\n");
		printf("p:[");
		for(int i=1;i<n;i++)
			printf("%d%c",p[i],(i&(i+1))?' ':'\n');
		printf("]\n");
	}
}

LL compute(int v,int beg,int end){
	if(end - beg == 1){
		if(M[beg] >= 0)return 0;
		else return OO;
	}
	int mid = (beg+end)/2;
	for(int i = beg; i<end; i++){
		//if(M[i]==0)return r2;
		M[i]--;
	}
	LL r1 = compute(2*v,beg,mid) + compute(2*v+1,mid,end);
	for(int i = beg;i<end;i++){
		M[i]++;
	}
	LL r2 = p[v] + compute(2*v,beg,mid) + compute(2*v+1,mid,end);
	if(dbg){
		printf("M:[");
		for(int i=beg;i<end;i++)
			printf("%d ",M[i]);
		printf("]\n");
	}
	if(dbg)printf("compute(%d,[%d,%d)) (p[v]:%d) %lld\n",v,beg,end,p[v],min(r1,r2));
	return min(r1,r2);
}

void computeCase(int c){
	int res = compute(1,0,n);	
	printf("Case #%d: %d\n",c+1,res);
}
int main(){
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		read();
		computeCase(i);
	}
	return 0;
}
