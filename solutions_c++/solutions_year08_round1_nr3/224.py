#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;
int ans[31]={1,5,27,143,751,935,607,903,991,335,47,943,471,55,447,463,991,95,607,263,151,855,527,743,351,135,407,903,791,135,647};
int main(){
    int t,n,i;
    cin>>t;
    cout<<setfill('0');
    for(i=1;i<=t;i++){
        cin>>n;
        cout<<"Case #"<<i<<": "<<setw(3)<<ans[n]<<endl;
    }
    return 0;
}
        
    
    
