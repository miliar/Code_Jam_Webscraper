#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int ii=0;ii<t;ii++){
        long long n,d,g;
        cin>>n>>d>>g;
        long long nd,dd,ng,dg;
        nd=d;
        ng=g;
        dd=100;
        dg=100;
        for(int i=2;i<100;i++){
            while( nd%i==0 && dd%i==0){
                nd=nd/i;
                dd=dd/i;
            }
            while(ng%i==0 && dg%i==0){
                ng=ng/i;
                dg=dg/i;
            }
        }
        if(n<dd || (g==100 && d<100) || ( g==0 && d>0) ){
            string s="Broken";
            cout<<"Case #"<<ii+1<<": "<<s<<endl; 
            continue;
        }
        cout<<"Case #"<<ii+1<<": "<<"Possible"<<endl;
       
    }
}
