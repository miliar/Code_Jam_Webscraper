#include<stdio.h>
int ans[200];
int normalMode[31][3]=
{
  {0,0,0},
  {0,0,1},
  {0,1,1},
  {1,1,1},
  {1,1,2},
  {1,1,3},
  {2,2,2},
  {2,2,3},
  {2,3,3},
  {3,3,3},
  {3,3,4},
  {3,4,4},
  {4,4,4},
  {4,4,5},
  {4,5,5},
  {5,5,5},
  {5,5,6},
  {5,6,6},
  {6,6,6},
  {6,6,7},
  {6,7,7},
  {7,7,7},
  {7,7,8},
  {7,8,8},
  {8,8,8},
  {8,8,9},
  {8,9,9},
  {9,9,9},
  {9,9,10},
  {9,10,10},
  {10,10,10}   
};
int superMode[31][3]=
{
  {0,0,0},
  {0,0,0},
  {0,0,2},
  {0,1,2},
  {0,0,0},
  {1,2,2},
  {1,2,3},
  {0,0,0},
  {2,2,4},
  {2,3,4},
  {0,0,0},
  {3,3,5},
  {3,4,5},
  {0,0,0},
  {4,4,6},
  {4,5,6},
  {0,0,0},
  {5,5,7},
  {5,6,7},
  {0,0,0},
  {6,6,8},
  {6,7,8},
  {0,0,0},
  {7,7,9},
  {7,8,9},
  {0,0,0},
  {8,8,10},
  {8,9,10},
  {0,0,0},
  {0,0,0},
  {0,0,0}
};
int keySuper[31]={0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0};
int no[10];
int su[10];
int sol[10];
int max(int p[]);
int main()
{
  int T;
  
  //cheat code...
 /* printf("\nNormal Mode Triplets\n");
  for(int i=0;i<=30;i++)
    printf("%2d: %d %d %d MAX:%d\n",i,normalMode[i][0],normalMode[i][1],normalMode[i][2],max(normalMode[i])); 
  printf("\nSuperMode Triplets\n");
  for(int i=0;i<=30;i++)
    printf("%2d: %d %d %d MAX:%d\n",i,superMode[i][0],superMode[i][1],superMode[i][2],max(superMode[i]));
  */
  freopen("B-small-attempt3.in","r",stdin);
  freopen("out.txt","w",stdout);
  scanf("%d",&T);
  int N_googlers[T],S[T],P[T],points[T][10];
  for(int i=0;i<T;i++)
  {
    scanf("%d%d%d",&N_googlers[i],&S[i],&P[i]);
    for(int w=0;w<N_googlers[i];w++)
      scanf("%d",&points[i][w]);
  }
  
  /*printf("\nInput\n");
  printf("%d\n",T);
  for(int i=0;i<T;i++)
  {
    printf("%d %d %d ",N_googlers[i],S[i],P[i]);
    for(int w=0;w<N_googlers[i];w++)
      printf("%d ",points[i][w]);
    printf("\n");
  }*/
  for(int i=0;i<T;i++)
  {
    if(S[i]==0)
    {
      for(int w=0;w<N_googlers[i];w++)
      {     
	if( max(normalMode[points[i][w]]) >=P[i] )
	  ans[i]++;
      }
    }
    else
    {
      //initially no[] and su[] contains all zeros
      for(int w=0; w<N_googlers[i];w++)
	no[w]=su[w]=sol[w]=0;
      for(int w=0; w<N_googlers[i];w++)
      {
	no[w]=max(normalMode[points[i][w]]);
	su[w]=max(superMode[points[i][w]]);
	//printf("\nNormal MAx: %d superMode MAx:%d best:%d",no[w],su[w],P[i]);
      }
      int w=0;
      while(S[i] && (w<N_googlers[i]))
      {
	//printf("\nw=%d\n",w);
	if(su[w]>= P[i])
	{
	  //printf("\n w=%d \n",w);
	  if(no[w]>= P[i])
	  {
	    w++;
	    continue;
	  }
	  ans[i]++;
	  sol[w]++;
	  S[i]--;
	}
	w++;
      }
      /*printf("\nSuperMode answers\n");
      for(int w=0;w<N_googlers[i];w++)
	printf("%d ",sol[w]);
      */
      for(int w=0; w<N_googlers[i];w++)
      {
	if(!sol[w])
	  if(no[w]>= P[i])
	  {
	      ans[i]++;
	      sol[w]++;
	  }
      }
     /* for(int w=0; w<N_googlers[i];w++)
      {
	if(S[i])
	{
	  if(su[w]>=P[i] && (!sol[w]))
	    ans[i]++;
	  S[i]--;
	}
      }*/
    
	    
	    
	    
    }
    printf("Case #%d: %d\n",i+1,ans[i]);
  }
  return 0;
}
int max(int p[])
{
  int val=p[0];
  for(int i=1;i<3;i++)
    if(val<p[i])
      val=p[i];
  return val;  
}
