
#include <algorithm>
#include <cstdio>
#include <cstring>

#include <cassert>

unsigned int a[1001][1001];

int L,P,C,T;

unsigned int calc(int l, int p){
    if (a[l][p]!=-1)
        return a[l][p];
    if (l*C>=p)
        return a[l][p]=0;

    unsigned b=-1;
    for (int x=l+1; x<p; x++)
        b=std::min(b, 1+std::max(calc(l,x), calc(x,p)));
    assert(b!=-1);
              
    return a[l][p]=b;
}

int main(){
    
    scanf("%d", &T);
    
    for (int t=1; t<=T; t++){
        
        scanf("%d %d %d", &L, &P, &C);
        
        memset(a, -1, sizeof(a));
        
        // for (int l=0; l<=L; l++){
        //     for (int d=1; l+d<=P; d++){
        //         int p=d+l;
        //         if (l*C >= p)
        //             a[l][p]=0;
        //         else 
        //             for (int x=l+1; x<p; x++)
        //                 if (std::max(a[l][t], a[t][p]) != 0xFFFFFFFF)
        //                     a[l][p]=std::min(a[l][p], 1+std::max(a[l][t], a[t][p]));
                        
                
        //     }
        // }
        
        // for (int l=0; l<=L; l++){
        //     for (int p=l+1; p<=P; p++)
        //         printf("%2d ", a[l][p]);
        //     printf("\n");
        // }
        

        printf("Case #%i: %u\n", t, calc(L,P));
    }
}
