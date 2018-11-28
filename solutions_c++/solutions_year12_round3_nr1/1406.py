#include <stdio.h>
#include <iostream>
#include <set>
using namespace std;

// enum shade {RED, BLUE, EMPTY};
// shade grid[100][100];
int T, N;

int graph[1001][1001];
bool marked[1001];
int edges, vertices;

// void dfs(int v)
// {
//   if(marked[v]) return;
//   vertices ++;
//   marked[v] = true;
//   int i,j,k;
//   for(i=1;i<=N;i++)
//     if(i!=v && graph[i][v])
//       {
// 	edges ++;
// 	if(!marked[i]) 
// 	  dfs(i);
//       }
// }

bool dfs (int v)
{
  marked[v]=true;
  int i,j,k;
  for(i=1;i<=N;i++)
    if(graph[v][i])
      {
	if (marked[i]) 
	  return true;
	else 
	  {
	    if(dfs(i)) return true;
	  }
      }
  return false;
}      
      

bool solve()
{
  int i,j,k,l;

  for(i=1;i<=N;i++)
    {
      edges = 0;
      vertices = 0;

      for(j=1;j<=N;j++) 
      	marked[j] = false;

      if(dfs(i)) 
	return true;
      // if(edges && edges != 2*(vertices-1)) return false;
      
    }
  return false;
}



int main()
{
  cin >> T;
  int i, j, k, l, temp;
  for (i=0;i<T;i++)
    {
      cin >> N ;
      for(j=0;j<N;j++) 
	{
	  for(k=1;k<=N;k++)
	    {
	      graph [k][j+1] =0;
	      //	      graph [j+1][k] =0;
	    }
	}
      for(j=0;j<N;j++) 
	{
	  cin >> l;
	  for(k=0;k<l;k++)
	    {
	      cin >> temp ;
	      //	      graph [temp][j+1] =1;
	           graph [j+1][temp] =1;
	    }
	  
	}

      cout << "Case #" << i+1 << ": " << (solve()?"Yes":"No") << endl;
    }
}
