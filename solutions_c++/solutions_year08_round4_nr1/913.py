#include<stdio.h>
#define MAX 99999999

typedef struct{
   int g;//0==OR 1==AND -1==leaf
   int c;//1==changable 
   int cost;
   int output;
}Tree;
 
Tree tree[10005]; 

int FindO(int now,int M)
{
    if(tree[now].g==-1)
	{
	//	printf("%d %d\n",now+1,tree[now].output);
		return tree[now].output;
	}
    else 
	{
        int l,r;
		l=FindO((now+1)*2-1,M);
		r=FindO((now+1)*2,M);
        if(tree[now].g==0)
		{
           if(l==1||r==1)
		      tree[now].output=1;
		   else
			  tree[now].output=0;
		}
		else 
		{
           if(l==1&&r==1)
		      tree[now].output=1;
		   else
			  tree[now].output=0;
		}
	   // printf("%d %d\n",now+1,tree[now].output);
		return tree[now].output;
	}
}

int FindMin(int i,int M,int V)
{
    if(tree[i].output==V)
		return 0;
/*
	if(tree[i].c==1)
	{
        int l=(now+1)*2-1;
		int r=(now+1)*2;

        if(tree[l].output+tree[r].output==1)
			return 1; 
	}
*/
   
    if(tree[i].g==-1)
		return MAX;
	else 
	{
      int l=(i+1)*2-1;
	     int r=(i+1)*2;

	int l0= FindMin(l,M,0);
    int l1=FindMin(l,M,1);

	int r0= FindMin(r,M,0);
    int r1=FindMin(r,M,1);
    int min;


     if(tree[i].g==0)
	 {
   

        if(tree[i].output==0)
		{
           min=l0+r1;
		   min=min>l1+r0?l1+r0:min;
           min=min>l1+r1?l1+r1:min;
          
		}
		else if(tree[i].output==1)
		{
           min=l0+r0;
           if(tree[i].c==1)
		   {
               min=min>l1+r0+1?l1+r0+1:min;
               min=min>l0+r1+1?l0+r1+1:min;
		   }

		}
	}
	else if(tree[i].g==1)
	{
      
        if(tree[i].output==1)
		{
           min=l0+r1;
		   min=min>l1+r0?l1+r0:min;
           min=min>l0+r0?l0+r0:min;
          
		}
		else if(tree[i].output==0)
		{
           min=l1+r1;
		   
		   if(tree[i].c==1)
		   {
               min=min>l1+r0+1?l1+r0+1:min;
               min=min>l0+r1+1?l0+r1+1:min;
		   }

		}

	}
	// printf("(%d %d %d)\n",i+1,V,min>MAX?MAX:min);
     return min>MAX?MAX:min;
	}
}

int main()
{
 // freopen("A-small-attempt0.in.txt","r",stdin);
  // freopen("A-small-attempt0.out.txt","w",stdout);
     freopen("A-large.in.txt","r",stdin);
     freopen("A-large.out.txt","w",stdout);


  int N,M,i,j,p,V;
  
  scanf("%d",&N);
  for(p=0;p<N;p++)
  {
      scanf("%d%d",&M,&V);
  

  for(i=0;i<M;i++)
  {
	  if((i+1)*2<=M)
	  {
          scanf("%d%d",&tree[i].g,&tree[i].c);
          
	  }
	  else
	  {
          scanf("%d",&tree[i].output);
		  tree[i].c=0;
		  tree[i].g=-1;
	  }
  }
  FindO(0,M);

  int result=FindMin(0,M,V);
  if(result==MAX)
	  printf("Case #%d: IMPOSSIBLE\n",p+1);
  else
	  printf("Case #%d: %d\n",p+1,result);

  }
}