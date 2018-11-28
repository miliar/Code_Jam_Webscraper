#include<iostream>
#include<cstdio>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<assert.h>

using namespace std;
int main()
{
    int cases;
    cin>>cases;
    for(int c=1;c<=cases;c++)
    {
        long long n,m,x,y,z;
        cin>>n>>m>>x>>y>>z;
        vector<long long> a(m);
        for(int i=0;i<m;i++)
        {
            cin>>a[i];
        }
        vector<long long> v(n);
        for(int i=0;i<n;i++)
        {
            v[i]=a[i%m];
            a[i%m]=(x*a[i%m]+y*(i+1))%z;
        }
        /*        for(int i=0;i<n;i++)
                  {
                  cout<<v[i]<<" "; 
                  }
                  cout<<endl;*/

        vector<long long> nis(n,1);

        for(int i=1;i<n;i++)
        {
            for(int j=0;j<i;j++)
            {
                if(v[i]>v[j])
                    nis[i]+=(nis[j]);
                nis[i]%=1000000007;
            }
        }
        long long  max=-1;
        long long tot=0;
        for(int i=n-1;i>=0;i--)
        {
                tot+=nis[i];
            tot%=1000000007;
        }
        printf("Case #%d: %Ld\n",c,tot);
        //cout<<tot<<endl;
    }
    return 0;
}
