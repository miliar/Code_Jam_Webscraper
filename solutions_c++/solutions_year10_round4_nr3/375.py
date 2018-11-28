#include <cstdio>
#include <algorithm>
#define INF (1<<29)
using namespace std;

int c,n,x1,y1,x2,y2,S,AC;
int v[105][105],u[105][105];


int main(){
	scanf("%d",&c);
	for (int tc=1;tc<=c;tc++){
		memset(v,0,sizeof(v));
		scanf("%d",&n);
		while (n--){
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (int i=x1;i<=x2;i++)
				for (int j=y1;j<=y2;j++) v[i][j]=1;
		}
		AC=0;
		do{
			for (int i=1;i<=100;i++)
				for (int j=1;j<=100;j++)
				    if (v[i][j]){
						if (!v[i-1][j]&&!v[i][j-1]) u[i][j]=0;
						else u[i][j]=1;
					}
					else{
						if (v[i-1][j]&&v[i][j-1]) u[i][j]=1;
						else u[i][j]=0;
					}
			S=0;
			for (int i=1;i<=100;i++)
			    for (int j=1;j<=100;j++){
					v[i][j]=u[i][j];
					S+=v[i][j];
				}
			AC++;
		}   while (S!=0);
		printf("Case #%d: %d\n",tc,AC);

	}
	return 0;
}
