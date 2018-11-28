#include <cstdio>
#include <algorithm>

using namespace std;


int cases;
int R,C;
int ans;

int grid[15][15];
bool person[15][15];
char str[15];

int dx[5]={-1,0,0,-1,0};
int dy[5]={-1,-1,0,1,1};

void DFS(int r,int c,int ct) {
	if (c==C+1) {
		c=1;
		r++;
	}
	if (r==R+1) {
		ans>?=ct;
		return;
	}
	if (ct+(R-r+1)*((C+1)/2)<=ans) {
		return;
	}	
	if (grid[r][c]==0) {
		bool yes=true;
		for(int i=0;i<5;i++) {
			int x=r+dx[i];
			int y=c+dy[i];
			if (person[x][y]) {
				yes=false;
				break;
			}
		}
		if (yes) {
			person[r][c]=true;
			for(int i=0;i<5;i++) {
				int x=r+dx[i];
				int y=c+dy[i];
				grid[r][c]++;
			}
			DFS(r,c+1,ct+1);
			person[r][c]=false;
			for(int i=0;i<5;i++) {
				int x=r+dx[i];
				int y=c+dy[i];
				grid[r][c]--;
			}			
		}
	}
	DFS(r,c+1,ct);
}

int main() {
	FILE * fin=fopen("C.in","r");
	FILE * fout=fopen("C.out","w");
	
	fscanf(fin,"%d ",&cases);
	for(int h=0;h<cases;h++) {
		ans=0;
		memset(grid,0,sizeof(grid));
		memset(person,0,sizeof(person));
		fscanf(fin,"%d %d ",&R,&C);
		for(int i=1;i<=R;i++) {
			fscanf(fin,"%s ",str);
			for(int j=1;j<=C;j++) {
				if (str[j-1]=='x') {
					grid[i][j]++;
				}
			}
		}
		DFS(1,1,0);
		fprintf(fout,"Case #%d: %d\n",h+1,ans);
	}
	return 0;
}
