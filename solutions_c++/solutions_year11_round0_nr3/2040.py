#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
#define rep(X,Y) for ( int X=0; X<Y ; X++)

bool IsPermissible(vector<int> &v,int n)
{
    int res=v[0];
    for ( int i=1; i<n ; i++)
    {
        res^= v[i];
    }
    return res==0;
}
bool IsPermissiblei(vector<int> &v,int i,int n)
{
    int res=v[i];
    for ( int j=i; j<n ; j++)
    {
        res^= v[j];
    }
    return res==0;
}


void run(vector<int> &v,int n,int T)
{
    int res=0;
    int res2=0;

    int sum=0;
    int patrick=0;
    sort(v.begin(),v.end());

    if (IsPermissible(v,n))
    {
        for ( int i=0 ; i <n; i++)
        {
            res=v[0];
            for ( int j=1 ; j <i ; j++)
            {
                res^=v[j];

            }
            res2=v[i];
            sum=v[i];
            for ( int k=i+1 ; k <n ; k++)
            {

                res2^=v[k];
                sum+= v[k];

            }

            if ( (res^res2)==0 )
            {
                if (sum > patrick)
                patrick = sum;

            }

        }
     //   cout<<"Case #"<<T<<": "<<patrick<<endl;
     printf("Case #%d: %d \n",T,patrick);

    }
    else
    printf("Case #%d: NO\n",T);


}
int main()
{
    int T,N;
    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    rep(X,T)
    {
        N=0;
        scanf("%d",&N);
        vector<int> v(N);
        rep(i,N)
        {
            scanf("%d",&v[i]);

        }
    run(v,N,X+1);

    }

    return 0;
}
