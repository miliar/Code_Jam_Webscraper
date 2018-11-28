#include <iostream>
using namespace std;

int T,N,x[1000],y[1000];
int times;
long long ans;

int cmp(const void*a,const void*b){
    return *(int*)a - *(int*)b;
}
int cmp2(const void*a,const void*b){
    return *(int*)b - *(int*)a;
}

int main(){
    cin>>T;
    for(times=1;times<=T;times++){
        cin>>N;
        for(int i=0;i<N;i++) cin>>x[i];
        for(int i=0;i<N;i++) cin>>y[i];

        qsort(x,N,sizeof x[0],cmp);
        qsort(y,N,sizeof y[0],cmp2);
        
        ans = 0;
        for(int i=0;i<N;i++) ans+=x[i]*y[i];
        
        cout<<"Case #"<<times<<": "<<ans<<endl;

    }
    return 0;
}
