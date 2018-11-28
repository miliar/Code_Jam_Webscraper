#include <iostream>
#include <cmath>
#include <cstdio>
#include <vector>
using namespace std;

int Pile[ 16 ];

int main(){
    freopen( "1.txt","r",stdin );
    freopen( "2.txt","w",stdout );
    int t,ca = 0;
    scanf("%d",&t);
    while(t--){
        int N,res = 0,Asum,Bsum = 0;
        scanf("%d",&N);
        for(int i = 0;i<N;++i)scanf("%d",&Pile[i]);
        for(int i = 1;i<(1<<N)-1;++i){

            vector<int>A,B;
            Asum = 0;Bsum = 0;
            for(int j = 0;j<N;++j)
                if( i & (1<<j) ){A.push_back( Pile[j] );Asum += Pile[j];}
                else {B.push_back( Pile[j] );Bsum += Pile[j];}
            int left = 0,right = 0;
            for(int j = 0;j<20;++j){
                int count = 0;
                for(int k = 0;k<A.size();++k)if( A[k] & (1<<j) )count++;
                if( count % 2 )left |= (1<<j);
            }
            for(int j = 0;j<20;++j){
                int count = 0;
                for(int k = 0;k<B.size();++k)if(B[k] & (1<<j) )count++;
                if( count % 2)right |= (1<<j);
            }
            if( left == right )res = max(res,max(Asum,Bsum));

        }
        printf("Case #%d: ",++ca);
        if( res )printf("%d\n",res);
        else puts("NO");
    }
    return 0;
}
