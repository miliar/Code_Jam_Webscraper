#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define MST(a,b) (memset(a,b,sizeof(a)))
#define DB(x) (cout<<#x<<": "<<x<<endl)
#define PB push_back
#define MP make_pair
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;


struct Node
{
    LL a;
};


#define KSIZE 1048575
#define HSIZE 100000000

struct HashNode
{
    LL data;
    int next;
};

HashNode Hash[HSIZE];
int pos[KSIZE+1];
int H_Top = 1;

inline int Key(LL data)
{
    
    return data & KSIZE;
}
inline int Find(LL data)
{
   int key = Key(data);
   int p = pos[key];
   while(p && Hash[p].data != data)
       p = Hash[p].next;
   return p;
}
inline void Insert(LL data)
{
   int p = Key(data);
   Hash[H_Top].data = data;

   Hash[H_Top].next = pos[p];
   pos[p] = H_Top++;
   if(H_Top > HSIZE) printf("ERROR");
}
void Init()
{
     memset(pos, 0, sizeof(pos));
     H_Top = 1;
}
#define QSIZE 1048575
LL que[QSIZE+1];
int front, rear;
char Map[16][16];
int R, C;
int N;
bool M[16][16];
bool M2[16][16];
int dx[4] = {0, 1, -1, 0};
int dy[4] = {1, 0, 0, -1};
#define IN(r,c) (0<=r && r < R && 0 <= c && c < C)
bool EMP(int y, int x)
{
     return IN(y, x) && Map[y][x] != '#' && !M[y][x];
}
bool EMP2(int y, int x)
{
     return IN(y, x) && !M[y][x];
}
bool Dan(int *r, int *c)
{
     bool S[8]={0};
     int cnt = 1;
     S[0] =1;
     int i, j, k;
     for(i = 0; i < N; ++i)
     {
         for(j = 0; j < N; ++j)
             if(S[j])
                for(k = 0; k < N; ++k)
                   if(!S[k])
                   {
                      if((r[j] == r[k] && abs(c[j] - c[k]) == 1) || (c[j] == c[k] && abs(r[j] - r[k]) == 1) )
                      {
                         S[k] = 1;
                         ++cnt;
                      }
                   }
                
     }
    return cnt < N;
     //if(N == 1) return 1;
     //return (r[0] == r[1] && abs(c[0] - c[1]) == 1) || (c[0] == c[1] && abs(r[0] - r[1]) == 1);
}
void Out(bool M[][16])
{
     int k, j;

     for(k = 0; k < R; ++k){
           for(j = 0; j < C; ++j)
           printf("%d ", M[k][j]);printf("\n");}
     printf("\n");
}
int bfs()
{
    front = rear = 0;
    int i, j, k;
    int step, re;
    int r[8], c[8], r2[8], c2[8];
    LL cur, next;
    if(N == 0) return 0;
    cur = 0;
    bool fg=0;
    for(i = 0; i < R; ++i)for(j = 0; j < C; ++j)
        if(Map[i][j] == 'o' || Map[i][j] == 'w')
        {
            cur = cur * 256 + i * 16 + j;
            if(Map[i][j] == 'w') Map[i][j] =  'x';
            if(Map[i][j] == 'o') fg = 1;
        }
    if(!fg) return 0;
    step = 0;
    bool dan;
    bool dan2;
          int d;
           int n2;
    que[rear++] = cur;
    Init();
          
    Insert(cur);
    
    while(front != rear)
    { 
         re = rear;
         ++step;
        while(front != re)
        {
           cur = que[front++];
           front &= QSIZE;
           
           memset(M, 0, sizeof(M));
           for(i = 0; i < N; ++i)   
           {
               c[i] = cur % 16;
               cur /= 16;
               r[i] = cur % 16;
               cur /= 16;
               M[r[i]][c[i]] = 1;
               //printf("%d %d, ", r[i], c[i]);
           }
           dan = Dan(r, c);
          //printf("\n");
          //Out(M);
         /* if(step == 12)
          
          {
          printf("%d", dan);
          Out(M);
          }*/
           for(i = 0; i < N; ++i)
           {
               for(d = 0; d <4; ++d)
               {
                   if(EMP(r[i]-dy[d], c[i]-dx[d]) && EMP(r[i] + dy[d], c[i] + dx[d]) )
                   {
                       memcpy(M2, M, sizeof(M));
                       M2[r[i]][c[i]] = 0;
                       M2[r[i]+dy[d]][c[i]+dx[d]] = 1;
                       
                      // Out(M2);
                       
                       n2=  0;
                       for(k = 0; k < R; ++k)for(j = 0; j < C; ++j)
                       if(M2[k][j])
                           r2[n2] = k, c2[n2++] = j;
                       
                       dan2 = Dan(r2, c2);
                       
                       //if(dan && !dan2) 
                      /* {printf("%d %d=====\n", dan, dan2);
                              Out(M);
                              Out(M2);
                       }*/
                       if(dan && dan2) 
                       {
                              //printf("=====\n");
                              //Out(M);
                              //Out(M2);
                              continue;
                       }
                        
                       next = 0;
                      // printf("ne: ");
                       for(j = 0; j < N; ++j)
                       {
                           next = next * 256 + r2[j] * 16 + c2[j];
                           //printf("%d %d, ", r2[j], c2[j]);
                       }
                      // printf("\n");
                       for(j = 0; j < N; ++j)
                           if(Map[r2[j]][c2[j]] != 'x') break;
                       if(j == N) return step;
                       if(Find(next)) continue;
                       Insert(next);
                       que[rear++] = next;
                       rear &= QSIZE;
                   }
               }
           }
           
       }
       
    }
    return -1;
}
int main()
{
	freopen("A_L.in","r", stdin);
	freopen("A_L.out", "w", stdout);

int t;
	scanf("%d", &t);
    int Case;
     
     
    int i, j, k;
    
	for(int Case = 1; Case <= t; Case++)
	{
		scanf("%d%d", &R, &C);
		for(i = 0; i < R; ++i)
		    scanf("%s", Map[i]);
        N = 0;
        for(i = 0; i < R; ++i)for(j = 0; j < C; ++j)
        if(Map[i][j] == 'o' || Map[i][j] == 'w') ++N;
        
		printf("Case #%d: %d\n", Case, bfs());


	}


	return 0;
}
/*
10
5 4
....
#..#
#xx#
#oo#
#..#
7 7
.######
.x....#
.x....#
..#oo.#
..#...#
.######
.######
7 7
#######
#x....#
#xx.o.#
#..oo.#
#.#...#
#######
#######
4 10
##########
#.x...o..#
#.x...o..#
##########
7 7
#######
#x....#
#x..o.#
#x#oo.#
#.#...#
#######
#######
3 4
.#x.
.oww
....
12 12
.xxxxx......
............
............
............
............
............
............
............
............
............
.ooooo......
............

12 12
.xxxxx......
............
............
............
............
............
............
............
............
............
....ooooo...
............
*/
