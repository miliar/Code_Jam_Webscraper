//shjj-Tic-Tac-Toe-Tomek

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

char s[5];
int a[5][5];
const int tx[4]={1,0,1,1};
const int ty[4]={0,1,1,-1};
void write(int typ)
{
if (typ==1) printf("X won\n");
if (typ==2) printf("O won\n");
if (typ==3) printf("Draw\n");
if (typ==4) printf("Game has not completed\n");
}

int main()
{
freopen("A.in","r",stdin);
freopen("A.out","w",stdout);
memset(a,120,sizeof(a));
int Test,TT=0;scanf("%d",&Test);
for (;Test--;)
{
printf("Case #%d: ",++TT);
bool End=1;
for (int i=1;i<=4;i++)
  {
  scanf("%s",s+1);
  for (int j=1;j<=4;j++)
    {
	if (s[j]=='X') a[i][j]=1;
	if (s[j]=='O') a[i][j]=2;
	if (s[j]=='T') a[i][j]=0;
	if (s[j]=='.') a[i][j]=3,End=0;
	}
  }
bool flag=0;
for (int i=1;i<=4&&!flag;i++)
  for (int j=1;j<=4&&!flag;j++)
    if (a[i][j]<3)
	  {
      for (int k=0;k<4;k++)
		{
		if (k==0&&i!=1) continue;
		if (k==1&&j!=1) continue;
		if (k==2&&(i!=1||j!=1)) continue;
		if (k==3&&(i!=1||j!=4)) continue;
		int now=a[i][j],ss=1,x=i,y=j;
		for (int l=0;l<3;l++)
		  {
		  x+=tx[k],y+=ty[k];
		  if (a[x][y]>=3||i>4||j<1||j>4) break;
		  if (now&&a[x][y]&&a[x][y]!=now) break;
		    else {
			     if (a[x][y]) now=a[x][y];
			     ss++;
				 }
		  }
		if (ss==4&&now) {flag=1;write(now);break;}
		}
	  }
if (End&&!flag) write(3);
if (!End&&!flag) write(4);
}
}