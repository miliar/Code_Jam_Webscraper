#include <iostream>
#include <bitset>
#include <algorithm>
//standard libraries , reference available on www.cplusplusreference.com
using namespace std;

int main()
{
    int t=1;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int n,j;
        cin>>n;
        int candy[n],sum=0,newval;
        bitset<20> bsum;
        for (j=0;j<n;j++)
        {
            cin>>newval;
            candy[j]=newval;
            bitset<20> bnewval (newval);
            bsum^=bnewval;
        }
        cout<<"Case #"<<i<<": ";
        if(bsum!=0)
        {
            cout<<"NO"<<endl;
        }
        else
        {
            sort(candy,candy+n);
            for (int i=1;i<n;i++)
            {
                sum+=candy[i];
            }
            cout<<sum<<endl;
        }
    }
return 0;
}
