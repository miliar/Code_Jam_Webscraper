#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>


using namespace std;

long long l,t,n,c;


int inp[1000007];
int my[1000007];
vector<int> myv;


int main()
{
freopen("db.in","r",stdin);
freopen("db.out","w",stdout);
int dt,ti;
cin>>dt;
for(ti=1;ti<=dt;ti++)
{
    cin>>l>>t>>n>>c;
    for(int i=0;i<c;i++)
    {
        cin>>inp[i];
        int j=1;
        while(j*c<=n)
        {
            if((j*c+i)<n) inp[j*c+i]=inp[i];
            j++;
        }
    }
    //for(int i=0;i<=n;i++) cout<<":"<<inp[i]<<"x";


    int myt=t/2;
    int res=0;int res2=0;
    int myi=0;
    while(myt!=0 && myi<n)
    {
        res2+=inp[myi];
        if(res2<=myt){ res+=inp[myi];myi++;}
        else
        {
            res=myt;
            inp[myi]=res2-myt;
            break;
        }
    }
    res=res*2;
    //cout<<myi<<":x\n";

    int myn=n-myi;
    myv.clear();
    for(int i=myi;i<n;i++) myv.push_back(inp[i]*-1);
    sort(myv.begin(),myv.end());
    //for(int i=myi;
    int myl=l;
    for(int i=0;i<myv.size();i++)
    {
        if(myl!=0) res=res-myv[i];
        else res=res-2*myv[i];
        if(myl!=0) myl--;
    }

    cout<<"Case #"<<ti<<": "<<res<<endl;




}

return 0;
}
