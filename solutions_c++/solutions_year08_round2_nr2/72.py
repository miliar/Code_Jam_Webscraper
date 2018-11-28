#include <stdio.h>
#include <string.h>
#include <map>
#include <vector>
#include <set>
using namespace std;

int siemat[1001000];
int primes[100000];
int pc;
void sieve(){
    pc = 0;
    memset(siemat,0,sizeof(siemat));
    for (int i=2;i<1001000;i++){
        if (!siemat[i]){
            primes[pc++]=i;
            for (int j=i+i;j<1001000;j+=i){
                siemat[j]=1;
            }
        }
    }
  //  printf("There are %d primes\n", pc);
}

int par[1001000];
// use -a based index
int parent(int pos){
    if (par[pos]==pos) return pos; 
    else return par[pos]=parent(par[pos]);
}
inline void join(int a,int b){
    if (parent(a)!=parent(b)){
        par[parent(b)]=parent(a);
    }
}

int main(){
    sieve();
    
    int ntc,ttc=0;
    scanf("%d", &ntc);
    
    while (ntc--){
        long long a,b,p;
        scanf("%I64d%I64d%I64d", &a,&b,&p);
        map<int,vector<int> > hass;
        
        for (long long i=a;i<=b;i++){
            par[i-a]=i-a;            
        }
        for (int i=0;i<pc;i++){
            if (primes[i]>=p){
                long long x = primes[i];
                long long start = (a%x>0)?a+x-a%x:a;
                if (start<=b){
                    for (long long j = start+x;j<=b;j+=x){
                        join(start-a, j-a);
                    }
                }   
            }
        }
        
        set<int> uniq;        
        for( long long i=a;i<=b;i++){
            uniq.insert(parent(i-a));
        }
        printf("Case #%d: %d\n", ++ttc, uniq.size());
    }
    
    return 0;
}
