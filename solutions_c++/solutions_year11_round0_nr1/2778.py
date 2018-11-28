#include <iostream>
#include <string.h>
#include <string>
#include <cstdio>
#include <cmath>
using namespace std;
int main()
{
    freopen("C:\\Users\\guanxing\\Desktop\\codejam\\A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n,i,t,j;
    int p[2];
    int num[2];
    char who;
    int po,time1,time2;
    int aim[2][110];
    int aims[220];
    int total;
    scanf("%d",&t);
    for (j = 1;j <= t;j++){
        total = 0;
        aim[1][0] = aim[0][0] = 0;
        p[0] = p[1] = 1;
        scanf("%d",&n);
        for (i = 0;i < n;i++){
            scanf("%c",&who);
            scanf("%c%d",&who,&po);
            
            if (who == 'O'){
                aim[0][++aim[0][0]] = po;
                aims[i*2] = 0;
                aims[i*2+1] = po;
            }
            else{
                aims[i*2] = 1;
                aims[i*2+1] = po;
                aim[1][++aim[1][0]] = po;
            }
        }
        num[0] = num[1] = 1;
        for (i = 0;i < n;i++){
            if (aims[2*i] == 0){
                time1 = abs(aims[2*i+1]-p[0])+1;
                if (num[1] > aim[1][0])
                    time2 = 0;
                else
                    time2 = abs(aim[1][num[1]]-p[1]);
                if (time1 >= time2){
                    p[1] = aim[1][num[1]];
                }
                else{
                    p[1] = aim[1][num[1]]-time2+time1;
                }
                num[0] ++;
                p[0] = aims[2*i+1];
                total += time1;
            }
            else if (aims[2*i] == 1){
                time1 = abs(aims[2*i+1]-p[1])+1;
                if (num[0] > aim[0][0])
                    time2 = 0;
                else
                    time2 =abs(aim[0][num[0]]-p[0]);
                if (time1 >= time2){
                    p[0] = aim[0][num[0]];
                }
                else{
                    p[0] = aim[0][num[0]]-time2+time1;
                }
                num[1]++;
                p[1] = aims[2*i+1];
                total += time1;
            }
        }
        printf("Case #%d: %d\n",j,total);
    }
    return 0;
}
                        
        
