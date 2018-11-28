#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <cassert>
#include <cmath>
#include <string>
#include <set>

int main(int argc, char *argv[])
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int N;

    scanf("%d",&N);

    int CASE = 1;
    while(N--)
    {
          unsigned int n,k;
          scanf("%u %u",&n,&k);
          long long int ret = 2<<(n-1);
          unsigned int tmp = k%ret;

          if(tmp==ret-1)
              printf("Case #%d: ON\n",CASE);
          else
              printf("Case #%d: OFF\n",CASE);
          CASE++;
    }

    return 0;
}
