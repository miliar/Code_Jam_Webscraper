#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    int t,r,k,n,g[1000],sum;
    int i,j,ptr,ctr,mny;
    ifstream fin("C-small.in");
    ofstream fout("C-small.out");
    fin>>t;
    for(i=1;i<=t;i++)
    {
        mny=ptr=0;
        fin>>r>>k>>n;
        for(j=0;j<n;j++)
        {
            fin>>g[j];
        }
        while(r>0)
        {
            sum=0;
        for(j=0;j<n;ptr++,j++)
        {
            if(ptr==n)
                ptr=0;
            sum+=g[ptr];
            if(sum>=k)
            {
                if(sum>k)
                {
                    sum-=g[ptr];
                }
                else
                    ptr++;
                break;
            }
        }
        mny+=sum;
        r--;
        }
        fout<<"Case #"<<i<<": "<<mny<<endl;
    }
    return 0;
}
