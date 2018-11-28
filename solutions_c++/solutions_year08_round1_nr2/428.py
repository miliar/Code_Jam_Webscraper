/#include <iostream>
//
//using namespace std;
//
//int Vin()
//{
//	int T;
//	scanf("%d", &T);
//	for (int ctr = 1; ctr <= T; ctr++)
//	{
//		double x = 3 +sqrt(5);
//		scanf("%d", &n);
//		double ans = 1;
//		while (n > 0)
//		{
//			if (n % 2 == 0)
//			{
//				x *= x;
//				n /= 2;
//			}
//			else
//			{
//				ans *= x;
//				n -= 1;
//			}
//		}
//
//		ostream os;
//		
//
//
//	}
//	return 0;
//}

#include<iostream>
#include<vector>
using namespace std;

vector<int> V[128];
vector<int> G[128];
bool Vl[16];
int N, M;





bool nic(int a)
{
     int i;
     for(i = 0; i < V[a].size(); ++i)
         if(Vl[V[a][i]] == 1) 
                return 1;
     for(i = 0; i < G[a].size(); ++i)
         if(Vl[G[a][i]] == 0)
                return 1;
     return 0;
}

bool process()
{
     int i;
     for(i = 1; i <= M; ++i)
         if(!nic(i)) return 0;
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
     Vl[a] = 1;
     if(C(a + 1, b - 1)) return 1;
     Vl[a] = 0;
     if(C(a + 1, b)) return 1;
     return 0;
}


bool OK(int n)
{
     memset(Vl, 0, sizeof(Vl));
     if(C(1, n)) return 1;
     return 0;
}
int main()
{
    int T;
	int ctr = 0, i, a, b, t;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d%d", &N, &M);
        memset(Vl, 0, sizeof(Vl));
        for(i = 1; i <= M; ++i)
        {
              scanf("%d", &t);
              V[i].clear();
              G[i].clear();
              while(t--)
              {
                  scanf("%d%d", &a, &b);
                  if(b) V[i].push_back(a);
                  else G[i].push_back(a);
              }
        }for(i = 0; i <= N; ++i)
        {
            if(OK(i)) break;
        }
        printf("Case #%d:", ++ctr);
        if(i > N) printf(" IMPOSSIBLE\n");
        else
        {
            for(i = 1; i <= N; ++i)
                 printf(" %d", Vl[i]);
            printf("\n");
        }
    }
} 