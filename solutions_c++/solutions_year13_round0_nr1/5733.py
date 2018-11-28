#include <stdio.h>
int dr[8]={-1,-1,0,1,1,1,0,-1};
int dc[8]={0,1,1,1,0,-1,-1,-1};
char v[4][5];
char check(int r,int c,int dir,char who){
	if(v[r][c]=='.')
		return '-';
	int nr=r+dr[dir];
	int nc=c+dc[dir];
	if(nr==-1 || nc==-1 || nr==4 || nc==4)
		return who;
	if(v[nr][nc]==v[r][c] || v[nr][nc]=='T' || v[r][c]=='T')
		return check(nr,nc,dir,who=='T'?v[nr][nc]:who);
	return '-';
}
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	bool s=0;
	char res;
	scanf("%d",&t);
	for(int k=1;k<=t;++k){
		printf("Case #%d: ",k);
		for(int i=s=0;i<4;++i){
			scanf("%s",v[i]);
			for(int j=0;j<4;++j)
				s|=v[i][j]=='.';
		}
		for(int i=0;i<4;++i){
			res=check(0,i,4,'T');
			if(res=='-')
				res=check(i,0,2,'T');
			if(res!='-')
				break;
		}
		if(res=='-')
			res=check(0,0,3,'T');
		if(res=='-')
			res=check(0,3,5,'T');
		if(res!='-')
			printf("%c won\n",res);
		else if(s)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
	}
	return 0;
}