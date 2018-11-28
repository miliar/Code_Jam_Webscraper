#include<cstdio>
#include<vector>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<sstream>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<queue>
#include<deque>
#include<fstream>
using namespace std;
void printArray(int _a[],int _n){
    if(_n==0){
        puts("");
        return;
    }
    printf("%d",_a[0]);
    for(int i=1;i<_n;++i){
        printf(" %d",_a[i]);
    }
    puts("");
}
#define N 1000000
long long a[N];

long long copia[N];

int n,L,C;
long long T;

long long f0(int start){
    long long ret=0; 
    for(int i=start;i<n;++i){
        ret+=a[i];
    }
    return ret;
}

long long f(int start,int cuantos){
    if(start==n)return 0;
    if(cuantos==0)return f0(start);
    int faltan=n-start;
    if(faltan<=cuantos){
        long long ret=0LL;
        for(int i=start;i<n;++i){
            ret+=a[i]/2;
        }
        return ret;
    }
    for(int i=start;i<n;++i)copia[i]=a[i];
    sort(copia+start,copia+n,greater<long long>());
    long long ret=0LL;
    for(int i=start;i<start+cuantos;++i){
        ret+=copia[i]/2;
    }
    for(int i=start+cuantos;i<n;++i){
        ret+=copia[i];
    }
    return ret;
}

long long doit(){
    cin>>L>>T>>n>>C;
    for(int i=0;i<C;++i){
        cin>>a[i];
    }
    for(int i=C;i<n;++i){
        a[i]=a[i%C];
    }
    for(int i=0;i<n;++i){
        a[i]*=2;//normalizacion
    }
    if(L==0)return f0(0);
    long long tiempo=0LL;
    for(int i=0;i<n;++i){
        if(T<tiempo+a[i]){
            //cout<<"index: "<<i<<"\n";
            long long temp;
            if(T==tiempo){
                temp=a[i]/2;
            }
            else{
                long long recorrido=T-tiempo;
                temp=recorrido+(a[i]-recorrido)/2;
            }
            long long aux=min(temp+f(i+1,L-1),a[i]+f(i+1,L));//uso y no uso 1 booster en i
            return tiempo+aux;
        }
        tiempo+=a[i];
    }
    return tiempo;
}
int main(){
    int T;
    cin>>T;
    for(int i=1;i<=T;++i){
        cout<<"Case #"<<i<<": "<<doit()<<"\n";
    }
}

