#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int r[33]={0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10};
int m[33]={0, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7 ,8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11};
int main(int argc, char *argv[])
{
    freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
    int n, t, s, p, q, i, ans;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        ans=0;
        scanf("%d%d%d",&n,&s,&p);
        while(n--){
            scanf("%d",&q);
            if(r[q] >= p)ans++;
            else{
                if(s>0){
                    if(m[q] >= p){
                        ans++;
                        s--;
                    }
                }
            }

        }
        printf("Case #%d: %d\n",i,ans);
    }
    fclose(stdin);
	fclose(stdout);
    return 0;
}
