#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;

int main()
{
    freopen("A-large.in.txt","r",stdin);
    freopen("A.out","w",stdout);

    int tcases;
    cin>>tcases;
    for(int t=1;t<=tcases;t++)
    {
        unsigned long long p,k,l;
        cin>>p>>k>>l;

        vector<unsigned long long> n(l);

        for(long i=0;i<l;i++)
            cin>>n[i];

        sort(n.begin(),n.end());
        reverse(n.begin(),n.end());
        unsigned long long sum=0;

        //cout<<"P="<<p<<" K="<<k<<endl;

        for(unsigned long long i=0;i<p;++i)
        {
            for(unsigned long long j=0;j<k;j++)
            {
               // cout<<"i="<<i<<" j="<<j<<" sum="<<(i*(k))+j<<endl;
                if((i*k)+j<n.size())
                    sum += (unsigned long long)n[(i*(k))+j]*((unsigned long long)i+1);
            }
        }

        cout << "Case #"<<t<<": " << sum<< endl;
    }
    return 0;
}
