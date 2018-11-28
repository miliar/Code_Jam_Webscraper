#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int num;
    long long a[800],b[800];
    cin>>num;
    for(int i=0;i<num;i++)
    {
        int n;
        cin>>n;
        for(int j=0;j<n;j++)
        {
            cin>>a[j];
        }
        for(int k=0;k<n;k++)
        {
            cin>>b[k];
        }
        sort(a,a+n);
        sort(b,b+n);
        int t1=0,e1=n-1;
        long long asw=0;
        while(t1<n){asw+=a[t1++]*b[e1--];}
        cout<<"Case #"<<i+1<<": "<<asw<<endl;
    }
    return 0;
}