#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;
const int pp[12]={1,2,4,8,16,32,64,128,256,512,1024,2048};
int tttt = 0, tree[6666][11],cost[6666],p,tand[6666],le[6666];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
 int i,j,t,k, T;
 scanf("%d",&T);
 while ( T-- ) 
 {	
  scanf("%d",&p);
  for (i=1;i<=pp[p];i++)
   scanf("%d",&le[i]);
  for (i=p-1;i>=0;i--)
  {
    for (j=pp[i];j<pp[i+1];j++)
     scanf("%d",&cost[j]);  
  }
  for (i=1;i<=pp[p];i++)
   tand[i-1+pp[p]]=le[i]; 
  j=p;
  do 
  { 		
   for (i=pp[j-1];i<pp[j];i++)
    tand[i]=min(tand[i*2],tand[i*2+1]);
   j--; 
  }while (j>0);	
  memset(tree,0,sizeof(tree));
  for (i=pp[p]-1;i>0;i--)
   {
     for (j=0;j<=p;j++)
      {
	   if (j>tand[i])
	     tree[i][j]=-1;
	   else
	    {
		  tree[i][j]=cost[i]+tree[i*2][j]+tree[i*2+1][j];
		  if (i>=pp[p-1]&&tand[i]>j) tree[i][j]=0;
		  if (i<pp[p-1]&&tree[i*2][j+1]>=0&&tree[i*2+1][j+1]>=0&&tree[i*2][j+1]+tree[i*2+1][j+1]<tree[i][j])	
		   tree[i][j]=tree[i*2][j+1]+tree[i*2+1][j+1];
	    }	 		
	  }
	 //cout<<i<<" "<<tree[i][0]<<endl; 
   }
  printf("Case #%d: %d\n",++tttt,tree[1][0]);  
 }	
 return 0;	
}

