#include<iostream>
using namespace std;

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
            int N,S,p;
            cin>>N>>S>>p;
            int term,count=0;
            for(int i=0;i<N;i++){
                    cin>>term;
                    if(term<p) continue;
                    if((term/3)>=p) count++;
                    else if((term/3)==(p-1) && (term%3)>=1) count++;
                    else if((term/3)==(p-1) && S>0) { count++; S--; }
                    else if((term/3)==(p-2) && S>0 && (term%3)>=2) { count++; S--; }
            }
            cout<<"Case #"<<t<<": "<<count<<endl;
    }
    return 0;
}
