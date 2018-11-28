#include <iostream>
#include <algorithm>
using namespace std;
int t,casen;
int n,c[15];
int P,S,sum,totalsum;

bool find (int p)
{
    if (p==n && P==S && sum!=totalsum && sum!=0) return true;
    if (p==n) return false;
    P=P^c[p];
    sum+=c[p];
    if (find(p+1)) return true;
    sum-=c[p];
    P=P^c[p];
    S=S^c[p];
    if (find(p+1)) return true;
    S=S^c[p];
    return false;
}

int main()
{
    cin>>t;
    for (casen=1; casen<=t; casen++)
    {
        cin>>n;
        totalsum=0;
        for (int i=0; i<n; i++)
        {
            cin>>c[i];
            totalsum+=c[i];
        }
        sort(c,c+n);
        reverse(c,c+n);
        P=0;
        S=0;
        sum=0;
        cout<<"Case #"<<casen<<": ";
        if (!find(0)) cout<<"NO"<<endl;
        else cout<<sum<<endl;
    }
    return 0;
}

