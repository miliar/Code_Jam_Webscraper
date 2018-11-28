#include<cstdio>
#include<algorithm>
#include<queue>
#include<iostream>
#include<cstring>
using namespace std;

inline int Rint(){ int x; scanf("%d", &x); return x; }
inline int Rstr(){ char str[10]; scanf("%s", str); return str[0] == 'B';}
class tt
{
    public:
        int x, y, z;
        tt( int _x, int _y, int _z ):
            x(_x), y(_y), z(_z){};
};

const int maxn = 110;
int n;
int a[maxn], b[maxn];

int d[maxn][100 + 1][100 + 1];
int work()
{
    for( int i = 0; i <= n; ++ i )
         for( int j = 0; j <= 100; ++ j )
              for( int k = 0; k <= 100; ++ k )
                   d[i][j][k] = -1;
    d[0][1][1] = 0;
    queue< tt > Q;
    Q.push(tt(0, 1, 1));
    while( !Q.empty() )
    {
            tt now = Q.front(); Q.pop();
            int id = now.x;
            if( id == n ) return d[id][now.y][now.z];
            // 1
            if( a[id + 1] == 0 )
            {
                if( now.y == b[id + 1] )
                {
                    int del = d[now.x][now.y][now.z] + 1;
                    for( int i = -1; i <= 1; ++ i )
                    {
                        int y = now.y;
                        int z = now.z + i;
                        if( z <= 0 || z > 100 )continue;
                        if( d[id+1][y][z] == -1 )
                        {
                            d[id+1][y][z] = del;
                            Q.push(tt(id+1, y, z));
                        }
                    }
                }
            }
            // 2
            if( a[id + 1] == 1 )
            {
                if( now.z == b[id + 1] )
                {
                    int del = d[now.x][now.y][now.z] + 1;
                    for( int i = -1; i <= 1; ++ i )
                    {
                         int y = now.y + i;
                         int z = now.z;
                         if( y <= 0 || y > 100 )continue;
                         if( d[now.x+1][y][z] == -1 )
                         {
                             d[now.x+1][y][z] = del;
                             Q.push(tt(now.x+1, y, z));
                         }
                    }
                }
            }
            for( int i = -1; i <= 1; ++ i )
                 for( int j = -1; j <= 1; ++ j )
                 {
                      int y = now.y + i;
                      int z = now.z + j;
                      if( y <= 0 || y > 100 )continue;
                      if( z <= 0 || z > 100 )continue;
                      if( d[id][y][z] == -1 )
                      {
                          d[id][y][z] = d[now.x][now.y][now.z] + 1;
                          Q.push(tt(id, y, z));
                      }
                 }
    }
    return -1;
}
  

int main()
{
    int Tcase = Rint();
    while( Tcase -- )
    {
           n = Rint();
           for( int i = 1; i <= n; ++ i )
           {
                a[i] = Rstr();
                b[i] = Rint();
           }
           static int o = 1;
           printf("Case #%d: %d\n",o ++, work());
    }
    return 0;
}
