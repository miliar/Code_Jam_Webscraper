#include<stdio.h>
const int maxn = 51;
char s[maxn][maxn];
char t[maxn][maxn];
const int d[4][2]={1,0,0,1,
                   1,1,-1,1};

int main() {
	int cs;
	scanf("%d",&cs);
	for (int step=1; step<=cs; ++step)
	{
		int n, k;
		scanf("%d%d",&n,&k);
		int i,j;
		for(i=0;i<n;i++){
			scanf("%s",&s[i]);
		}
		for(i=0;i<n;i++)for(j=0;j<n;j++){
			t[n-1-i][n-1-j] = s[i][j];
		}
		int x,y;
		for(x=0;x<n;x++){
			i = 0;
			for(y=0;y<n;y++)if(t[x][y]!='.'){
				t[x][i++] = t[x][y];
			}
			for(y=i;y<n;y++)t[x][y]='.';
		}
		bool B = false;
		bool R = false;
		for(x=0;x<n;x++)for(y=0;y<n;y++)
			if(t[x][y]!='.'){
		  for(i=0;i<4;i++){
			  int count = 1;
			  int x1=x,y1=y;
			  while(true){
				  x1+=d[i][0];
				  y1+=d[i][1];
				  if(x1>=0&&x1<n&&y1>=0&&y1<n&&
					  t[x1][y1]==t[x][y])
					  count++;
				  else break;
			  }
			  if(count>=k){
				  if(t[x][y]=='B') B=true;
				  else R=true;
			  }
		  }
		}
		printf("Case #%d: ", step);
		if(!B&&!R) printf("Neither\n");
		else if(B&&R) printf("Both\n");
		else if(B) printf("Blue\n");
		else  printf("Red\n");
	}
}