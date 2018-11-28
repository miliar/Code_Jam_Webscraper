#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int t,Case=1;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int temp;
        vector <int> a;vector <int> b;
        for(int i=0;i<n;i++)
        {  cin>>temp;a.push_back(temp);}        
        for(int i=0;i<n;i++)
        {   cin>>temp;b.push_back(temp);}
        sort(a.begin(),a.end());
        sort(b.rbegin(),b.rend());
        unsigned long long  ans=0;
        for(int i=0;i<n;i++)
        {
           ans+=a[i]*b[i];
        }
        cout<<"Case #"<<Case++<<": "<<ans<<endl;
    }
}
