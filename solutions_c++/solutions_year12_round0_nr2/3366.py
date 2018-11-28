
#include<cstdio>
#include<iostream>
#include<string>

#define MAX_VALUE 31

int max[MAX_VALUE];
int max_st[MAX_VALUE];

int main(void)
{
  int test_count;
  int N,S,p,data,max_best;
  int r,q;  //remainder and quotient
  int i,j;

  max[0] = 0;
  max[1] = -1;
  for(i=1;i<(MAX_VALUE-2);i++)
  {
    q=i/3;
    r=i%3;
    if(r == 0)
    {
      max[i] = q;
      max_st[i] = q+1;
    }
    else if(r == 1)
    {
      max[i] = q+1;
      max_st[i] = -1;
    }
    else if(r == 2)
    {
      max[i] = q+1;
      max_st[i] = q+2;
    }
  }
  max[i] = 10; max_st[i] = -1;
  i++;
  max[i] = 10; max_st[i] = -1;

/*  for(i=0;i<MAX_VALUE;i++)
  {
    printf("Index %d: %d, %d\n",i,max[i],max_st[i]);
  } */
  scanf("%d",&test_count);

  for(i=0;i<test_count;i++)
  {
    max_best = 0;
    printf("Case #%d: ",i+1);
    scanf("%d %d %d",&N,&S,&p);
    if(p == 0)
    {
      for(j=0;j<N;j++)
      {
        scanf("%d",&data);
      }
      printf("%d\n",N);
    }
    else
    {
      for(j=0;j<N;j++)
      {
        scanf("%d",&data);
        if(max[data] >= p) 
        { 
          max_best++;
        }
        else if((max_st[data] >= p) && (S != 0))
        {
          S--;
          max_best++;
        } 
      }
      printf("%d\n",max_best);
    }
  }
return 0;
}
            
