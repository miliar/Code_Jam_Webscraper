#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
vector<long long> v;
long long max (long long a, long long b)
{
    if (a>b)
    {
        b=a;
    }
    return b;
}
int main()
{
    ifstream cin ("i.in");
    ofstream cout ("o.out");
    long long t, n, L, T, sum=0, i, j, k, c, maxx=0, x, x_sum, res, res_1;
    bool z;
    cin>>T;
    for (i=0;i<T;++i)
    {
        cin>>L>>t>>n>>c;
        v.clear();
        res=0;
        for (j=0;j<c;++j)
        {
            cin>>k;
            k*=2;
            v.push_back(k);
        }
        if (L>0)
        {
            maxx=0;
            sum=0;
            for (j=0;j<n;++j)
            {
                if (v[j%c]-min(max((t-sum), 0), v[j%c])>maxx)
                {
                    x=j;
                    maxx=v[j%c]-min(max((t-sum), 0), v[j%c]);
                    x_sum=sum;
                }
                sum+=v[j%c];
            }
            res-=maxx/2;
            res_1=maxx/2;
            if (L>1)
            {
                maxx=0;
                sum=0;
                for (j=0;j<n;++j)
                {
                    if (j==0)
                    {
                        sum+=v[0];
                        continue;
                    }
                    if (j==x)
                    {
                        sum+=res_1;
                        continue;
                    }
                    if (v[j%c]-min(max((t-sum), 0), v[j%c])>maxx)
                    {
                        maxx=v[j%c]-min(max((t-sum), 0), v[j%c]);
                    }
                    sum+=v[j%c];
                }
                res-=maxx/2;
            }
        }
        for (j=0;j<n;++j)
        {
            res+=v[j%c];
        }
        cout<<"Case #"<<(i+1)<<": "<<res<<endl;
    }
    return 0;
}
