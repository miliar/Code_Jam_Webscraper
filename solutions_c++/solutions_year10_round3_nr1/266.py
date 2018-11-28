#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
using namespace std;

pair<int,int> p[1001];
int a[100000];

int kveri( int x )
{
    int ret = 0;
    for( ; x > 0; x -= x&-x ) ret += a[x];
    return ret;
}
void dodaj( int x )
{
     for( ; x < 20000; x += x&-x ) a[x]++;
}

int main ( )
{
    int t; scanf("%d", &t);
    for(int it=0; it<t; it++)
    {
              memset( a, 0, sizeof a );
              int n; scanf("%d", &n);
              for(int i=0; i<n; i++) scanf("%d%d", &p[i].first, &p[i].second);
              sort( p, p+n );
              int s = 0;
              for(int i=n-1; i>=0; i--)
              {
                      s += kveri( p[i].second-1 );
                      dodaj( p[i].second );
              }
              printf("Case #%d: %d\n", it+1, s);
    }
    return 0;
}
