#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
using namespace std;
#define mx 100
#define lim 201*201
#define lim2 210
#define os 100
#define p(x) cout<<#x<<":"<<x<<"\n"

int cs,c,n,i,j,m,sz,x,y,cnt,d,area,interior,boundary,pick,f,area2;
string s;
int dx[]={0,1,0,-1},dy[]={1,0,-1,0};
char str[22];
int X[lim],Y[lim];
bool B[lim2][lim2],B2[lim2][lim2];

int cross(int x1,int y1,int x2,int y2)
{
  return x1*y2-x2*y1;
}
int main()
{
  scanf("%d",&cs);
  for(c=0;c<cs;c++)
  {
    scanf("%d",&n);
	s="";
	for(i=0;i<n;i++)
	{
	  scanf("%s %d",str,&m);
	  for(j=0;j<m;j++)
	    s+=str;
	}
	sz=s.size();
	x=0;
	y=0;
	cnt=0;
	d=0;
	i=0;
	if(s[i]=='R')
	{
	  d=(d+1)%4;
	  i++;
	}
	else if(s[i]=='L')
	{
	  d=(d+1)%4;
	  i++;
	}
	memset(B,0,sizeof B);
	while(i<sz)
	{
	  while(i<sz && s[i]=='F')
	  {
	    B[x+mx][y+mx]=1;
	    X[cnt]=x;
	    Y[cnt]=y;
	    cnt++;
	    x+=dx[d];
	    y+=dy[d];
	    i++;
	  }
	  if(i<sz)
	  {
	    if(s[i]=='R')
		  d=(d+1)%4;
		else
		  d=(d+3)%4;
	    i++;
	  }
	}
	area=0;
	for(i=0;i<cnt;i++)
	  area+=cross(X[i],Y[i],X[(i+1)%cnt],Y[(i+1)%cnt]);
	area=abs(area)/2;
	interior=0;
	boundary=0;
	memset(B2,0,sizeof B);
    for(x=-mx;x<=mx;x++)
      for(y=-mx;y<=mx;y++)
	  {
	    if(B[x+os][y+os])
		  B2[x+os][y+os]=1;
		else
		{
		  f=0;
		  i=y;
		  while(i>=-mx && !B[x+os][i+os])
		    i--;
		  j=y;
		  while(j<=mx && !B[x+os][j+os])
		    j++;
		  if(i>=-mx && j<=mx)
		    f=1;
		  i=x;
		  while(i>=-mx && !B[i+os][y+os])
		    i--;
		  j=x;
		  while(j<=mx && !B[j+os][y+os])
		    j++;
		  if(i>=-mx && j<=mx)
		    f=1;
		  if(f)
		  {
		    interior++;
			B2[x+os][y+os]=1;
		  }
		}
	  }
	area2=0;
	for(x=-mx;x<mx;x++)
      for(y=-mx;y<mx;y++)
	    if(B2[x+os][y+os] && B2[x+os][y+1+os] && B2[x+1+os][y+os] && B2[x+1+os][y+1+os])
		  area2++;
	printf("Case #%d: %d\n",c+1,area2-area);
  }
  return 0;
}
