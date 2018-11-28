#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <vector>
#include <list>
#include <algorithm>

typedef unsigned long long ull;

#define OR 0
#define AND 1
#define FALSE 0
#define TRUE 1

using namespace std;

#define INF 10002

typedef struct node
{
  int value;
  int type;
  bool changeable;
  bool val0;
  bool val1;
  int val0c;
  int val1c;
  ull val[2];
} node;

node tree[10000];

ull min(ull a, ull b)
{
  if (a<b)
    return a;
  else
    return b;
}

/*
int solve(int node, int value)
{
  int ret;
  if (tree[node].value==-1)
    {
      if (tree[node].type==AND)
	{
	  if (value==FALSE)
	    {
	    }
	  if (value==TRUE)
	    {
	      return solve(2*node+1, TRUE)+solve(2*node+2, TRUE);
	    }
	}
      else
	{
	  if (value==FALSE)
	    {
	      return solve(2*node+1, TRUE)+solve(2*node+2, TRUE);
	    }
	  if (value==TRUE)
	    {
	    }
	}
    }
  else
    {
      if (tree[node].value==value)
	return 0;
      else
	return -1;
    }
}
*/

int main()
{
  int _N;
  cin >> _N;

  int M,V;
  int sol;

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ": ";

      cin >> M >> V;

      int G,C,I;
      for (int i=0; i<(M-1)/2; i++)
	{
	  cin >> tree[i].type >> C;
	  tree[i].changeable=(C==1);
	  tree[i].value=-1;
	  tree[i].val[0]=INF;
	  tree[i].val[1]=INF;
	}
      for (int i=0; i<(M+1)/2; i++)
	{
	  cin >> tree[i+(M-1)/2].value;
	  tree[i+(M-1)/2].val[tree[i+(M-1)/2].value]=0;
	  tree[i+(M-1)/2].val[1-tree[i+(M-1)/2].value]=INF;

	}

      sol = 0;

      for (int i=(M-1)/2-1; i>=0; i--)
	{
	  if (tree[i].value==-1)
	    {
	      if (tree[i].type==AND)
		{
		  tree[i].val[TRUE]=tree[2*i+1].val[TRUE]+tree[2*i+2].val[TRUE];
		  tree[i].val[FALSE]=min(min(tree[2*i+1].val[TRUE]+tree[2*i+2].val[FALSE],tree[2*i+1].val[FALSE]+tree[2*i+2].val[TRUE]),tree[2*i+1].val[FALSE]+tree[2*i+2].val[FALSE]);
		  if (tree[i].changeable)		
		    {
		      tree[i].val[TRUE]=min(tree[i].val[TRUE],min(min(tree[2*i+1].val[TRUE]+tree[2*i+2].val[FALSE],tree[2*i+1].val[FALSE]+tree[2*i+2].val[TRUE]),tree[2*i+1].val[TRUE]+tree[2*i+2].val[TRUE])+1);
		      tree[i].val[FALSE]=min(tree[i].val[FALSE],tree[2*i+1].val[FALSE]+tree[2*i+2].val[FALSE]+1);
		      /*
		      if (tree[i].val[TRUE]>=INF)
			{
		  tree[i].val[TRUE]=min(min(tree[2*i+1].val[TRUE]+tree[2*i+2].val[FALSE],tree[2*i+1].val[FALSE]+tree[2*i+2].val[TRUE]),tree[2*i+1].val[TRUE]+tree[2*i+2].val[TRUE])+1;
			}
		      if (tree[i].val[FALSE]>=INF)
			{
			  tree[i].val[FALSE]=tree[2*i+1].val[FALSE]+tree[2*i+2].val[FALSE]+1;
			}
		      */
		    }
		}
	      else
		{
		  tree[i].val[FALSE]=tree[2*i+1].val[FALSE]+tree[2*i+2].val[FALSE];
		  tree[i].val[TRUE]=min(min(tree[2*i+1].val[TRUE]+tree[2*i+2].val[FALSE],tree[2*i+1].val[FALSE]+tree[2*i+2].val[TRUE]),tree[2*i+1].val[TRUE]+tree[2*i+2].val[TRUE]);
		  if (tree[i].changeable)		
		    {
		      tree[i].val[FALSE]=min(tree[i].val[FALSE],min(min(tree[2*i+1].val[TRUE]+tree[2*i+2].val[FALSE],tree[2*i+1].val[FALSE]+tree[2*i+2].val[TRUE]),tree[2*i+1].val[FALSE]+tree[2*i+2].val[FALSE])+1);
		      tree[i].val[TRUE]=min(tree[i].val[TRUE],tree[2*i+1].val[TRUE]+tree[2*i+2].val[TRUE]+1);
		      /*
		      if (tree[i].val[TRUE]>=INF)
			{
			  tree[i].val[TRUE]=tree[2*i+1].val[TRUE]+tree[2*i+2].val[TRUE]+1;
			}
		      if (tree[i].val[FALSE]>=INF)
			{
			  tree[i].val[FALSE]=min(min(tree[2*i+1].val[TRUE]+tree[2*i+2].val[FALSE],tree[2*i+1].val[FALSE]+tree[2*i+2].val[TRUE]),tree[2*i+1].val[FALSE]+tree[2*i+2].val[FALSE])+1;
			}
		      */
		    }

		}
	    }
	  else
	    {
	      //	      tree[(i-1)/2].val[tree[i].value]=0;
	    }
	}

      if (tree[0].val[V]>=INF)
	cout << "IMPOSSIBLE";
      else
	cout << tree[0].val[V];

      cout << endl;
    }

  return 0;
}
