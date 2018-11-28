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

int main()
{
    int nc;
    cin>>nc;
    forn(tt,nc)
    {
        int n;
        cin>>n;
        vector<string>r(n);
        forn(i,n)cin>>r[i];
        vector<double>cp(n,0),cw(n,0),wp(n,0),owp(n,0),oowp(n,0);
        forn(i,n)forn(j,n)if(r[i][j]!='.')cp[i]++;
        forn(i,n)forn(j,n)if(r[i][j]=='1')cw[i]++;
        forn(i,n)wp[i]=cw[i]/cp[i];
        forn(i,n)
        {
            forn(j,n)if(r[i][j]!='.')
            {
                if(r[i][j]=='1')owp[i]+=cw[j]/(cp[j]-1);
                if(r[i][j]=='0')owp[i]+=(cw[j]-1)/(cp[j]-1);
            }
            owp[i]/=cp[i];
        }
        forn(i,n)
        {
            forn(j,n)if(r[i][j]!='.')
            {
                oowp[i]+=owp[j];
            }
            oowp[i]/=cp[i];
        }
        printf("Case #%d:\n",tt+1);
        forn(i,n)cout<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
    }
}
