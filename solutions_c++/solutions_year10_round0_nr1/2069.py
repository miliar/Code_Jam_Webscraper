#include<iostream>
using namespace std;

int main()
{
    long long N,K,T;
    long long temp;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
              
            cin>>N>>K;
           
            cout<<"Case #"<<t<<": ";
            temp=K%(1ll<<N);
         //   cout<<K<<" "<<temp<<"  "<<(1ll<<N)<<endl;
           if(temp==(1ll<<(N))-1)
           
            {
                          cout<<"ON\n";
            }
            else
            {
                cout<<"OFF\n";
            }
            
    }
    //system("pause");
    return 0;
}
            
