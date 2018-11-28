#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int main()
{
    int nCase, n, con = 1;
    int TotalStep, opos, bpos, pos, ostep, bstep, ts;
    char c;
    //freopen("input.txt", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);
    scanf("%d", &nCase);
    while(nCase--){
        scanf("%d", &n);
        pos = 1;
        opos = bpos = 1;
        ostep = bstep = TotalStep = 0;
        for(int i = 0; i < n; i++){
            getchar();
            scanf("%c%d", &c, &pos);
            if(c == 'O'){
                ts = pos > opos ? pos - opos : opos - pos;
                if(ostep <= ts){
                    TotalStep += (ts - ostep) + 1;
                    bstep += (ts - ostep) + 1;
                }else{
                    TotalStep++;
                    bstep++;
                }
                ostep = 0;
                opos = pos;
            }else {
                ts = pos > bpos ? pos - bpos : bpos - pos;
                if(bstep <= ts){
                    TotalStep += (ts - bstep) + 1;
                    ostep += (ts - bstep) + 1;
                }else{
                    TotalStep++;
                    ostep++;
                }
                bstep = 0;
                bpos = pos;
            }
        }
        printf("Case #%d: %d\n", con++, TotalStep);
    }
    return 0;
}
