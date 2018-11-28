#include <cstdio>

int H, W, cnt, b[110][110], c[110][110];

void rec(int x, int y){
  if(x!=0&&b[x-1][y]==1000*x+y&&c[x-1][y]==-1){
    c[x-1][y]=cnt;
    rec(x-1, y);
  }
  if(x!=H-1&&b[x+1][y]==1000*x+y&&c[x+1][y]==-1){
    c[x+1][y]=cnt;
    rec(x+1, y);
  }
  if(y!=0&&b[x][y-1]==1000*x+y&&c[x][y-1]==-1){
    c[x][y-1]=cnt;
    rec(x, y-1);
  }
  if(y!=W-1&&b[x][y+1]==1000*x+y&&c[x][y+1]==-1){
    c[x][y+1]=cnt;
    rec(x, y+1);
  }  
}

int main(){
  int T, a[110][110], d[30];
  scanf("%d",&T);
  for(int tc=1;tc<=T;tc++){
    scanf("%d%d",&H,&W);
    for(int i=0;i<H;i++)
      for(int j=0;j<W;j++)
	scanf("%d",&a[i][j]);
    for(int i=0;i<H;i++)
      for(int j=0;j<W;j++){
	int min;
	min=a[i][j];
	if(i!=0&&a[i-1][j]<min){
	  min=a[i-1][j];
	  b[i][j]=1000*(i-1)+j;
	}
	if(j!=0&&a[i][j-1]<min){
	  min=a[i][j-1];
	  b[i][j]=1000*i+j-1;
	}
	if(j!=W-1&&a[i][j+1]<min){
	  min=a[i][j+1];
	  b[i][j]=1000*i+j+1;
	}
	if(i!=H-1&&a[i+1][j]<min){
	  min=a[i+1][j];
	  b[i][j]=1000*(i+1)+j;
	}
	if(min==a[i][j])b[i][j]=-1;
	c[i][j]=-1;
      }
    cnt=0;
    for(int i=0;i<H;i++)
      for(int j=0;j<W;j++)
	if(b[i][j]==-1){
	  c[i][j]=cnt;
	  rec(i, j);
	  cnt++;
	}
    for(int i=0;i<30;i++)d[i]=-1;
    int num=0;
    printf("Case #%d:\n",tc);
    for(int i=0;i<H;i++)
      for(int j=0;j<W;j++){
	if(d[c[i][j]]==-1){
	  printf("%c",'a'+num);
	  d[c[i][j]]=num;
	  num++;
	}
	else printf("%c",'a'+d[c[i][j]]);
	if(j==W-1)puts("");
	else printf(" ");
      }
  }
  return 0;
}
