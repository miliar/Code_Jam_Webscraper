#include <iostream>
#include <set>
#include <vector>
#include <sstream>
#include <cmath>

using namespace std;

int C,N,K,B,T;

int main(){
    cin>>C;
    for(int CC=1;CC<=C;++CC){
        cin>>N;
        int poc=0;
        vector<bool> S(N);
        S[N-1]=true;

        int cislo;
        while(true){
            cislo=N;
            bool je=true;
            //cout<<"idem"<<endl;
            while(cislo>1){
                int rank=0;
                if(!S[cislo-1]) {je=false; break;}
                for(int i=1;i<cislo;++i) if(S[i]) ++rank;
                cislo=rank;
            }
            //cout<<"mame reank "<<cislo<<endl;
            if(je && cislo==1) ++poc;

            int x=1;
            while(x<N){
                if(S[x]) S[x]=false;
                else { S[x]=true; ++x; break;}
                ++x;
            }
            //cout<<x<<" dacO: ";
            //for(int i=0;i<N;i++) cout<<S[i]<<' ';
            //cout<<endl;
            if(x==N) break;
        }

        cout<<"Case #"<<CC<<": "<<poc%100003<<endl;
        }
    return 0;
}
