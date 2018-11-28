
#include <iostream>
using namespace std;

const int N =55;

char in[N][N],inr[N][N];
int n,k;

void move()
{
	int i,j,k;
	for(i=0;i<n;i++){
		for(j=n-1;j>=0;j--){
			if(in[i][j]=='.'){
				for(k=j-1;k>=0;k--){
					if(in[i][k]!='.'){
						in[i][j]=in[i][k];
						in[i][k]='.';
						break;
					}
				}
			}
		}
	}
}
void rotate()
{
	int i,j;
	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
			inr[j][n-i-1] =in[i][j];
}

int pos[8][2]={{-1,0},{-1,1},{0,1},{1,1},
{1,0},{1,-1},{0,-1},{-1,-1}};
bool out(int x,int y)
{
	return (x <0 || x>=n || y<0 || y>=n);
}
bool kmatch(int x,int y,int ch)
{
	int r[8],i,j,q;
	memset(r,0,sizeof(r));
	for(int p=0;p<8;p++){
		for(q=0;q<k;q++){
			i= x + pos[p][0]*q;
			j = y + pos[p][1]*q;
			if(out(i,j) || inr[i][j]!=ch)break;
			r[p]++;
		}
		if(r[p]>=k)return 1;
	}

	for(i=0;i<4;i++)
		if(r[i]+r[i+4]>k)
			return 1;

	return 0;
}
bool cal(char ch)
{
	int i,j;
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			if(inr[i][j]==ch && kmatch(i,j,ch))
				return 1;
		}
	}
	return 0;
}
int main()
{
	freopen("F://Google Code Jam//A-large.in","r",stdin);
	freopen("F://Google Code Jam//write.txt","w",stdout);
	int cas,t=1;
	scanf("%d",&cas);
	while(t<=cas)
	{
		printf("Case #%d: ",t);
		t++;

		scanf("%d %d",&n,&k);

		int i;
		for(i=0;i<n;i++)
			scanf("%s",in[i]);

		move();
		rotate();
		bool red=false,blue=false;
		red = cal('R');
		blue= cal('B');

		if(red && blue)
			printf("Both\n");
		else if(red)
			printf("Red\n");
		else if(blue)
			printf("Blue\n");
		else
			printf("Neither\n");
	}
	return 0;
}