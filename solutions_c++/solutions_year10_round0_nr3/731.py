//BS渣网！怎么可以这样>_<
//要么下不下来，要么传不上去……
#include <stdio.h>
#include <string.h>

int v[1023], next[1023], time[1023];
long long R[1023], s[1023];

int main(){
    int testnum, r, k, n, cur, step;
    long long tot, ret;

    scanf("%d", &testnum);
    for(int test = 1;test <= testnum;test++){
        scanf("%d%d%d", &r, &k, &n);
        tot = ret = 0;
        for(int i = 0;i < n;i++){
            scanf("%d", &v[i]);
            tot += v[i];
        }
        int head, tail = 0, sum = 0;
        while(tail < n && sum + v[tail] <= k){
            sum += v[tail++];
        }
        if(tail == n)
            tail = 0;
        next[0] = tail;
        s[0] = sum;
        for(head = 1;head < n;head++){
            sum -= v[head - 1];
            if(tail == head){
                sum += v[head];
                tail++;
				if(tail == n)
					tail = 0;
            }
            while(tail != head && sum + v[tail] <= k){
                sum += v[tail++];
                if(tail == n)
                    tail = 0;
            }
            next[head] = tail;
            s[head] = sum;
        }
        memset(time, 0xff, sizeof(time));
        cur = step = 0;
        while(time[cur] < 0 && step < r){
            R[cur] = ret;
            ret += s[cur];
            time[cur] = step++;
            cur = next[cur];
        }
        if(step < r){
            ret += ((r - step) / (step - time[cur])) * (ret - R[cur]);
            int temp = (r - step) % (step - time[cur]);
            for(int i = 0;i < n;i++)
                if(time[i] == temp + time[cur]){
                    ret += (R[i] - R[cur]);
                    break;
                }
        }
        printf("Case #%d: %lld\n", test, ret);
    }
}
