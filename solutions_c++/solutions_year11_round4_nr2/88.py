#include <stdio.h>
#define MAXL 505

int rn,cn;
char g[MAXL][MAXL];
int gs[MAXL][MAXL];
int rlad1[MAXL][MAXL],rlad2[MAXL][MAXL];
int clad1[MAXL][MAXL],clad2[MAXL][MAXL];

inline int min(int a,int b) { return a<b?a:b; }

inline void pre() {
	int i,j;
	for(i=0;i<=rn;i++) {
		gs[i][0]=0;
		rlad1[i][0]=rlad2[i][0]=0;
		clad1[i][0]=clad2[i][0]=0;
	}
	for(j=0;j<=cn;j++) {
		gs[0][j]=0;
		rlad1[0][j]=rlad2[0][j]=0;
		clad1[0][j]=clad2[0][j]=0;
	}
	for(i=0;i<rn;i++) {
		for(j=0;j<cn;j++) {
			gs[i+1][j+1]=gs[i][j+1]+gs[i+1][j]-gs[i][j]+g[i][j];
			rlad1[i+1][j+1]=rlad1[i+1][j]+rlad1[i][j+1]-rlad1[i][j]+g[i][j]*(i+1);
			rlad2[i+1][j+1]=rlad2[i+1][j]+rlad2[i][j+1]-rlad2[i][j]+g[i][j]*(rn-i);
			clad1[i+1][j+1]=clad1[i+1][j]+clad1[i][j+1]-clad1[i][j]+g[i][j]*(j+1);
			clad2[i+1][j+1]=clad2[i+1][j]+clad2[i][j+1]-clad2[i][j]+g[i][j]*(cn-j);
		}
	}
}

inline int getg(int r1,int r2,int c1,int c2) {
	return gs[r2+1][c2+1]-gs[r2+1][c1]-gs[r1][c2+1]+gs[r1][c1];
}
inline int getu(int r1,int r2,int c1,int c2) {
	return rlad2[r2+1][c2+1]-rlad2[r2+1][c1]-rlad2[r1][c2+1]+rlad2[r1][c1]-getg(r1,r2,c1,c2)*(rn-r2-1);
}
inline int getb(int r1,int r2,int c1,int c2) {
	return rlad1[r2+1][c2+1]-rlad1[r2+1][c1]-rlad1[r1][c2+1]+rlad1[r1][c1]-getg(r1,r2,c1,c2)*(r1);
}
inline int getl(int r1,int r2,int c1,int c2) {
	return clad2[r2+1][c2+1]-clad2[r2+1][c1]-clad2[r1][c2+1]+clad2[r1][c1]-getg(r1,r2,c1,c2)*(cn-c2-1);
}
inline int getr(int r1,int r2,int c1,int c2) {
	return clad1[r2+1][c2+1]-clad1[r2+1][c1]-clad1[r1][c2+1]+clad1[r1][c1]-getg(r1,r2,c1,c2)*(c1);
}

inline bool goodblade(int r1,int r2,int c1,int c2) {
	int l=(r2-r1+1)/2,ll=r2-r1+1;
	int p1=g[r1][c1],p2=g[r1][c2],p3=g[r2][c1],p4=g[r2][c2];
	int au,ab,al,ar;
	if(ll&1) au=getu(r1,r1+l-1,c1,c2)-(p1+p2)*l;
	else au=getu(r1,r1+l-1,c1,c2)*2-getg(r1,r1+l-1,c1,c2)-(p1+p2)*(2*l-1);
	if(ll&1) ab=getb(r2-l+1,r2,c1,c2)-(p3+p4)*l;
	else ab=getb(r2-l+1,r2,c1,c2)*2-getg(r2-l+1,r2,c1,c2)-(p3+p4)*(2*l-1);
	if(au!=ab) return 0;
	if(ll&1) al=getl(r1,r2,c1,c1+l-1)-(p1+p3)*l;
	else al=getl(r1,r2,c1,c1+l-1)*2-getg(r1,r2,c1,c1+l-1)-(p1+p3)*(2*l-1);
	if(ll&1) ar=getr(r1,r2,c2-l+1,c2)-(p2+p4)*l;
	else ar=getr(r1,r2,c2-l+1,c2)*2-getg(r1,r2,c2-l+1,c2)-(p2+p4)*(2*l-1);
	if(al!=ar) return 0;
	return 1;
}

inline bool process(int l) {
//	printf("<%d>\n",l);
	int i,j;
	for(i=0;i<=rn-l;i++)
		for(j=0;j<=cn-l;j++)
			if(goodblade(i,i+l-1,j,j+l-1)) return 1;
}

inline int solve() {
	int l;
	pre();
	for(l=min(rn,cn);l>=3;l--)
		if(process(l)) return l;
	return 0;
}

int main(void)
{
	int t,casenum=1;
	int i,j,sol;
	scanf("%d",&t);
	while(t--) {
		scanf("%d %d %*d",&rn,&cn);
		for(i=0;i<rn;i++) {
			scanf("%s",g[i]);
			for(j=0;j<cn;j++)
				g[i][j]-='0';
		}
		printf("Case #%d: ",casenum++);
		sol=solve();
		if(sol>=3) printf("%d\n",sol);
		else puts("IMPOSSIBLE");
	}
}
