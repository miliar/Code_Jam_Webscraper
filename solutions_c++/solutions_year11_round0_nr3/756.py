#include <cstdio>
#include <cstdlib>
#include <map>

using namespace std;

int main(){
    map<int,int> mapa;
    int num[1020];
    int qtt[1020];
    int n,i,j,k,x,t;
    int aux,pos,min,max,total;
    int tot[100];
    

    
    scanf("%d", &t);
    
    for( k =1; k <=t; k++){
        memset(num,-1,sizeof(num));
        memset(qtt,0,sizeof(qtt));
        memset(tot,0,sizeof(tot));
        min = 9999999;
        total = 0;
        max = 0;
        mapa.clear();
        mapa[0] = 0;        
        scanf("%d", &n);
        for( i =0; i < n; i++){
            scanf("%d", &x);
            total+=x;
            pos = 0;
            if( x < min ) min = x;
            while(x){
                tot[pos++] += (x%2);
                //num[i][pos] = tot[pos];
                x/=2;
            }
            if( pos > max ) max = pos;
            /*for( map<int,int>::iterator ii = mapa.begin(); ii != mapa.end(); ii++){
                if( mapa.find(!((ii->first)^x)) != mapa.end() ){
                    if( mapa[!(ii->first^x)] > mapa[ii->first]+x ){
                        mapa[!(ii->first^x)] = mapa[ii->first]+x;
                    }
                } else mapa[!(ii->first^x)] = mapa[ii->first]+x;
            }*/
        }
//        x = 0;
        int ok = 0;
        for( i =0, j =1; i < max; i++, j*=2){
            //printf("[%d]", tot[i]);
            if( tot[i]%2 ) ok = 1;
        }
  //      printf("::%d %d \n", x, max);
        printf("Case #%d: ", k);
        if( ok ){
            printf("NO\n");
        } else {
            printf("%d\n", total-min);
        }
    }
    
    
}
