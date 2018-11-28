#include <string>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
typedef long long ll;
const ll magic = 10007;
int tst()
{
    int w;
    int h;
    cin >> h >> w;

    int r;
    cin >> r;
    ll ans = 0;
    set<pair<int,int> > in;
    ll wyn[h][w];

    bzero(wyn,sizeof(wyn));
    for(int i=0;i<r;i++)
    {
        int x,y;
        cin >> x >> y;
        x--;
        y--;
        in.insert(make_pair(x,y));
    }
    for(int x=0;x<h;x++)
        for(int y=0;y<w;y++)
        {
            if(x==0 && y==0)
            {
                wyn[x][y]=1;
                continue;
            }
            if(in.find(make_pair(x,y)) != in.end())
                continue;
            if(x>=2 && y>=1)wyn[x][y]+=wyn[x-2][y-1];
            if(x>=1 && y>=2)wyn[x][y]+=wyn[x-1][y-2];
            wyn[x][y]%=magic;
        }

    
    return wyn[h-1][w-1];

}
int main()
{
    int n;
    cin >> n;
    for(int i=0;i<n;i++)
    {
        printf("Case #%d: %d\n",i+1,tst());
    }

}
