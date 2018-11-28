#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
 //   freopen("C-small-attempt0.in", "r+", stdin);
        freopen("C-small-attempt1.in", "r+", stdin);
    freopen("out_c.txt", "w+", stdout);
    int T;
    scanf("%d", &T);
    for(int u=0;u<T;u++){
        long R, k, N;
        long Euro = 0;
        scanf("%d %d %d", &R, &k, &N);
        long g[1001];
        for (int i=0;i<N;i++) {
            scanf("%d", &(g[i]));
        }
        long total = 0;
        long num = 0;
        long v = 0;
        while((total+g[v])<=k && num<N) {
            total += g[v];
            v++;
            v%=N;
            num++;
        }
        long f1 = total;
        long exp[10001];
        long exp_num = 0;
        long all = 0;
        long f2 = 0;
        int flag = 0;
        int time = 1;
        if(R == 1){
            Euro = f1;
            goto fout;
        }
     //   printf("f1 %d\n", f1);

        total = 0;
        num = 0;
        while((total+g[v])<=k && num<N) {
    //        printf("g[%d] %d\n", v, g[v]);
            total += g[v];
            exp[exp_num] = g[v];
            exp_num++;
            v++;
            v%=N;
            num++;
        }
        all = total;
        f2 = all;
        if (R == 2){
            Euro = all+f1;
            goto fout;
        }
   //     printf("f2 %d\n", f2);
        flag = 0;
        time = 1;
        while(flag == 0){
            total = 0;
            num = 0;
            long v_2 = v;
            while((total+g[v])<=k && num<N) {
                total += g[v];
                v++;
                v%=N;
                num++;
            }
            int flag2 = 0;
            for(int j=0;j<exp_num++&&j<num;j++){
                if(exp[j]!=g[v_2]){
                    flag2 = 1;
                    break;
                } else {
                    v_2++;
                    v_2%=N;
                }
            }
            if(flag2 == 0 && exp_num==num)
                flag  = 1;
            else{
                all += total;
      //          printf("total %d\n", total);
                time++;
            }
            if(time+1 == R){
      //                        printf("time %d\n", time);
                Euro = f1+all;
                goto fout;
            }
        }

    //    printf("flag %d\n", flag);
        Euro = f1;
        Euro += ((R-1)/time)*all;
        Euro += f2;
        for(int i=1;i<(R-1)%time;i++){
            total = 0;
            num = 0;
            while((total+g[v])<=k&&num<N){
                total+= g[v];
                v++;
                v%=N;
                num++;
            }
            Euro+=total;
        }
fout:
        printf("Case #%d: %d\n", u+1, Euro);
    }
    
    return 0;
}
