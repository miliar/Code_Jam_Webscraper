#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <stack>
#include <cmath>
#include <deque>
#include <stack>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define maxn 110
#define datat int
#define ansdatat int

int m,n,h[maxn][maxn], mark[maxn*maxn],tt,
    color,col[maxn*maxn],fa[maxn*maxn];
int dx[4] = {-1,0,0,1},
    dy[4] = {0,-1,1,0};

void init_deal(){
     tt++;
     for (int i = 1;i<=m*n;i++)
         fa[i] = i;
}

int get_num(int a, int b){
    return (a-1)*n+b;
}

bool check(int x,int y){
     return 1<=x && x<=m &&
            1<=y && y<=n;
}

int find_(int v){
    if (fa[v] == v) return v;
    else{
         int r = find_(fa[v]);
         fa[v] = r;
         return r;
    }
}

void add_(int a,int b){
     int r1 = find_(a),
         r2 = find_(b);
     if (r1 != r2)
        fa[r1] = r2;
}

int main(){
	
	int tttt;
	scanf("%d", &tttt);
	int ttt = 0;
	while (tttt-->0){
          ttt++;
          scanf("%d%d", &m, &n);
          init_deal();
          for (int i = 1;i<=m;i++)
          for (int j = 1;j<=n;j++){
              scanf("%d", &h[i][j]);
          }
          for (int i = 1;i<=m;i++)
          for (int j = 1;j<=n;j++){
              int lo = 1000000,px,py;
              for (int k = 0;k<4;k++){
                  int nx = i+dx[k],
                      ny = j+dy[k];
                      
                  if (check(nx,ny) &&
                      lo > h[nx][ny]){
                      lo = h[nx][ny];
                      px = nx;
                      py = ny;
                  }
              }
              if(h[i][j]>lo){
                 int n1, n2;
                 n1 = get_num(i,j);
                 n2 = get_num(px,py);
                 add_(n1,n2);
              }
          }
          
          int color = 0;
          for (int i = 1;i<=m;i++)
          for (int j = 1;j<=n;j++){
              int n1 = get_num(i,j),r1;
              r1 = find_(n1);
              if (mark[r1] != tt){
                  mark[r1] = tt;
                  col[r1] = color;
                  color++;
              }
          }
          
          printf("Case #%d:\n", ttt);
          for (int i = 1;i<=m;i++){
              for (int j = 1;j<=n;j++){
                  int n1 = get_num(i,j),r1;
                  r1 = find_(n1);
                  printf("%c", 'a'+col[r1]);
                  
                  if (j!=n) printf(" ");
              }
              printf("\n");
          }
          
          
    }

	

	return 0;
};

