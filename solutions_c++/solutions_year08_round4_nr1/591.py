#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define min(a,b) ((a)<(b)?(a):(b))

int numNodes, V;
int tree[20000][2];

int findMin(int x)
{
  if (x > numNodes) { printf("problem\n"); fflush(stdout); exit(0); }

  int l, r, typ = tree[x][0];
  int lc = (2*(1+x))-1, rc = 2*(x+1);

  if (typ == -1)
  {
    if (tree[x][1] == V)
      return 0;
    return -1;
  }

  l = findMin(lc);
  r = findMin(rc);
  //printf("L %d R %d\n", l, r);
  if (l == -1 && r == -1) return -1;
  if (V == 1)
  {
    if (typ == 2 || typ == 4)
    {
      int ans = l + r;
      if (typ == 4)
        ans = min(ans, min(l,r)+1);

      if (l == -1 || r == -1)
      {
        if (typ == 4)
          ans = l+r+2;
        else
          return -1;
      }

      return ans;
    }
    else
    {
      int ans = min(l,r);
      if (l == -1 || r == -1)
        ans = l + r + 1;

      return ans;
    }
  }
  else
  {
    if (typ == 2 || typ == 4)
    {
      int ans = min(l,r);
      if (l == -1 || r == -1)
        ans = l + r + 1;

      return ans;
    }
    else
    {
      int ans = l + r;
      if (typ == 3)
        ans = min(ans, min(l,r)+1);
      
      if (l == -1 || r == -1)
      {
        if (typ == 3)
          ans = l + r + 2;
        else
          return -1;
      }

      return ans;
    }
  }

  return -1;
}

int main()
{
  int N,i,j,g,c,ans;

  scanf("%d", &N);

  for (int cs=1; cs<=N; cs++)
  {
    scanf("%d %d", &numNodes, &V);
    memset(tree, -1, sizeof(tree));

    j = (numNodes-1)/2;
    for (i=0;i<j;i++)
    {
      scanf("%d %d", &g, &c);
      tree[i][0] = 1+g+2*c;
      //printf("Node %d: %d\n", i, tree[i][0]);
    }

    for (;i<numNodes;i++)
    {
      scanf("%d", &c);
      tree[i][1] = c;
      //printf("Node: %d: %d\n", i, tree[i][1]);
    }

    ans = findMin(0);

    if (ans != -1)
      printf("Case #%d: %d\n", cs, ans);
    else
      printf("Case #%d: IMPOSSIBLE\n", cs);
  }

  return 0;
}
