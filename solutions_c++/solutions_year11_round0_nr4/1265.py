#include <cstdio>
#include <vector>
#define MaxN 1001

using namespace std;

int n, perm[MaxN], p[MaxN], used[MaxN];
double cycles[MaxN][MaxN], avg[MaxN], fact[MaxN];

vector<int> getCycles(int p[], int n){
   vector<int> rez;
   memcpy(perm, p, sizeof(int) * n);
   for (int i=0; i<n; i++)
      if (perm[i] >= 0){
         int len = 1, st = i, k = i;
         while (perm[k] != st){
            int prev = k;
            k = perm[k];
            perm[prev] = -1;
            len++;
         }
         perm[k] = -1;
         rez.push_back(len);
      }
   int sum = 0;
   for (size_t i=0; i<rez.size(); i++)
      sum += rez[i];
   if (n != sum)
      printf("BAD!!\n");
   return rez;
}

void back(int lev){
   if (lev == n){
      vector<int> cyc = getCycles(p, n);
      for (size_t i=0; i<cyc.size(); i++)
         cycles[n][cyc[i]]++;
      return;
   }
   for (int i=0; i<n; i++)
      if (!used[i]){
         used[i] = true;
         p[lev] = i;
         back(lev+1);
         used[i] = false;
      }
}

void precalc()
{
   avg[1] = 0;
   avg[2] = 2;
   fact[1] = 1;
   for (int i=2; i<=10; i++)
      fact[i] = i * fact[i-1];
   for (n=3; n<=10; n++){
      back(0);
      double sum = 0;
      for (int i=1; i<n; i++)
         sum += avg[i] * cycles[n][i];
      avg[n] = (sum + fact[n]) / (fact[n] - cycles[n][n]);
   }
}

void solve()
{
   scanf("%d", &n);
   for (int i=0; i<n; i++)
      scanf("%d", p+i), p[i]--;
   vector<int> cyc = getCycles(p, n);
   double sol = 0;
   for (size_t i=0; i<cyc.size(); i++)
      if (cyc[i] > 1)
         sol += cyc[i];
   printf("%.8f\n", sol);
}

int main()
{
   //precalc();
   freopen("data.in", "r", stdin);
   freopen("data.out", "w", stdout);
   int tst;
   scanf("%d", &tst);
   for (int iter = 1; iter <= tst; iter++){
      printf("Case #%d: ", iter);
      solve();
   }
   return 0;
}