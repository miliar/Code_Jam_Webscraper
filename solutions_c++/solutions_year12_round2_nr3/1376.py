#include <cstdio>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <string>
#include <cstring>
#include <set>
#include <queue>
#include <stack>

#define MAX 30

using namespace std;

int vetor[MAX],T,N;
char acho;
int cont1,cont2;
int vetor1[MAX];
int vetor2[MAX];


bool bckt(int tot1,int tot2,int atual){


    if(tot1 == tot2 && cont1 && cont2){

        for(int i=0;i<cont1;i++){
            printf("%d ",vetor1[i]);
        }
        printf("\n");


        for(int i=0;i<cont2;i++){
            printf("%d ",vetor2[i]);
        }
        printf("\n");


        return true;

    }

    if(atual == N){
        return false;
    }

    vetor1[cont1++]=vetor[atual];

    if(bckt(tot1+vetor[atual],tot2,atual+1)) return true;

    cont1--;

    vetor2[cont2++]=vetor[atual];

    if(bckt(tot1,tot2+vetor[atual],atual+1)) return true;

    cont2--;

    if(bckt(tot1,tot2,atual+1)) return true;


    return false;

}

int main(void){

    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);

    scanf("%d",&T);

    for(int casos=1;casos<=T;casos++){

        printf("Case #%d:\n",casos);

        scanf("%d",&N);

        for(int i=0;i<N;i++){
            scanf("%d",&vetor[i]);
        }

        cont1 = cont2 = 0;

        if(!bckt(0,0,0)) printf("Impossible\n");

    }

    return 0;


}
