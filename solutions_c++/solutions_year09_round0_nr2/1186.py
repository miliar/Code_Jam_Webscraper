#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int u[]={-1,0,0,1};
int v[]={0,-1,1,0};

int m[250][250],w,h;
bool us[250][250];
int cor[250][250];
char letra[25000];

bool valid(int a, int b) {
	if (a<h && a>=0 && b<w && b>=0) return true;
	return false;
}

int flow(int a, int b) {
	int mn=1000000;
	for (int i=0; i<4; i++) 
		if (valid(a+u[i],b+v[i])) mn=min(mn,m[a+u[i]][b+v[i]]);
	
	if (mn>=m[a][b]) return -1;
	
	for (int i=0; i<4; i++) 
		if (valid(a+u[i],b+v[i]) && mn==m[a+u[i]][b+v[i]]) return i;
}

void dfs(int x, int y, int c) {
	if (us[x][y]) return;
	us[x][y]=true;
	
	cor[x][y]=c;
	
	for (int i=0; i<4; i++)
		if (valid(x+u[i],y+v[i])) {
			int k=flow(x+u[i],y+v[i]);
			if (k==-1) continue;
			if (x+u[i]+u[k]==x && y+v[i]+v[k]==y) dfs(x+u[i],y+v[i],c);
		}
}

int main() {
	int nt;
	
	scanf(" %d",&nt);
	for (int ct=1; ct<=nt; ct++) {
		scanf(" %d %d",&h,&w);
		for (int i=0; i<h; i++)
			for (int j=0; j<w; j++) scanf(" %d",&m[i][j]);
			
		memset(us,0,sizeof(us));
		int nc=0;
		for (int i=0; i<h; i++)
			for (int j=0; j<w; j++) 
				if (flow(i,j)==-1) dfs(i,j,nc++);
				
		memset(letra,'@',sizeof(letra));
		char nl='a';
		
		printf("Case #%d:\n",ct);
		for (int i=0; i<h; i++) {
			for (int j=0; j<w; j++) {
				if (letra[cor[i][j]]=='@') letra[cor[i][j]]=nl++;
				if (j) printf(" ");
				printf("%c",letra[cor[i][j]]);
			}
			printf("\n");
		}
	}
	
	return 0;
}
