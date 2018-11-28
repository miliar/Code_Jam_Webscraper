#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int iii,T;
    scanf("%d",&T);
    for(iii=1;iii<=T;iii++){
        int K,n;
        scanf("%d",&K);
        scanf("%d",&n);
        vector<int> di(n);
        int i;
        for(i=0;i<n;i++)
            scanf("%d",&di[i]);
        vector<int> ki(K);
        int pozost=K,akt=0,teraz=1,bufor=0;
        while(pozost>1){
            if(bufor==0){
                ki[akt]=teraz;
                pozost--;
                teraz=K-pozost+1;
                bufor=(teraz-1)%pozost+1;
            }
            akt=(akt+1)%K;
            if(ki[akt]==0)
                bufor--;
        }

        printf("Case #%d:",iii);
        for(i=0;i<n;i++)
            printf(" %d",(ki[di[i]-1]+K-1)%K+1);
        printf("\n");
    }
	return 0;
}
/*
1
5
5 1 2 3 4 5
*/
