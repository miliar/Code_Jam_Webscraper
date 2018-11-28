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
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int i, j, T, N, K, s;
	scanf("%d",&T);
	for (i=0;i<T;i++)
	{
        scanf("%d%d",&N,&K );
        for(j=0,s=1;j<N;j++)
              s*=2;
        for(j=s;j<K+2;j+=s)
              if(j==K+1)
              break;
        if(j==K+1)
        {
              printf("Case #%d: ", i+1);
              printf("ON");
              printf("\n");
        }
        else
        {
              printf("Case #%d: ", i+1);
              printf("OFF");
              printf("\n");
        }
    }
return 0;
}
