#include <cstdio> 
#include <cstring> 
#include <algorithm> 
using namespace std; 
const int size= 800; 
 __int64 x[size], y[size]; 

int main() 
{ 
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
   int n; 
   int i; 
  int m,j;
  int T, t;
  __int64 cost;
  scanf("%d", &T);
  for (t=1; t <= T; t++)
  { 
      scanf("%d",&n);
      for (i= 0; i < n; i++)
      {
          scanf("%I64d", x + i);
      }     
      sort(x, x+n);
       
      for (i= 0; i < n; i++)
      {
          scanf("%I64d", y + i);

      }
      sort(y, y + n); 
      cost = 0; 
      for (i = 0; i < n; i++)
      {
              cost += x[i] * y[n-1-i]; 

      }
          
      printf("Case #%d: %I64d\n", t, cost);
  }
  return 0;
}


