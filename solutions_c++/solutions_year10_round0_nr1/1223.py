#include<iostream>
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int N,K;
    int num;
    int cas=1;
    cin>>num;
    while(num--){
        cin>>N>>K;
        bool flag=true;
        for(int i=0;i<N;i++){
            if(K%2==0){
                flag=false;
                break;
            }
            K=K/2;
        }
        if(flag) cout<<"Case #"<<cas++<<": ON"<<endl;
        else cout<<"Case #"<<cas++<<": OFF"<<endl;
    }
    return 0;
}
