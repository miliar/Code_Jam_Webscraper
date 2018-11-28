#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int g[1024];
int next[1024];
int em[1024];
int main()
{
    int _t,t,k,r,n;
    cin>>_t;
    for (t=1;t<=_t;t++)
    {
        cin>>r>>k>>n;
        for (int i=0;i<n;i++)
        {
            cin>>g[i];
        }

        for (int i=0;i<n;i++)
        {
            int now=0,j=i;
            while (now + g[j] <= k)
            {
                now += g[j];
                j = (j+1) % n;
                if (j == i) break;
            }
            em[i] = now;
            next[i] = j;
        }

        //cout<<" DEBUG] gi,nexti,emi"<<endl;
        //for (int i=0;i<n;i++)
        //{
        //    cout<<"   "<<g[i]<<"\t "<<next[i]<<"\t "<<em[i]<<endl;
        //}

        int cnt=0;
        long long sum = 0;
        while (r--)
        {
            sum += em[cnt];
            cnt = next[cnt];
        }

        cout<<"Case #"<<t<<": "<<sum<<endl;
    }
    return 0;
}
