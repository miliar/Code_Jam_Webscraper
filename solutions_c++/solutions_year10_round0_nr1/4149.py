#include<iostream>
#include<vector>
#include<fstream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cmath>

using namespace std;

int main()
{
    
    freopen("large3.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    
    int k2;
    cin>>k2;
    for(int ch = 1; ch <= k2; ch++ ){
    int n;
    int  k;
    
    cin>>n;
    cin>>k;
    int k1;
    k1 = pow((double)2,(double)n);
    int l =0;
    l = k+1;
    if( (l%k1) == 0){
        cout<<"Case #"<<ch<<": "<<"ON"<<endl;
    }
    else {
         cout<<"Case #"<<ch<<": "<<"OFF"<<endl;
    }
} 
    
//    system("pause");
}
