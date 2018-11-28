#include<iostream>
using namespace std;

int T;
int N,K;


int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cas = 0;
    cin>>T;
    while(T--){
        cin>>N>>K;
        int t1 = (1<<N)-1;
        cas++;
        cout<<"Case #"<<cas<<": ";
        if((t1&K)==t1){
            cout<<"ON\n";
        }
        else{
            cout<<"OFF\n";
        }
    }
    return 0;
}

