#include<iostream>
using namespace std;
int t, n, s, p, a;
int main()
{
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        int wyn=0;
        cin>>n>>s>>p;
        for(int j=0; j<n; j++){
        cin>>a;
        if(a>=3*p-2 && a>=p){wyn++;
        }else
        if(a>=3*p-4 && s>0 && a>=p){wyn++; s--;}
        }
        cout<<"Case #"<<i<<": "<<wyn<<endl;

    }
}
