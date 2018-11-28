#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>

int main()
{
	freopen("C-small-attempt4.in","r",stdin);
    freopen("C-small-attempt4.out","w",stdout);
	int i, j, m, l, s, g[10], T, N, R, k;
	scanf("%d",&T);
	for (i=0;i<T;i++)
	{
        m=0, l=0;
        scanf("%d%d%d",&R,&k,&N);
        // printf("R=%d, k=%d, N=%d\n", R, k, N);
        for(j=0;j<N;j++)
        scanf("%d",&g[j]); // for(j=0;j<N;j++) printf("%d ",g[j]); printf("\n");
        for(j=0;j<R;j++)
        {
              s=0;
              int y=l;
              for(;;l++)
              {
                     
                     if(l==N) 
                     l=0;
                     if((s>0)&&(y==l))
                     break;
                     s+=g[l]; // printf("%d ", g[l]);
                     m+=g[l];
                     if(s>k)
                     {
                         m-=g[l]; // printf("-%d ", g[l]);
                         s-=g[l];
                        // l--;  printf("%d  %d\n ", j+1,s);
                         break;
                     }
              }
        }
              printf("Case #%d: ", i+1);
              printf("%d",m);
              printf("\n");
    }
return 0;
}
