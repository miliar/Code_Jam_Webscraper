#include <cstdio>
#include <string.h>

int main(){
        int T, ca=0;
        scanf("%d", &T);
        char s[100];
        gets(s);
        while (T--){
                gets(s);
                int len = strlen(s), c=0;
                bool vis[200]; memset(vis, 0, sizeof(vis));
                for (int i=0; i<len; i++){
                        if (!vis[s[i]]){
                                c++;
                                vis[s[i]] = true;
                        }
                }
                if (c<2) c = 2;

                int d[200];
                int use[200]; for (int i=0; i<200; i++) use[i] = -1;
                use[s[0]] = 1;
                int k = 0;
                for (int i=0; i<len; i++){
                        if (use[s[i]] == -1){
                                use[s[i]] = k++;
                                if (k==1) k++;
                        }
                        d[i] = use[s[i]];
                }
/*
                for (int i=0; i<len; i++)
                        printf("%d ", d[i]);
                printf("\n");
*/
                long long ans = 0;
                long long q = 1;
                for (int i=len-1; i>=0; i--){
                        ans += d[i] * q;
                        q *= c;
                }


                printf("Case #%d: %lld\n", ++ca, ans);
        }
        return 0;
}
