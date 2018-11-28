#include <string>
#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("d:\\in.txt","r",stdin);
    freopen("d:\\out.txt","w",stdout);
    int T,cas,i,j,p,q,a[10];
    int res,sum;
    bool f[105];
    
    cin>>T;
    for (cas=1;cas<=T;cas++)
    {
        cin>>p>>q;
        for (i=0;i<q;i++) cin>>a[i];
        sort(a,a+q);
        res=1000000000;
        do
        {
            memset(f,0,sizeof(f));
            sum=0;
            for (i=0;i<q;i++)
            {
                f[a[i]]=true;
                j=a[i]-1;
                while (j>0&&!f[j]) sum++,j--;
                j=a[i]+1;
                while (j<=p&&!f[j]) sum++,j++;
            }
            if (sum<res) res=sum;
        }while (next_permutation(a,a+q));
        cout<<"Case #"<<cas<<": "<<res<<endl;
    }
    return 0;
}
        
