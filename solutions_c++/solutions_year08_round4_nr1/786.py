#include <iostream>
#define MAX 10123
#define INF 999999
#define neg(a) ((a) ? (0) : (1))
using namespace std;

typedef struct node
{
  int c, g;
  int i;
}Node;

Node tree[MAX];
int memo[2][MAX];

bool is_leaf(int n, int m)
{
  return ((n+1) > (m - 1)/2);
}

int get_min(int v, int n, int m)
{
  // printf("[%d][%d][%d]\n", v, n + 1, m);
  // if(is_leaf(n, m)) printf("aqui\n");
  // if(memo[v][n] != -1) return memo[v][n];
  if(n > m) return INF;
  if(is_leaf(n, m) && v == tree[n].i) return memo[v][n] = 0;
  if(is_leaf(n, m) && v != tree[n].i) return memo[v][n] = INF;
  
  if(tree[n].c == 0) // CANT CHANGE
    {
      // printf("[cant change %d][g = %d][c = %d]\n", n + 1, tree[n].g,
// 	     tree[n].c);
      if(tree[n].g  == 0) //OR GATE
	{
	  if(v == 0) return memo[v][n] = get_min(0, 2*n + 1, m) +
		       get_min(0, 2*n + 2, m);
	  else return memo[v][n] = 
		 min(get_min(1, 2*n + 1, m), get_min(1, 2*n + 2, m));
	}
      else //AND GATE
	{
	  if(v == 1) return memo[v][n] = get_min(1, 2*n + 1, m) +
		       get_min(1, 2*n + 2, m);
	  else return memo[v][n] = 
		 min(get_min(0, 2*n + 1, m), get_min(0, 2*n + 2, m));
	}
    }
  else //CAN CHANGE
     {
       // printf("[can change %d][g = %d][c = %d]\n", n + 1, tree[n].g,
// 	     tree[n].c);
      tree[n].c = 0;
      int m1 = get_min(v, n, m);
      // printf("[%d] -> [%d]\n", tree[n].g ,neg(tree[n].g));
      tree[n].g = neg(tree[n].g);
      int m2 = get_min(v, n, m) + 1;
      // printf("[can change %d][%d][%d]\n", n + 1, m1, m2);
      tree[n].c = 1;
      tree[n].g = neg(tree[n].g);
      // if(m1 < m2) printf("didnt change %d\n", n + 1);
//       else printf("changed %d\n",n + 1);
      return memo[v][n] = min(m1, m2);
    }
  return INF;
}


int main(int argc, char *argv[]){
  int n, m, v, t = 1;
  
  scanf("%d",&n);
  
  while(n--)
    {
      scanf("%d %d", &m, &v);

      for(int i = 0; i < (m-1)/2; i++)
	scanf("%d %d", &(tree[i].g), &(tree[i].c));
      
      for(int i = (m-1)/2; i < m; i++)
	scanf("%d",&(tree[i].i));
      
      // for(int i = 0; i < m; i++) printf("%d %d\n",i + 1, is_leaf(i, m));
//       exit(1);
					
      for(int i = 0; i < m; i++) memo[0][i] = memo[1][i] = -1;
      // for(int i = 0; i < m; i++)
      // 	{
      // 	  if(i < (m-1)/2) printf("[%d %d]\n", (tree[i].g), (tree[i].c));
      // 	  else printf("(%d)\n",(tree[i].i));
      // 	}

      m = get_min(v, 0, m);      
      printf("Case #%d: ", t++);
      if(m >= INF) printf("IMPOSSIBLE\n");
      else printf("%d\n", m);
      // printf("3: %d\n6: %d\n", get_min(0, 2, m), get_min(0, 5, m));sx
    }
  
  return 0;
}
