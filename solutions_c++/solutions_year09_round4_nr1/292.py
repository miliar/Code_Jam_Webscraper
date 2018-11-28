#include <stdio.h>

char str[64];
int dat[64];

int main(){
    int testnum, n, tmp;

    scanf("%d", &testnum);
    for(int test = 1;test <= testnum;test++){
        scanf("%d", &n);
        for(int i = 0;i < n;i++){
            scanf("%s", str);
            int j;
            for(j = n;j > 0;j--)
                if(str[j - 1] == '1') break;
            dat[i] = (j > 0) ? j - 1 : 0;
        }
        int ret = 0;
        for(int i = 0;i < n;i++){
            for(int j = i;j < n;j++){
                if(dat[j] <= i){
                    tmp = dat[j];
                    for(int k = j;k > i;k--)
                        dat[k] = dat[k - 1];
                    ret += (j - i);
                    dat[i] = tmp;
                    break;
                }
            }
            /*for(int j = i + 1;j < n;j++){
                if(dat[j] < dat[i])
                    ret++;
            }*/
        }
        printf("Case #%d: %d\n", test, ret);
    }
    return 0;
}
