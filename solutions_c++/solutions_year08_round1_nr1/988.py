#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include<cstdio>
using namespace std;

int main()
{
    int num,x=0;
    cin>>num;
    int k=0;
    while(num--)
    {
                int n;
                cin>>n;
                k++;
                vector <int> v1(n),v2(n);
                for(int i=0;i<n;i++)
                cin>>v1[i];
                for(int i=0;i<n;i++)
                cin>>v2[i];
                int ans=0;
                sort(v1.begin(),v1.end());
                sort(v2.begin(),v2.end());
                for(int i=0;i<n;i++)
                ans+=v1[i]*v2[n-1-i];
                cout<<"Case #"<<k<<": "<<ans<<endl;
    }
    return 0;
}
