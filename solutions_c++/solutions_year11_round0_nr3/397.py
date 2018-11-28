#include<iostream>
#include<cstdlib>
#include<fstream>

using namespace std;

int main()
{
   // ifstream cin("C-large.in");
   // ofstream cout("C-large.out");
    int t;
    cin>>t;
    for (int ti=0; ti<t; ti++)
    {
        int n, m=0, min=1000000, s=0;
        cin>>n;
        for (int i=0; i<n; i++)
        {
            int x;
            cin>>x;
            m=m^x;
            if (x<min)
                min=x;
            s+=x;
        }
        if (m==0)
            cout<<"Case #"<<ti+1<<": "<<s-min<<endl;
        if (m!=0)
            cout<<"Case #"<<ti+1<<": NO"<<endl;
    }
    return 0;
}
        
