#include<iostream>
using namespace std;

int main(){
    int cases;
    cin>>cases;
    for(int kases=1;kases<=cases;kases++){
            int N,S,p;
            cin>>N>>S>>p;
     //       cout<<N<<S<<p;
            int c_C=0;
            int c_S=0;
            for(int i=0;i<N;i++){  
                    int value,temp;
                    cin>>value;
                    if( value>=(3*p-2)){
                        c_C++;
                        continue;
                    }
                    if( value>0 && value>=(3*p-4))
                               c_S++;             
            }
  //          cout<<c_C<<" "<<c_S<<endl;
            cout<<"Case #"<<kases<<": "<<c_C + min(c_S, S)<<endl;
    }
    
 return 0;   
}
