
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<cstdio>

#define F(i,n) for( i = 1; i <=(int)n;i++)
#define FE(i,v) for( typeof((v).begin()) i = (v).begin(); i!= (v).end();i++)

using namespace std;

int m, n;
int a[105][105];
const int inf = 1<<25;
int dy[]={0,-1,1,0};
int dx[]={-1,0,0,1};
char done[105][105];
char used;
char fill( int x, int y, char c)
{
//   printf("filling %d %d %c\n",x,y,c);
   if(done[x][y]) return done[x][y];
   int k, s = a[x][y],xx,yy, sk=5;
   for(k=0;k<4;k++) 
   {
      xx=x+dx[k];
      yy=y+dy[k];
      if( a[xx][yy] < s) 
      {
	 s=a[xx][yy];
	 sk=k;
      }
   }
 //  printf("sk=%d\n",sk);
   if(sk!=5)
   {
      done[x][y] = fill(x+dx[sk],y+dy[sk],c);
   }
   else done[x][y] = c;
   return done[x][y];
	    
}
int main()
{
   int i, j, t, tt;
   scanf("%d",&tt);
   F(t,tt)
   {
      memset(a,100,sizeof(a));
      memset(done,0,sizeof(done));
      used = 'a';
      scanf("%d%d",&m,&n);
      F(i,m)
	 F(j,n)
	 scanf("%d",a[i]+j);
      F(i,m)
	 F(j,n)
	 {
//	    printf("%d %d\n",i,j);
	    if(!done[i][j])
//	    fill(i,j,used++);
	    if(fill(i,j,used)==used) used++;
//	    if(!done[i][j] ) { done[i][j] = used++; fill(i,j);}
	 }
      printf("Case #%d:\n",t);
      F(i,m)
      {
	 F(j,n)
	 {
	    printf("%c ",done[i][j]);
	    
	 }
	 puts("");

      }
   }

   return 0;
}
