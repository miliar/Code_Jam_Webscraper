#include<cstdio>
#include<algorithm>

using namespace std;



int main(){
    int z;
    scanf("%d",&z);
    int Z=z;
    while(z--){
        int n,pozO=1,pozB=1,tO=0,tB=0,wynik=0,t;
        scanf("%d",&n);
        while(n--){
            char C;int k;
            getchar(); C=getchar();
            scanf("%d",&k);
            if(C=='O'){
              t=max(pozO-k,k-pozO);
              t=max(t-tO,0);
              t++;
              tB+=t;
              wynik+=t;
              pozO=k;
              tO=0;
            }
            if(C=='B'){
              t=max(pozB-k,k-pozB);
              t=max(t-tB,0);
              t++;
              tO+=t;
              wynik+=t;
              pozB=k;
              tB=0;
            }
        }
        printf("Case #%d: %d\n",Z-z,wynik);
    }
}

            
