#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define in(x,y) (x>=0 && x<y)
#define ST vector <pair<int,int> >
#define lim 13

int cs,c,i,j,k,p,n,m,sz,x,y,z,x2,y2,x3,y3;
bool f;
ST V,E,V2;
int dx[]={-1,0,1,0},dy[]={0,1,0,-1};
char A[lim][lim];
queue <ST> Q;
map <ST,int> M;
bool B[lim][lim];

void enqueue(ST V,int i,int x,int y,int z)
{
  V[i]=mp(x,y);
  sort(V.begin(),V.end());
  if(!M[V])
  {
    M[V]=z;
	Q.push(V);
  }
}
int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%d%d",&n,&m);
	V.clear();
	E.clear();
	for(i=0;i<n;i++)
	{
	  scanf("%s",A[i]);
	  for(j=0;j<m;j++)
	    if(A[i][j]=='o')
		{
		  V.pb(mp(i,j));
		}
		else if(A[i][j]=='x')
		  E.pb(mp(i,j));
		else if(A[i][j]=='w')
		{
		  V.pb(mp(i,j));
		  E.pb(mp(i,j));
	    }
	}
	printf("Case #%d: ",c);
	if(V.size()!=E.size())
	{
	  printf("-1\n");
	  continue;
	}
	sz=V.size();
	sort(V.begin(),V.end());
	sort(E.begin(),E.end());
	while(!Q.empty())
	  Q.pop();
	Q.push(V);
	M.clear();
	M[V]=1;
	while(!Q.empty())
	{
	  V=Q.front();
	  z=M[V];
/*	  for(i=0;i<sz;i++)
	    printf("%d %d\n",V[i].f,V[i].s);
	  p(z-1);*/
	  Q.pop();
	  V2=V;
	  if(V==E)
	    break;
	  memset(B,0,sizeof B);
	  for(i=0;i<sz;i++)
		B[V[i].f][V[i].s]=1;
	  if(sz==1)
	    f=1;
	  else
	  {
	    f=1;
		for(i=0;i<sz;i++)
		{
	      for(j=0;j<4;j++)
		  {
		    x=V[i].f+dx[j];
		    y=V[i].s+dy[j];
			if(in(x,n) && in(y,m) && B[x][y])
			  break;
		  }
		  if(j==4)
		    f=0;
		}
	  }
	  for(i=0;i<sz;i++)
	    for(j=0;j<4;j++)
		{
		  x=V[i].f+dx[j];
		  y=V[i].s+dy[j];
		  x3=V[i].f-dx[j];
		  y3=V[i].s-dy[j];
		  if(in(x,n) && in(y,m) && in(x3,n) && in(y3,m) && !B[x][y] && A[x][y]!='#' && !B[x3][y3] && A[x3][y3]!='#')
		  {
		    if(f)
			  enqueue(V,i,x,y,z+1);
			else
			{
			  V2=V;
			  V2[i]=mp(x,y);
			  for(k=0;k<sz;k++)
			  {
			    for(p=0;p<sz;p++)
				  if(p!=sz && abs(V2[k].f-V2[p].f)+abs(V2[k].s-V2[p].s)==1)
			        break;
			    if(p==sz)
				  break;
			  }
			  if(k==sz)
			    enqueue(V,i,x,y,z+1);
			}
		  }	  
		}
	}
	printf("%d\n",M[E]-1);
  }
  return 0;
}
