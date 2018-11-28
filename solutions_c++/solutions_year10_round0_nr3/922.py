#include <stdio.h>
#include <string.h>
int num[1010];
int head[1010];
long long count[1010];

int main () {
    int kase, i, r, k, n, h = 1;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    scanf("%d", &kase);
    while (kase--) {
          scanf("%d %d %d", &r, &k, &n);
          for (i = 0; i < n; i++) 
              scanf("%d", &num[i]);
          memset(head,0,sizeof(head));
          count[0] = 0;
          int ptr = 0, sum = 1; 
          while ( head[ptr] == 0 && sum <= r) {
                head[ptr] = sum;
                if (num[ptr] > k) break;
                int tmp = k-num[ptr];
                for (i = (ptr+1)%n; i != ptr && tmp >= num[i]; ++i,i%=n) 
                    tmp = tmp-num[i];
                count[sum] = count[sum-1]+k-tmp;
                ptr = i;
                sum++;
                if (head[ptr] != 0) break;
          }
          /*if (sum > r) {
             printf("%d\n",count[sum-1]);
          } */
        //  printf("%d\n", ptr);
          if (num[ptr] > k) {
             printf("Case #%d: %lld\n",h++,count[sum-1]);
          }
          else {
               long long p = (r-(head[ptr]-1))%(sum-head[ptr]);
               long long q = (r-(head[ptr]-1))/(sum-head[ptr]);
          //     printf("%d %d\n", p, q);
               long long ans = count[head[ptr]-1]+q*(count[sum-1]-count[head[ptr]-1]);
               ans += count[head[ptr]+p-1]-count[head[ptr]-1];
               printf("Case #%d: %lld\n",h++,ans);
          }
    }
 //   while (1);
    return 0;
}
