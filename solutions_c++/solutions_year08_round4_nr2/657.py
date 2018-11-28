#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int n,m,a;
int s[50*50+1];
int x1, y1, x2, y2;

int main() {
	int cs, step;
	scanf("%d",&cs);	
	for(step=1;step<=cs;step++)
	{
		int i,j,k;
		scanf("%d%d%d",&n,&m,&a);
		
		
		memset(s, 0, sizeof(s));
		for(i=1;i<=n;i++)for(j=0;j<=m;j++)
		{
			s[i*j] = i;			
		}

		x1 = -1;

		if(a<=n*m){
			i = 0;
			j = a;
			for(; j<=n*m; i++,j++)if(s[i] && s[j])
			{
				x1 = s[i];
				y2 = i / s[i];

				x2 = s[j];
				y1 = j / s[j];
				break;
			}	
		}
		if(x1==-1) printf("Case #%d: IMPOSSIBLE\n", step);
		else printf("Case #%d: 0 0 %d %d %d %d\n", step, x1,y1,x2,y2);
	}
	return 0;
}