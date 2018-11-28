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

int cnt(vector<int> v)
{
    bool anda;
    forn(o,v.size())
    {
        anda=true;
        forn(i,v.size()-o)if(v[i+o]!=v[v.size()-i-1])anda=false;
        if(anda)return o;
    }
}

int cntr(vector<int> v)
{
    reverse(all(v));
    return cnt(v);
}

int m[500][500],mm[500][500];

int main()
{
    int T;
    cin>>T;
    forn(t,T)
    {
        int r;
        forn(i,500)forn(j,500)m[i][j]=0;
        cin>>r;
        int x1,x2,y1,y2;
        forn(k,r)
        {
            cin>>x1>>y1>>x2>>y2;
            forn(i,1+x2-x1)forn(j,1+y2-y1)m[x1+i][y1+j]=1;
        }
        bool hay=true;
        int res=0;
        while(hay)
        {
            res++;
            hay=false;
            forn(i,110)forn(j,110)mm[i][j]=0;
            forn(i,110)forn(j,110)if(m[i][j])
            {
                if((i && m[i-1][j]) || (j && m[i][j-1])){mm[i][j]=1;hay=true;}
            }
            forn(i,110)forn(j,110)if(!m[i][j])
            {
                if((i && m[i-1][j]) && (j && m[i][j-1])){mm[i][j]=1;hay=true;}
            }
            forn(i,110)forn(j,110)m[i][j]=mm[i][j];
        }
        cout<<"Case #"<<t+1<<": "<<res<<endl;
    }
    return 0;
}
