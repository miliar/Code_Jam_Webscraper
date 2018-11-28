#include <stdio.h>

int h[102][102],li[10000][2],lic;
char sink[102][103];
int r,c;
int ir[]={-1,0,0,1},ic[]={0,-1,1,0};

void dfs(int i0, int j0){
	lic=0;
	int i=i0,j=j0,k;
	while(sink[i][j]==0){
		li[lic][0]=i;
		li[lic][1]=j;
		lic++;
		int minh=h[i][j];
		for (k=0; k<4; k++){
			if (h[i+ir[k]][j+ic[k]]<minh) minh=h[i+ir[k]][j+ic[k]];
		}
		for (k=0; k<4; k++){
			if (h[i+ir[k]][j+ic[k]]==minh) break;
		}
		i=i+ir[k];
		j=j+ic[k];
	}
	for (k=0; k<lic; k++)
		sink[li[k][0]][li[k][1]]=sink[i][j];
}

int main(){
	int i,j,t,u,k;
	scanf("%d",&t);
	for (u=0; u<t; u++){
		scanf("%d%d",&r,&c);
		for (i=0; i<r+2; i++) h[i][0]=h[i][c+1]=100000;
		for (j=0; j<c+2; j++) h[0][j]=h[r+1][j]=100000;
		for (i=1; i<=r; i++) for (j=1; j<=c; j++) sink[i][j]=0;
		for (i=1; i<=r; i++) for (j=1; j<=c; j++) scanf("%d",&h[i][j]);
		int cn=0;
		for (i=1; i<=r; i++) for (j=1; j<=c; j++){
			for (k=0; k<4; k++){
				if (h[i+ir[k]][j+ic[k]]<h[i][j]) break;
			}
			if (k==4){
				sink[i][j]='a'+cn;
				cn++;
			}
		}
		for (i=1; i<=r; i++) for (j=1; j<=c; j++) dfs(i,j);
		cn=0;
		int order[26];
		for (i=0; i<26; i++) order[i]=-1;
		for (i=1; i<=r; i++) for (j=1; j<=c; j++) if (order[sink[i][j]-'a']==-1) order[sink[i][j]-'a']=cn++;
		printf("Case #%d:\n",u+1);
		for (i=1; i<=r; i++){
			printf("%c",'a'+order[sink[i][1]-'a']);
			for (j=2; j<=c; j++) printf(" %c",'a'+order[sink[i][j]-'a']);
			printf("\n");
		}
	}
	return 0;
}
