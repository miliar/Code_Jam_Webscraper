#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<map>
#include<set>
#include<cmath>

using namespace std;

#define mp make_pair
#define pb push_back
#define forn(i,n) for(int i=0;i<(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

int dx[4]={1,1,0,1};
int dy[4]={0,1,1,-1};

int main()
{
    int t,n,k;
    cin>>t;
    forn(nc,t)
    {
        cin>>n>>k;
        string s;
        vector<string>vs,vr;
        forn(i,n)
        {
            cin>>s;
            vs.pb(s);
        }
        forn(i,n)
        {
            s="";
            forn(j,n)
            {
                if(vs[n-i-1][n-j-1]!='.')s.pb(vs[n-i-1][n-j-1]);
            }
            while(s.size()<n)s.pb('.');
            vr.pb(s);
        }
        bool gr=false,gb=false;
        forn(i,n)forn(j,n)
        {
            forn(m,4)
            {
                bool g=true;
                forn(l,k)
                {
                    if(i+l*dx[m]<n && j+l*dy[m]<n && i+l*dx[m]>=0 && j+l*dy[m]>=0)g=g&(vr[i+l*dx[m]][j+l*dy[m]]=='R');else g=false;
                }
                if(g)gr=true;
                g=true;
                forn(l,k)
                {
                    if(i+l*dx[m]<n && j+l*dy[m]<n && i+l*dx[m]>=0 && j+l*dy[m]>=0)g=g&(vr[i+l*dx[m]][j+l*dy[m]]=='B');else g=false;
                }
                if(g)gb=true;
            }
        }
        if(!gr && !gb)cout<<"Case #"<<nc+1<<": Neither"<<endl;
        if(!gr && gb)cout<<"Case #"<<nc+1<<": Blue"<<endl;
        if(gr && !gb)cout<<"Case #"<<nc+1<<": Red"<<endl;
        if(gr && gb)cout<<"Case #"<<nc+1<<": Both"<<endl;
    }
}
