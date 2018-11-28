#include <cstdio>
#include <cstring>
#include <set>
#include <iostream>
#include <algorithm>

using namespace std;

int teste,A,B;
int pot[7];

int digitos(int n){

    if(!n) return 0;

    return 1 + digitos(n/10);

}

int main(void){

    freopen("C.in","r",stdin);

    freopen("C.out","w",stdout);


    pot[0]=1;
    pot[1]=10;
    pot[2]=100;
    pot[3]=1000;
    pot[4]=10000;
    pot[5]=100000;
    pot[6]=1000000;
        pot[7]=1000000;


    scanf("%d",&teste);

    for(int caso=1;caso<=teste;caso++){
        printf("Case #%d: ",caso);
        scanf("%d %d",&A,&B);
        set< pair<int,int> > heap;

        for(int n=A;n<=B;n++){

            int d=digitos(n);

            for(int i=1;i<d;i++){
                int r=n%pot[i];
                if(!r) continue;
                if(r<pot[i-1]) continue;
                int num=r*pot[d-i]+n/pot[i];
                if(num!=n && num<=B && num>n){
                    heap.insert(make_pair(max(num,n),min(num,n)));
                }
            }

        }

        printf("%d\n",heap.size());

    }

    return 0;
}
