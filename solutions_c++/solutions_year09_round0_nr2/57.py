#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define in(x,y) (x>=0 && x<y)
#define mp make_pair
#define lim 101

int cs,c,n,m,i,j,k,s,x,y,x2,y2,mn,z;
bool f;
int A[lim][lim],C[lim][lim],N[lim][lim],L[27];
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
queue <pair<int,int> > Q;

int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%d%d",&n,&m);
	for(i=0;i<n;i++)
	  for(j=0;j<m;j++)
	    scanf("%d",&A[i][j]);
	memset(C,-1,sizeof C);
	for(i=s=0;i<n;i++)
	  for(j=0;j<m;j++)
	  {
	    for(k=0,f=1,mn=-1;k<4;k++)
		{
		  x=i+dx[k];
		  y=j+dy[k];
		  if(in(x,n) && in(y,m))
		  {
		    if(A[x][y]<A[i][j])
		      f=0;
		    if(mn==-1 || A[x][y]<mn)
			  mn=A[x][y];
		  }
		}
	    if(f)
		{
		  C[i][j]=s++;
		  Q.push(mp(i,j));
		}
		if(mn!=-1)
		  for(k=0;k<4;k++)
		  {
		    x=i+dx[k];
		    y=j+dy[k];
		    if(in(x,n) && in(y,m) && A[x][y]==mn)
	        {
			  N[i][j]=k;
			  break;
			}
		  }
	  }
	while(!Q.empty())
	{
	  x=Q.front().first;
	  y=Q.front().second;
	  Q.pop();
	  for(k=0;k<4;k++)
	  {
		x2=x+dx[k];
		y2=y+dy[k];
		if(in(x2,n) && in(y2,m))
		{
		  z=N[x2][y2];
		  if(x2+dx[z]==x && y2+dy[z]==y && C[x2][y2]==-1)
		  {
		    C[x2][y2]=C[x][y];
			Q.push(mp(x2,y2));
		  }
		}
	  }
	}
	memset(L,-1,sizeof L);
	for(i=s=0;i<n;i++)
	  for(j=0;j<m;j++)
	    if(L[C[i][j]]==-1)
		  L[C[i][j]]=s++;
	printf("Case #%d:\n",c);
	for(i=0;i<n;i++)
	{
	  for(j=0;j<m;j++)
	  {
	    if(j)
		  printf(" ");
		printf("%c",L[C[i][j]]+'a');
	  }
	  printf("\n");
	}
  }  
  return 0;
}
