# include <iostream>
# include <string>
# include <stdio.h>
using namespace std;

int main()
{
     freopen("C-small-attempt0.in","r",stdin);
     freopen("C-small-attempt0.out","w",stdout);
    long long t,cas;
    long long n,l,h,d[10007];
    cin>>t;
    for(cas=1;cas<=t;cas++)
    {

        cin>>n>>l>>h;
        for(int i=0;i<n;i++)
        {
            cin>>d[i];
        }
        long long i,j;
        for(i=l;i<=h;i++)
        {

            for(j=0;j<n;j++)
            {
                if( i%d[j] == 0|| d[j]%i==0 )
                    continue;
                break;
            }
            if(j == n)
                break;
        }
        printf("Case #%d: ",cas);
        if(i>h)
        {
            printf("NO\n");
        }else
            cout<<i<<endl;
    }
    return 0;
}
