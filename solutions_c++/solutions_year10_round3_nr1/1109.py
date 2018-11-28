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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    int i, T;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for(i=0;i<T;i++)
    {
                   printf("Case #%d: ",i+1);
                   int j, k, N, out=0, A[1000], B[1000];
                   scanf("%d%",&N);
                   for(j=0;j<N;j++)
                   scanf("%d%d",&A[j],&B[j]);
                   for(j=0;j<N;j++)
                            for(k=j+1;k<N;k++)
                            {
                                              int s=(A[j]-A[k])*(B[j]-B[k]);
                                              if(s<0)
                                              out++;
                            }
                   printf("%d",out);
                   printf("\n");
    }
    return 0;
}
