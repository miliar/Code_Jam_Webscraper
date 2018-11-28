#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;
#define ll long long
char word[600];
int R,C,D;
ll Wt[600][600];
ll Cx[600][600];
ll Cy[600][600];
ll Wx[600][600];
ll Wy[600][600];
ll mass[600][600];
ll M[600][600];
int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
    {
      scanf("%d%d%d",&R,&C,&D);

      for(int i=0;i<=R;i++)
	for(int j=0;j<=C;j++)
	  Cx[i][j]=Cy[i][j]=Wt[i][j]=mass[i][j]=Wx[i][j]=Wy[i][j]=0;
      for(int i=1;i<=R;i++)
	{
	  scanf("%s",&word);

	  for(int j=1;j<=C;j++)
	    {
	      mass[i][j]=word[j-1]-'0'+D;
	      Wt[i][j]=Wt[i-1][j]+Wt[i][j-1]-Wt[i-1][j-1]+mass[i][j];
	      Cx[i][j]=Cx[i-1][j]+Cx[i][j-1]-Cx[i-1][j-1]+i*mass[i][j];
	      Cy[i][j]=Cy[i-1][j]+Cy[i][j-1]-Cy[i-1][j-1]+j*mass[i][j];
	      Wx[i][j]=i*mass[i][j];
	      Wy[i][j]=j*mass[i][j];
	    }
				   
	}
      int opt=2;
      for(int i=1;i<=R;i++)
	for(int j=1;j<=C;j++)
	  {
	    for(int sz=max(2,opt)+1;sz<=min(i,j);sz++)
	      {
		ll cx=Cx[i][j]-Cx[i-sz][j]-Cx[i][j-sz]+Cx[i-sz][j-sz]-Wx[i][j]-Wx[i-sz+1][j]-Wx[i][j-sz+1]-Wx[i-sz+1][j-sz+1];
		ll cy=Cy[i][j]-Cy[i-sz][j]-Cy[i][j-sz]+Cy[i-sz][j-sz]-Wy[i][j]-Wy[i-sz+1][j]-Wy[i][j-sz+1]-Wy[i-sz+1][j-sz+1];
		ll W=Wt[i][j]-Wt[i-sz][j]-Wt[i][j-sz]+Wt[i-sz][j-sz]-mass[i][j]-mass[i-sz+1][j]-mass[i][j-sz+1]-mass[i-sz+1][j-sz+1];
		//printf("%d %d to %d %d is %lf %lf\n",i-sz+1,j-sz+1,i,j,cx/(double)W,cy/(double)W);
		//should be at i-(sz-1)/2 and j-(sz-1)/2
		if(cx*2==(2*i-(sz-1))*W && cy*2==(2*j-(sz-1))*W)
		  opt=max(opt,sz);
	      }
	  }
      if(opt==2)
	printf("Case #%d: IMPOSSIBLE\n",t);
      else
	printf("Case #%d: %d\n",t,opt);


    }
      
}
