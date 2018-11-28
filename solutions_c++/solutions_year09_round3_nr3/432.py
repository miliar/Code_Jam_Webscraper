#include <iostream>
#include <cstdio>
using namespace std;

int pris[101], P, Q;

bool empty[101];

int solve()
{
 int ans = -1;
 do {    
  memset(empty, 0, sizeof(empty));  
    
  int cur = 0;
  
  for (int i = 0; i < Q; i++)
  {
   empty[pris[i]] = true;
   
   int l = pris[i] - 1;
   while (l >= 1 && !empty[l])
   {
    cur++;
    l--;
   }
   
   int r = pris[i] + 1;
   while (r <= P && !empty[r])
   {
    cur++;
    r++;
   }
  }
  
  if (cur < ans || ans == -1)
   ans = cur;
  
 } while (next_permutation(pris, pris + Q));
 
 return ans;
}

int main()
{
 int T;
 scanf("%d", &T);
 
 for (int t = 0; t < T; t++)
 {
  scanf("%d%d", &P, &Q);
  for (int i = 0; i < Q; i++)
   scanf("%d", &pris[i]);
   
  sort(pris, pris + Q);
  
  printf("Case #%d: %d\n", t + 1, solve());
 }
 
 return 0;
}
