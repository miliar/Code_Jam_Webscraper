# include <iostream>

using namespace std;



int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);

    int t,cas,mx,max_c,n,temp,val1,val2,val;
    int c[1010];
    cin>>t;
    for(cas=1;cas<=t;cas++)
    {
        cin>>n;
        for(int i=0;i<n;i++) cin>>c[i];

        max_c = 1<<n;
        mx = -1;

        for(int i=1;i<max_c-1;i++)
        {
           // cout<<i<<endl;
            temp = i;
            val1=val2=0;
            val=0;
            for(int j=0;j<n;j++,temp>>=1)
            {
                if( temp & 1)
                {
                    val1^=c[j];
                    val+=c[j];
                }
                else val2^=c[j];
                //cout<<val1<<" "<<val2<<endl;
            }//cout<<"---------"<<endl;

            if( val1 == val2 )
            {

                mx = max(mx,val);
              //  cout<<"-"<<mx<<endl;
            }
        }
        printf("Case #%d: ",cas);
        if(mx == -1)
        {
            printf("NO\n");
        }
        else
        {
            printf("%d\n",mx);
        }
    }
    return 0;
}
