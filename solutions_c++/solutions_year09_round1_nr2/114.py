#include <iostream>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <functional>

using namespace std;

typedef __int64 i64;

const int QUEUESIZE = 131072;
const int MAXN = 32;
const int To[4][4][3] = {
   { {0, 0, 2},   {0, 1, 1},    {1, 0, 2},    {0, 0, 1} },    
   { {0, 0, 3},    {0, 0, 0},    {1, 0, 3},   {0, -1, 0} },    
   {  {-1, 0, 0},    {0, 1, 3},    {0, 0, 0},    {0, 0, 3} }, 
   {  {-1, 0, 1},    {0, 0, 2},    {0, 0, 1},    {0, -1, 2} }
};

int N, M;
i64 S[MAXN][MAXN], W[MAXN][MAXN], T0[MAXN][MAXN], Time[MAXN][MAXN][4];

struct Node
{
       int y, x, c;
       i64 t;
	   Node(int _y = 0, int _x = 0, int _c = 0, i64 _t = 0) : y(_y), x(_x), c(_c), t(_t){}

}que[QUEUESIZE];


int front, rear;

i64 NextG(int y, int x, i64 t, int d)
{
	i64 dt, kt;
    bool flag;
    if(d == 0 || d == 2) 
		flag = 1;
    else
		flag = 0;
    
    
    if(flag == true)
    {
        dt = t - T0[y][x];
        dt %= (S[y][x] + W[y][x]);
        if(dt < S[y][x]) 
              kt = 0;
        else 
            kt = S[y][x] + W[y][x] - dt; 
       
    }
    else
    {
        dt = t - T0[y][x];
        dt %= (S[y][x] + W[y][x]);
        
        if(dt >= S[y][x]) 
              kt = 0;
        else 
            kt = S[y][x] - dt;
    }
    return t + kt;
}

bool GetNext(Node c, int d, Node& ne)
{
    ne.y = c.y + To[c.c][d][0];
    ne.x = c.x + To[c.c][d][1];
    ne.c = To[c.c][d][2];
    if(ne.y < 1 || ne.y > N || ne.x < 1 || ne.x > M) return 0;
    
    if(!(ne.y == c.y && ne.x == c.x))
    {
            ne.t = c.t + 2;
            return 1;
    }
    
    ne.t = NextG(ne.y, ne.x, c.t, d);
    ne.t += 1;
    return 1;
}

i64 BFS()
{
    front = rear = 0;
    que[rear++] = Node(N, 1, 1, 0);
    Time[N][1][1] = 0;
	memset(Time, 63, sizeof(Time));
    Node cur, ne;
    int d;
    while(front != rear)
    {
        cur = que[front++];
        front %= QUEUESIZE;
        
        for(d = 0; d < 4; ++d)
        {
              if(GetNext(cur, d, ne))
              {
                  if(ne.t < Time[ne.y][ne.x][ne.c])
                  {
                          Time[ne.y][ne.x][ne.c] = ne.t;
                          que[rear++] = ne;
                          rear %= QUEUESIZE;
                  }
              }
              
        }
    }
    return Time[1][M][2];
}
int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);

    int tt, t, j, i;
    scanf("%d", &t);

    for(tt = 1; tt <= t; ++tt)
    {
       scanf("%d%d", &N, &M);  
       for(i = 1; i <= N; ++i)
       {
           for(j =1; j <= M; ++j) 
           {
                 scanf("%I64d%I64d%I64d", &S[i][j], &W[i][j], &T0[i][j]);
                 T0[i][j] -= (S[i][j] + W[i][j]) * 100000000;
           }
       }    
       printf("Case #%d: %I64d\n", tt, BFS());
    }
}
