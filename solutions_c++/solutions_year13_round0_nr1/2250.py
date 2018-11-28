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
#define forn(i,n) for(int i=0;i<(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

typedef long long int tint;

int main()
{
    int T;
    cin>>T;
    forn(t,T)
    {
        vector<string>v(4);
        forn(i,4)cin>>v[i];
        string res;
        int win=0;
        forn(i,4)
        {
            bool w=true;
            forn(j,4)if(v[i][j]!='X' and v[i][j]!='T')w=false;
            if(w)win=1;
            w=true;
            forn(j,4)if(v[i][j]!='O' and v[i][j]!='T')w=false;
            if(w)win=2;
        }
        forn(j,4)
        {
            bool w=true;
            forn(i,4)if(v[i][j]!='X' and v[i][j]!='T')w=false;
            if(w)win=1;
            w=true;
            forn(i,4)if(v[i][j]!='O' and v[i][j]!='T')w=false;
            if(w)win=2;
        }
        bool w=true;
        forn(i,4)if(v[i][i]!='X' and v[i][i]!='T')w=false;
        if(w)win=1;
        w=true;
        forn(i,4)if(v[i][i]!='O' and v[i][i]!='T')w=false;
        if(w)win=2;
        w=true;
        forn(i,4)if(v[i][3-i]!='X' and v[i][3-i]!='T')w=false;
        if(w)win=1;
        w=true;
        forn(i,4)if(v[i][3-i]!='O' and v[i][3-i]!='T')w=false;
        if(w)win=2;
        if(win==0)res="Draw";
        if(win==1)res="X won";
        if(win==2)res="O won";
        if(res=="Draw")
        {
            forn(i,4)forn(j,4)if(v[i][j]=='.')
                    res="Game has not completed";
        }
        cout<<"Case #"<<t+1<<": "<<res<<endl;
        getline(cin,res);
    }
    return 0;
}
