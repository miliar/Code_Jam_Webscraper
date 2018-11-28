#include <iostream>
#include <cstdio>

using namespace std;

int d[200],l[200],f[200][200];
int n,test;


int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&test);
	for (int ttt=1; ttt<=test; ttt++){
		scanf("%d",&n);
		for (int i=1; i<=n; i++) scanf("%d%d",&d[i],&l[i]);
		scanf("%d",&d[n+1]);
		l[n+1]=2000*1000*1000;
		for (int i=0; i<=n+1; i++) 
			for (int j=0; j<=n+1; j++) f[i][j]=0;
		f[0][1]=1;
		for (int i=0; i<=n+1; i++)
			for (int j=i+1; j<=n+1; j++)
				if (f[i][j])
				{
					for (int k=j+1; k<=n+1; k++)
						if (d[k]>=d[i] && d[k]-d[j]<=min(d[j]-d[i],l[j]))
							f[j][k]=1;
				}
		int ok=0;
		for (int i=0; i<=n; i++)
			if (f[i][n+1]==1) ok =1;
		printf("Case #%d: ",ttt);
		if (ok) printf("YES\n");
		else printf("NO\n");	
	}
	
	
}