#include<iostream>
#include<vector>
using namespace std;

vector<int> Ma[128];
vector<int> UM[128];
bool mal[16];
int N, M;

bool Check(int a)
{
     int i;
     for(i = 0; i < Ma[a].size(); ++i)
         if(mal[Ma[a][i]] == 1) 
                return 1;
     for(i = 0; i < UM[a].size(); ++i)
         if(mal[UM[a][i]] == 0)
                return 1;
     return 0;
}

bool process()
{
     int i;
     for(i = 1; i <= M; ++i)
         if(!Check(i)) return 0;
     return 1;
}

bool C(int a, int b)
{
     if(a > N)
     { if(b == 0)
          if(process()) return 1;
     
          return 0;
     }
     if(b < 0) return 0;
     mal[a] = 1;
     if(C(a + 1, b - 1)) return 1;
     mal[a] = 0;
     if(C(a + 1, b)) return 1;
     return 0;
}
bool OK(int n)
{
     memset(mal, 0, sizeof(mal));
     if(C(1, n)) return 1;
     return 0;
}

int main()
{
    int C, ctr = 0, i, a, b, t;
    freopen("B_S.in", "r", stdin);
    freopen("B_S.out", "w", stdout);
    scanf("%d", &C);
    while(C--)
    {
        scanf("%d%d", &N, &M);
        memset(mal, 0, sizeof(mal));
        for(i = 1; i <= M; ++i)
        {
              scanf("%d", &t);
              Ma[i].clear();
              UM[i].clear();
              while(t--)
              {
                  scanf("%d%d", &a, &b);
                  if(b) Ma[i].push_back(a);
                  else UM[i].push_back(a);
              }
        }
        for(i = 0; i <= N; ++i)
        {
            if(OK(i)) break;
        }
        printf("Case #%d:", ++ctr);
        if(i > N) printf(" IMPOSSIBLE\n");
        else
        {
            for(i = 1; i <= N; ++i)
                 printf(" %d", mal[i]);
            printf("\n");
        }
    }
} 
/*
1000
5
3
1 1 1
2 1 0 2 0
1 5 0
1
2
1 1 0
1 1 1

*/
