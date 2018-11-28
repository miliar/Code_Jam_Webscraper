#include<stdio.h>
#include<set>
#include<vector>
using namespace std;

int A,B,C,P;
vector<int> PRIMES;
int euclid(int a, int b)
{
    if(b==0)
        return a;
    return euclid(b, a%b);
}

int discover(int a, int b)
{
    int i,j;
    for(j=0;j<PRIMES.size();j++){
        if(PRIMES[j]>min(a,b))return 0;
        if(PRIMES[j]>=P){
            if(((a%PRIMES[j])==0) && (b%PRIMES[j])==0)return 1;
        }
    }
    return 0;
}

int T[2000];
int main()
{
    int i,j;
    PRIMES.push_back(2);
    for(i=3;i<=1000;i++){
        int ok = 1;
        for(j=0;j<PRIMES.size() && PRIMES[j]<i;j++){
            if( (i % PRIMES[j])==0) ok = 0;
        }
        if(ok)PRIMES.push_back(i);
    }
    //for(i=0;i<10;i++)printf("%d\n", PRIMES[i]);
    scanf("%d", &C);
    for(int TC = 1;TC<=C;TC++){
        scanf("%d%d%d", &A,&B,&P);
        
        int sum = 0;
        for(i=0;i<2000;i++)T[i]=i;
        i = A;
        int COLOR = 1;
        while(i<=B){
                for(j=A;j<=B;j++){
                    if(discover(i,j)){
                        //merge
                        for(int k=A;k<=B;k++){
                            if(T[k]==T[i] || T[k]==T[j]){
                                T[k] = min(T[i], T[j]);
                            }
                        }
                    }
                }
            i++;
        }
        set<int> S;
        for(i=A;i<=B;i++)S.insert(T[i]);
        printf("Case #%d: %d\n", TC, S.size());        
    }
    
    return 0;
}
