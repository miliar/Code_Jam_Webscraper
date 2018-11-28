#include <iostream>
#include <cmath>
using namespace std;

struct combine{
    int y[20],n[20];
}c[201],milk;

int C,T,N,M,i,j;
int times;
int x,y;
int mk;

bool check(combine X, combine Y){
    int i;
    
    for(i=0;i<N;i++) if( (X.y[i]==Y.y[i]&&Y.y[i]==1) || (X.n[i]==Y.n[i]&&Y.n[i]==1) ) return 1;
    return false;
}

int main(){
    cin>>C;
    for(times=1;times<=C;times++){
        cin>>N>>M;
        memset(c,0,sizeof c);
        for(i=0;i<M;i++){
            cin>>T;
            for(j=0;j<T;j++){
                cin>>x>>y;
                --x;
                if(y==1) c[i].y[x]=1;
                else  c[i].n[x]=1;
            }
        }
        
        for(mk=0;mk<(1<<N);mk++){
            memset(&milk,0,sizeof milk);
            for(i=0;i<N;i++)
                if(mk&(1<<i)) milk.y[i]=1;
                else milk.n[i]=1;
            for(i=0;i<M;i++) if(!check(c[i],milk)) break;
            if(i==M) break;
        }
        if(mk==(1<<N)) printf("Case #%d: IMPOSSIBLE\n",times);
        else{
            printf("Case #%d:",times);
            for(i=0;i<N;i++) cout<<' '<<((mk&(1<<i))?1:0);
            cout<<endl;
        }
    }
    return 0;
}
