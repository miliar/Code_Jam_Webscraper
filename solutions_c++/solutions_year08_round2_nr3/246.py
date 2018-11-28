#include <iostream>
using namespace std;

struct card{
    int value;
    int lptr,nptr;
}c[1000001];

int T,times;
int K,N;

int d[101];
int ptr;
int i,j;

void simulate(){
    int i,j;

    for(i=0;i<K;i++){
        c[i].nptr = i+1;
        c[i].lptr = i-1;
    }
    c[K-1].nptr = 0;
    c[0].lptr = K-1;
    
    ptr = 0;
    for(i=1;i<=K;i++){
        for(j=1;j<i;j++) ptr = c[ptr].nptr;
        c[c[ptr].lptr].nptr = c[ptr].nptr;
        c[c[ptr].nptr].lptr = c[ptr].lptr;
        c[ptr].value = i;
        ptr = c[ptr].nptr;
    }
}

int main(){
    cin>>T;
    for(times=1;times<=T;times++){
        cin>>K>>N;
        for(i=0;i<N;i++) cin>>d[i];
        
        simulate();
        
        printf("Case #%d:",times);
        for(i=0;i<N;i++) cout<<' '<<c[d[i]-1].value;
        cout<<endl;

    }
    return 0;
}
