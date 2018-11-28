
#include <map>
#include <climits>
#include <set>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define DBG(e) cout<<(#e)<<" : "<<e<<endl
#define FOR(i,s,e) for(int i=(s);i<(e);i++)
#define CLEAR(v,i) memset(v,i,sizeof v)
#define ALL(x) x.begin(),x.end()
#define pb  push_back
#define pr pair<int,int>
#define SZ(x) int((x).size())


typedef long long LL;
bool win(char,vector<string>);
int main()
{
    int tests;
    cin>>tests;
    FOR(tt,1,tests+1)
    {
        vector<string>mat;
        bool point=0;
        FOR(j,0,4)
        {
            string s;
            cin>>s;
            FOR(i,0,4) if(s[i]=='.') point=1;
            mat.pb(s);
        }
        cout<<"Case #"<<tt<<": ";
        if(win('X',mat)) cout<<"X won";
        else if(win('O',mat)) cout<<"O won";
        else if(point) cout<<"Game has not completed";
        else cout<<"Draw";
        cout<<"\n";
    }
}
bool win(char player,vector<string>mat)
{
    bool state=0;
    /*
    Check for the columns
    */

    FOR(i,0,4)
    {
        map<char,int>mp;
        FOR(j,0,4) mp[mat[i][j]]++;
        if(mp[player]>=3)
        {
            if(mp['T'] || mp[player]==4) state=1;
        }
    }
    /*
    Check for the rows
    */
    FOR(i,0,4)
    {
        map<char,int>mp;
        FOR(j,0,4) mp[mat[j][i]]++;
        if(mp[player]>=3)
        {
            if(mp['T'] || mp[player]==4) state=1;
        }
    }

    /*
        Check for the diagonals
    */
    {
        map<char,int>mp;
        FOR(i,0,4) mp[mat[i][i]]++;
        if(mp[player]>=3)
        {
            if(mp['T'] || mp[player]==4) state=1;
        }
    }

    {
        map<char,int>mp;
        int i=0,j=3;
        while(i<4)
        {
            mp[mat[i][j]]++;
            i++,j--;
        }
        if(mp[player]>=3)
        {
            if(mp['T'] || mp[player]==4) state=1;
        }
    }
    return state;
}
