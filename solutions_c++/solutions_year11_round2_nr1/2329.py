#include <cstdio>
#include <vector>
#include <algorithm>
#define MaxN 111

using namespace std;

char wins[MaxN][MaxN];
double wp[MaxN], op[MaxN], sumOp[MaxN], sol[MaxN];
vector<int> ops[MaxN];

double div(double a, double b){
   if (b == 0) b = 1;
   return a/b;
}

void solve()
{
   int minVal = 1<<30, sumTotal = 0, xor = 0, n, x;
   scanf("%d\n", &n);
   for (int i=0; i<n; i++){
      scanf("%s", wins[i]);
      ops[i].clear();
   }
   memset(wp, 0, sizeof(wp));
   for (int i=0; i<n; i++)
      for (int j=i+1; j<n; j++)
         if (wins[i][j] != '.'){
            ops[i].push_back(j);
            ops[j].push_back(i);
            if (wins[i][j] == '1')
               wp[i]++;
            else
               wp[j]++;
         }
   for (int i=0; i<n; i++){
      if (ops[i].size()){
         sol[i] = wp[i] / ops[i].size();
      }
      op[i] = sumOp[i] = 0;
      for (unsigned j=0; j<ops[i].size(); j++){
         int k = ops[i][j];
         bool vict = (wins[k][i] == '1');
         op[i] += div(wp[k] - vict, ops[k].size() - 1);
      }
      op[i] = div(op[i], ops[i].size());
   }
   for (int i=0; i<n; i++){
      for (int k=0; k<ops[i].size(); k++){
         int j = ops[i][k];
         sumOp[i] += op[j];
      }
      sumOp[i] = div(sumOp[i], ops[i].size());
      printf("%.9f\n", 0.25 * sol[i] + 0.5 * op[i] + 0.25 * sumOp[i]);
   }
}

int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   int tst;
   scanf("%d", &tst);
   for (int iter = 1; iter <= tst; iter++){
      printf("Case #%d:\n", iter);
      solve();
   }
   return 0;
}