#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int koliko[1000], idemna[1000];
long long grupe[1000];

int main(){
    int t,R,N;
    long long k;
    scanf("%d",&t);
    for(int test = 0;test < t; ++test){
        scanf("%d %lld %d",&R,&k,&N);
        memset(koliko, 0, sizeof(koliko));
        memset(idemna, -1, sizeof(idemna));
        int trenutno = 0;
        for(int x = 0;x<N;++x)
            scanf("%lld",&grupe[x]);
        while( idemna[trenutno] == -1 ){
            long long cijena = grupe[trenutno];
            int temp = trenutno+1;
            if( temp == N ) temp = 0;
            while( trenutno != temp ){
                if( cijena + grupe[temp] > k ) break;
                cijena += grupe[temp];
                ++temp;
                if( temp == N ) temp = 0;
            }
            idemna[trenutno] = temp;
            koliko[trenutno] = cijena;
            trenutno = temp;
        }
        int temp = 0;
        long long sol = 0;
        for(int x = 0;x<R;++x){
            sol += koliko[temp];
            temp = idemna[temp];
        }
        printf("Case #%d: %lld\n",test+1,sol);
    }
    return 0;
}
