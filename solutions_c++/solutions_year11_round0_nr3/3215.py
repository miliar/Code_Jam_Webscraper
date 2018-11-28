#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int n;

vector<int> x;

main(){
    int t,aux,sum;
    scanf("%d",&t);
    //t=9999;
    for(int k=1;k<=t;k++){
        scanf("%d",&n);
        x.clear();
        for( int i = 0; i< n; i++){
            scanf("%d",&aux);
            x.push_back(aux);
        }
        sort(x.begin(),x.end());
        sum=0;
        for( int i = 0; i< n; i++) sum^= x[i];
        //printf("%d\n",sum);

        if(sum == 0){

            int i,sum2=0, sum3=0,b=0;
        do{b++;
        for( i = 0; i< b; i++) sum2^= x[i];
        for( ; i< n; i++) {sum3^=x[i];}
        }while(sum2 != sum3);
        //printf("%d %d\n",sum2,sum3);


            for( i = b ; i< n; i++) sum+= x[i];
            printf("Case #%d: %d\n",k,sum);
        }
        else printf("Case #%d: NO\n",k);
    }
    return 0;

}
