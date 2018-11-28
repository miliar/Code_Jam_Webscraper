#include <iostream>

using namespace std;


int main(){

    int t, n, s, p,r,ti;
    
    scanf("%d", &t);
    for (int T; T<t; T++) {
        r=0;
        scanf("%d%d%d", &n, &s, &p);
        for (int c=0; c<n; c++) {
            scanf("%d", &ti);
            //cout << (double)ti/3 << endl;
            if(ti<2){
                if (ti >= p) r++;
            }
            else if((double)ti/3 > (p-1) + 0.01) r++;
            else if((double)ti/3 > (double)p-1.5 && s > 0){
                s--;
                r++;
            }
        }
        printf("Case #%d: %d\n", T+1, r);
    }
    
}