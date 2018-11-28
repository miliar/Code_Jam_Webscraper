#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
#include<queue>
#include<complex>
#include<set>
#include<map>
#include<sstream>
#include<string>
#include<deque>
#include<sys/time.h>
#include<fstream>
#include<bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define dforn(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()
#define sq(x) ((x)*(x))
#define pi (4*atan(1))

int dp[20000];

int main()
{
    int T;
    cin>>T;
    forn(t,T)
    {
        int n;
        cin>>n;
        vector<int> dd(n),l(n);
        forn(i,n)
        {
            cin>>dd[i]>>l[i];
        }
        int d;
        cin>>d;
        forn(i,20000)dp[i]=-1;
        dp[0]=dd[0];
        forn(i,n)if(i)
        {
            forn(j,i)
            {
                if(dp[j]>=dd[i]-dd[j])
                {
                    dp[i]=max(dp[i],min(dd[i]-dd[j],l[i]));
                }
            }
        }
        //forn(i,n)cout<<dp[i]<<endl;
        bool sirve=false;
        forn(i,n)if(dp[i]+dd[i]>=d)sirve=true;
        if(sirve)
        {
            cout<<"Case #"<<t+1<<": YES"<<endl;
        }else
        {
            cout<<"Case #"<<t+1<<": NO"<<endl;
        }
    }
}
