#include <iostream>

using namespace std;

int r[]={0,0,0,1,2,2,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6};

int  main(){
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        int a=0;
        int l,p,c;
        cin>>l>>p>>c;
        int ns=1;
        int sk=l;
        while(sk<p){
            if(p/c<sk){
                 ns++;
                 break;
            }else{
               sk*=c;
               ns++;
            }
        }


        a=r[ns];
        cout<<"Case #"<<i<<": "<<a<<endl;
    }
    return 0;
}
