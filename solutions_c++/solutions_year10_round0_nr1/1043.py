#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<numeric>
#include<map>
#include<set>
#include<queue>
using namespace std ;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int caso;
    cin>>caso;
    for(int i=0;i<caso;i++){
        cout<<"Case #"<<i+1<<": ";
        long long n,k;
        cin>>n>>k;
        bool ok=0;
        for(int i=0;i<n;i++)if( (k&(1<<i))==0 )ok=1;
        
        if(!ok){  
            cout<<"ON"<<endl;
        }else
        cout<<"OFF"<<endl;
    }
    //system("pause");
    return 0;
}


