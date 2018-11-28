// Ireyoner
// 92misiu@gmail.com
// Michal Bartecki
// ul. Jana Keplera 4F/15
// 60-158 Poznan
// Poland

#include<iostream>
using namespace std;
int main(){
    int T,N,S,p,val,max,ile;
    cin>>T;
    for( int i=0; i<T; i++){
        cin >>N>>S>>p;
        //cout<<"first: "<<N<<' '<<S<<' '<<p<<endl;
        if(p>1){
            p=p*3-2;
            max=p-2;
        }
        else if (p==1){
            p=1;
            max=1;
        }
        else{
            p=0;
            max=0;
        }
        ile=0;
        //cout<<"sec: "<<N<<' '<<S<<' '<<p<<endl<<"val: ";
        for(int j=0; j<N; j++){
            cin>>val;
            //cout<<val<<' ';
            if(val>=p)
                ile++;
            else if(val>=max&&S>0){
                ile++;
                S--;
            }
        }
        cout<<"Case #"<<i+1<<": "<<ile<<endl;
    }
    return 0;
}
