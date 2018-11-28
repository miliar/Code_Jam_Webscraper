#include<iostream>
using namespace std;
int main()
{
    unsigned long long int c=1,i,m,k,n;
    freopen("C://Users//abir//Desktop//New Folder//A.in","r",stdin);
    freopen("C://Users//abir//Desktop//New Folder//A.out","w",stdout);
    cin>>n;
    while(n--)
    {
        cin>>m>>k;
        for(i=0;i<m;i++)
        {   if(k%2==0)break;
            k=k>>1;    
        }    
        if(i==m)cout<<"Case #"<<c++<<": ON"<<endl;
        else cout<<"Case #"<<c++<<": OFF"<<endl;
    }
    
    //cin>>i;

return 0;    
}   
