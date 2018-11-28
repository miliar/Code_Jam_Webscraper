#include <stdio.h>
#include <string.h>

int H,W;
int h[110][110];
int f[110][110];

char v[110][110];

int dx[]={0,-1,0,0,1};
int dy[]={0,0,-1,1,0};

int IN(int nx,int ny){
	return nx>=0 && ny>=0 && nx<H && ny<W;
}


int getf(int idx){
	int x,y,fx,fy;
	x=idx/256; y=idx%256;
	fx=f[x][y]/256; fy=f[x][y]%256;
	return f[x][y]==idx?idx:f[x][y]=getf(fx*256+fy);
}

int main(){
	int t,cas;
	int nx,ny,d;
	int low;
	int idx;
	int i,j;
	char cur;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	for (cas=1;cas<=t;cas++){
		cur='a';
		scanf("%d%d",&H,&W);
		for (i=0;i<H;i++) for (j=0;j<W;j++)
			scanf("%d",&h[i][j]);
		for (i=0;i<H;i++) for (j=0;j<W;j++){
			f[i][j]=i*256+j;
			v[i][j]='0';
			low=h[i][j];
			for (d=0;d<5;d++){
				nx=i+dx[d];
				ny=j+dy[d];
				if (IN(nx,ny) && h[nx][ny]<low){
					low=h[nx][ny];
					f[i][j]=nx*256+ny;
				}
			}
		}
		for (i=0;i<H;i++) for (j=0;j<W;j++){
			if (v[i][j]!='0') continue;
			idx=getf(i*256+j);
			if (v[idx/256][idx%256]=='0'){
				v[i][j]=v[idx/256][idx%256]=cur;
				cur++;
			}else v[i][j]=v[idx/256][idx%256];
		}
		printf("Case #%d:\n",cas);
		for (i=0;i<H;i++){
			for (j=0;j<W;j++)
				printf("%c%c",v[i][j],j==W-1?'\n':' ');
		}
	}
	return 0;
}

