#include<cstdio>
#include<cstring>
#define INF 1234567890

int P;
int t,T;
int A[11][1024];
int ANS[11][1024][11][2];

int fans(int r, int x, int p) {
	if(r==P) {
		if(P-A[P][x] <= p) return 0;
		return -1;
	}
	if(ANS[r][x][p][0] == t) return ANS[r][x][p][1];
	
	int mc = -1;
	
	{
		//Don't buy
		int c1 = fans(r+1,2*x,p), c2 = fans(r+1,2*x+1,p), c;
		if(c1 >= 0 && c2 >= 0) c = c1+c2;
		else c=-1;
		if(mc < 0 || (c>=0 && c<mc) ) mc = c;
	}
	
	{
		int c1 = fans(r+1,2*x,p+1), c2 = fans(r+1,2*x+1,p+1), c;
		if(c1 >= 0 && c2 >= 0) c = A[r][x]+c1+c2;
		else c=-1;
		if(mc < 0 || (c>=0 && c<mc) ) mc = c;
	}
	ANS[r][x][p][0]=t;
	ANS[r][x][p][1]=mc;
	return mc;
}

int main() {
	int i,j;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		scanf("%d",&P);
		for(i=P;i>=0;i--) {
			for(j=0;j<(1<<i);j++) scanf("%d",&A[i][j]);
		}
		printf("Case #%d: %d\n",t,fans(0,0,0));
		
	}
	return 0;
}
