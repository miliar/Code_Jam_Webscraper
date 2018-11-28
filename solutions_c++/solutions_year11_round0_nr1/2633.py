#include<iostream>

using namespace std;
int main(){
    int nc;
    cin>>nc;
    for(int k=0;k<nc;k++){
        int n;
        cin>>n;
        int t=0,to=0,tb=0,po=1,pb=1;
        for(int i=0;i<n;i++){
            char c;
            int x;
            cin>>c>>x;
            if(c=='O'){
                if(abs(x-po)>to){
                    t+=abs(x-po)-to;
                    tb+=abs(x-po)-to;
                }    
                t++;
                tb++;
                po=x;
                
                to=0;
            }
            else{
                if(abs(x-pb)>tb){
                    t+=abs(x-pb)-tb;
                    to+=abs(x-pb)-tb;
                }    
                t++;
                to++;
                pb=x;
                tb=0;    
            }
        }
        cout<<"Case #"<<k+1<<": "<<t<<endl;    
    }    
}
