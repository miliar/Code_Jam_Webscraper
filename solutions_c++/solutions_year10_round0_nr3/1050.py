#include <stdio.h>
#include <string.h>

int line[2222],sum[1111],cnt[1111], len[1111];
long long visited[1111];


int main() {
    freopen("out.txt", "w", stdout);
    int ca;
    scanf("%d", &ca);
    for(int v=1; v<=ca; v++) {
        memset(visited, -1, sizeof(visited));
        int r,k,n;
        scanf("%d%d%d", &r, &k, &n);
        for(int i=0; i<n; i++) {
            scanf("%d", &line[i]);
            line[n+i] = line[i];
        }
        for(int i=0; i<n; i++) {
            sum[i] = cnt[i] = 0;
            for(int j=i; j<i+n; j++) {
                sum[i] += line[j];
                cnt[i]++;
                if(sum[i] > k) {
                    sum[i] -= line[j];
                    cnt[i]--;
                    break;
                }
            }
        }

        long long ans = 0;
        int pos = 0;

        for(int i=0; i<r; i++) {
            if(visited[pos] == -1) {
                visited[pos] = ans;
                ans += sum[pos];
                len[pos] = i;
                pos += cnt[pos];
                pos = pos%n;
            }
            else {
                int cyclelen = i-len[pos];
                int cyclesum = ans - visited[pos];
                while(i+cyclelen < r) {
                    i += cyclelen;
                    ans += cyclesum;
                }
                while(i < r) {
                    ans += sum[pos];
                    pos += cnt[pos];
                    pos = pos%n;
                    i++;
                }
            }
        }

        printf("Case #%d: %I64d\n", v, ans);
    }

    return 0;
}
