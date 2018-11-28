#include <iostream>
#include <cmath>

using namespace std;

int main(){
    double n,t,k,r1,r2;
    long long int y;
    cin>>t;
    for(int i=1;i<t+1;i++){
        cin>>n>>k;
            cout<<"Case #"<<i<<": ";
            r1=(k+1)/pow(2.0,n);
            if(r1<=0.0)
                cout <<"OFF"<<endl;
            else{
                y=(long long int)r1;
                r2=(r1-y)*1E15;
                if(r2>0)
                    cout <<"OFF"<<endl;
                else
                    cout <<"ON"<<endl;
            }
    }
    return 0;
}
