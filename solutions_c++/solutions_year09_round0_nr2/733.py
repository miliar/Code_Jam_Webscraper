#include <stdio.h>
#include <string.h>
#define MAX 110

int n,m,mp[MAX][MAX],fa[MAX*MAX];
char c[MAX*MAX];
bool u[MAX][MAX];
int move[4][2] = {-1,0,0,-1,0,1,1,0};
int find_fa(int x){
	if (fa[x] == -1) return x;
	return fa[x] = find_fa(fa[x]);
}
void floodfill(int x,int y){
	int i,x0,y0,min = mp[x][y],minx = -1,miny;
	u[x][y] = true;
	for (i = 0;i < 4;i++){
		x0 = x+move[i][0],y0 = y+move[i][1];
		if (x0 >= 0 && x0 < n && y0 >= 0 && y0 < m &&
			mp[x0][y0] < min)
			min = mp[x0][y0],minx = x0,miny = y0;
	}
	if (minx == -1) return;
	if (!u[minx][miny]) floodfill(minx,miny);
	int fax = find_fa(x*m+y),fay = find_fa(minx*m+miny);
	if (fax != fay) fa[fay] = fax;
}
int main(){
	int t_case,t,i,j,d,fax;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t_case);
	for (t = 1;t <= t_case;t++){
		scanf("%d%d",&n,&m);
		for (i = 0;i < n;i++)
			for (j = 0;j < m;j++)
				scanf("%d",&mp[i][j]);
		memset(u,0,sizeof(u));
		memset(c,0,sizeof(c));
		memset(fa,-1,sizeof(fa));
		for (i = 0;i < n;i++)
			for (j = 0;j < m;j++)
				if (!u[i][j])
					floodfill(i,j);
		d = 0;
		for (i = 0;i < n;i++)
			for (j = 0;j < m;j++){
				fax = find_fa(i*m+j);
				if (!c[fax]) c[fax] = ++d;
			}
		printf("Case #%d:\n",t);
		for (i = 0;i < n;i++){
			fax = find_fa(i*m);
			putchar(c[fax]+'a'-1);
			for (j = 1;j < m;j++){
				putchar(' ');
				fax = find_fa(i*m+j);
				putchar(c[fax]+'a'-1);
			}
			putchar('\n');
		}
	}
	fclose(stdout);
}
