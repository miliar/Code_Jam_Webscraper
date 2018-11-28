#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

int max(int a,int b)
{

  return( a < b ? a : b);
}

int main(void)
{

  vector<int> on;  // int型の動的配列
  vector<int> bn;  // int型の動的配列

  vector<char> cn;  // int型の動的配列
  int t;
  int p,temp,n;
  char c;
  int o=0,b=0;
  int op=1,bp=1;
  int i,k;
  int count=1;

  scanf("%d",&t);

  for(i=0;i<t;i++)
    {
      scanf("%d", &n);
      for(k=0;k<n;k++)
	{
	  scanf(" %c",&c);
	  //	  printf("c == %c\n",c);
	  cn.push_back(c);
	  if(c == 'O')
	    {
	      scanf(" %d",&temp);
	      //  printf("o temp = %d\n",temp);
	      on.push_back(temp);

	    }else
	    {
	      scanf(" %d",&temp);
	      //      printf("b temp = %d\n",temp);
	  
	      bn.push_back(temp);

	    }

	}
      int r=0;

      if(bn[0]>1 || on[0]>0)
	count--;

      while(1)
	{
	  //	  printf("before : bp = %d op = %d r = %d cn = %c\n",bp,op,r,cn[r]);
	  if(cn[r]=='B')
	    {
	      if(bn[b]==bp)
		{
		    r++;
		    b++;
		}
	      else if(bn[b]>bp)
		{
		    bp++;
		}
	      else
		{
		    bp--;
		}
	      if(op<on[o])
		op++;
	      else if(op>on[o])
		op--;
	      count++;
	      
	    }
	  else if(cn[r]=='O')
	    {
	      if(on[o]==op)
		{
		  r++;
		  o++;
		}
	      else if(on[o]>op)
		{
		  op++;
		}
	      else
		op--;

	      count++;
	      if(bp<bn[b])
		bp++;
	      else if(bp>bn[b])
		bp--;
	      
	    }
	  //	  printf("after : bp = %d op = %d r = %d\n\n\n",bp,op,r);

	  if(r >= cn.size())
	    break;
	}

      printf("Case #%d: %d\n",i+1,count);
      op=1;bp=1;
      o=0;b=0;
      count=1;
      cn.clear();

      bn.clear();
      on.clear();



    }
  return(0);
}
