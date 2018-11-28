#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int k=1,N;
    scanf("%d",&N);
    while (k <= N)
    {
          int n;
          scanf("%d",&n);
          pair<int,int> p[n+3];
          for (int i = 0; i < n; i++)
              scanf("%d %d",&p[i].first,&p[i].second);
          sort(p,p+n);
          int hasil = 0;
          for (int i = 0; i < n; i++)
              for (int j = 0; j < i; j++)
                  if (p[i].second < p[j].second) hasil++;
          printf("Case #%d: %d\n",k,hasil);
          k++;
    }
    return 0;
}
