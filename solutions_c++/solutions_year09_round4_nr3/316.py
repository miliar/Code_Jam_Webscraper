#include <cstdio>
#include <algorithm>
using namespace std;

int c,n,m,e,x1,x2,y1,y2,p[20][30],u[20][20],AC;

int b[20][20],s[20],S;

void per(int x){
	int e;
	if (S>AC) return;
	if (x>n) AC=S<AC?S:AC;
	else{
		for (int i=1;i<=S;i++){
		e=1;
			for (int j=1;j<=s[i]&&e;j++) e=u[x][b[i][j]];
			if (!e) continue;
		s[i]++;
		b[i][s[i]]=x;
		per(x+1);
		s[i]--;
		}		
	S++;
	s[S]=1;
	b[S][1]=x;
	per(x+1);	
	s[S]=0;
	S--;
	}
}

int main(){
	scanf("%d",&c);
		for (int tc=1;tc<=c;tc++){
		scanf("%d%d",&n,&m);
			for (int i=1;i<=n;i++)
				for (int j=1;j<=m;j++) scanf("%d",&p[i][j]);
			for (int i=1;i<=n;i++)
				for (int j=i+1;j<=n;j++){
				e=1;
					for (int k=1;k<m&&e;k++){
					x1=p[i][k];
					y1=p[i][k+1];
					x2=p[j][k];
					y2=p[j][k+1];
						if (x1==x2||y1==y2) e=0;
						if (x2>x1) swap(x1,x2),swap(y1,y2);
						if (y2>y1) e=0;
					}
				u[i][j]=u[j][i]=e;
				}
		S=1;
		AC=n;
			for (int i=1;i<=n;i++) s[i]=0;
		s[1]=1;
		b[1][1]=1;
		per(2);
		printf("Case #%d: %d\n",tc,AC);
		}
	return 0;
}

