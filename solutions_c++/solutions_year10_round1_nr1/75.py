#include<iostream>
using namespace std;

char M[128][128];
int X[4] = {1, 1, 0, -1};
bool Red, Blue;

int Y[4]= {0, 1, 1, 1};
int N, K;

void input(){
    
       scanf("%d%d", &N, &K);   
      // printf("%d", &N); 
         for(int i = 1; i <= N; ++i)
            scanf("%s", M[i] + 1);
}

bool checkOne(char c)
{
     int i, j, k, d;
     int y, x;
     for(i = 1; i <= N;++i)
       for(j = 1; j <= N; ++j) for(d = 0; d < 4; ++d)
       {
           y = i, x = j;
           for(k = 1; k <= K; ++k)
           {
               if(y < 1 || y > N || x < 1 || x > N) break;
               if(M[y][x] != c) break;
               y += Y[d];
               x += X[d];
           }
           if(k > K) return 1;
       }
       return 0;
}


void solve(){
       for(int i = 1; i <=N; ++i)
         {
             int k = N;
             for(int j = N; j >= 1; --j)
                 if(M[i][j] != '.')
                     M[i][k--] = M[i][j];
             for(int j = k; j >= 1; --j)
                 M[i][j] = '.';
         }
         
         Red=false, Blue=false;
         if(checkOne('R')) Red = true;
         if(checkOne('B')) Blue = true;
     }
int main()
{
    int t, caseT = 0;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    while(t--){
         input();
         solve();
         printf("Case #%d: ", ++caseT);
         if(Red && Blue)
              printf("Both\n");
         else if(Red)
               printf("Red\n");
           else if(Blue)
                printf("Blue\n");
             else
                printf("Neither\n");
    }
}
