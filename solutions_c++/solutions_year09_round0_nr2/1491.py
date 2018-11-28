#include <iostream>
using namespace std;

int tc,n,m;
int arr[120][120];
int movex[4]={1,0,0,-1};
int movey[4]={0,1,-1,0};
int lala[120][120];
char out[120][120];
int con;

bool inside(int x,int y){
	if (x<0 || y <0 || x>=n || y>=m) 	return 0;
								return 1;	
}

void dfs(int i,int j,int color){
	int k;
	int minim=1000000;
	
	for (k=0;k<4;k++){
		if (inside(i+movex[k],j+movey[k])){
			if (arr[i+movex[k]][j+movey[k]] > arr[i][j] && lala[i+movex[k]][j+movey[k]]==0) {
				if (minim > arr[i+movex[k]][j+movey[k]])
				lala[i+movex[k]][j+movey[k]]=color;
				dfs(i+movex[k],j+movey[k],color);
			}
		}
	}	
}

void dfs2(int i,int j,char color,int bef){
	int k;
	
	for (k=0;k<4;k++){
		if (inside(i+movex[k],j+movey[k]) && lala[i+movex[k]][j+movey[k]]==bef && out[i+movex[k]][j+movey[k]]!=color){
			out[i+movex[k]][j+movey[k]]=color;
			dfs2(i+movex[k],j+movey[k],color,bef);
		}
	}	
}

int main(){
	int ii,i,j,k;
	
	scanf("%d",&tc);
	for (ii=0;ii<tc;ii++){
		memset(lala,0,sizeof(lala));
		memset(out,' ',sizeof(out));
		con=0;
		scanf("%d %d",&n,&m);
		for (i=0;i<n;i++)
			for (j=0;j<m;j++)
				scanf("%d",&arr[i][j]);
		
		for (i=0;i<n;i++){
			for (j=0;j<m;j++){
				for (k=0;k<4;k++){
					if (inside(i+movex[k],j+movey[k]))
						if (arr[i+movex[k]][j+movey[k]] < arr[i][j]) break;	
				}
				if (k==4){
					lala[i][j]=++con;
					dfs(i,j,con);	
				}
			}	
		}
		
		
		
		char cumi='a';
		for (i=0;i<n;i++){
			for (j=0;j<m;j++){
				if (out[i][j]==' '){
					out[i][j]=cumi;
					dfs2(i,j,cumi,lala[i][j]);	
					cumi++;
				}	
			}	
		}
		
		for (i=0;i<n;i++){
			printf("%c",out[i][0]);
			for (j=1;j<m;j++){
				printf(" %c",out[i][j]);	
			}	
			printf("\n");
		}
		
	}
	return 0;
}	
