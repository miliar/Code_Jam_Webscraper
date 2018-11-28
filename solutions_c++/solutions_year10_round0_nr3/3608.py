#include <cstdio>
#include <vector>
#include <queue>
#define MAXN 1024

using namespace std;

int t, n;
int r, ans, k;
int first[MAXN];
int sum[MAXN];
queue<pair<int, int> > q;

void init() {
     int i;
     ans = 0;
     for (i = 0; i <= n; i++) {
         first[i] = -1;
         sum[i] = 0;     
     }
     while (!q.empty())
           q.pop();
}

int main() {
    int i, casen, on_board;
    int g, step, tmp_sum;

    freopen("tmp.in", "rt", stdin);
    freopen("tmp.out", "wt", stdout);
    
    scanf("%d", &t);
    for (casen = 1; casen <= t; casen++) {
          scanf("%d %d %d", &r, &k, &n);
          init();
          for (i = 0; i < n; i++) {
              scanf("%d", &g);
              q.push(make_pair(g, i + 1));
          }

          step = 1;
          while (first[q.front().second] == -1 && step < r) {
      //       printf("step = %d\n", step);
             first[q.front().second] = step;
             sum[q.front().second] = ans;
             tmp_sum = 0; on_board = 0;
             while ((tmp_sum + q.front().first) <= k && on_board < n) {
                   tmp_sum += q.front().first;
                   q.push(q.front());
                   q.pop();
                   on_board++;
             }
             ans += tmp_sum;
             step++;
          } 
    //      printf("step = %d\n", step);
     //     printf("ans = %d\n", ans);
          if (step <= r) {
           //  printf("step = %d\n", step);
             ans += ((r - step)/(step - first[q.front().second]) * (ans - sum[q.front().second]));
       //      printf("ans=%d\n", ans);
             //step += ((r - step)/(step - first[q.front().second]));
             step = r - ((r - step)%(step - first[q.front().second]));
         //    printf("step = %d\n", step);
             while (step <= r) {
                tmp_sum = 0; on_board = 0;
                while ((tmp_sum + q.front().first) <= k && on_board < n) {
                      tmp_sum += q.front().first;
                      q.push(q.front());
                      q.pop();
                      on_board++;
                }
                ans += tmp_sum;
                step++;
             }
             printf("Case #%d: %d\n", casen, ans);
          }
          else 
               printf("Case #%d: %d\n", casen, ans);
    }
 return 0;
}
