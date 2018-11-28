#include <iostream>
#include <vector>
#include <fstream>
#include <utility>
#include <algorithm>

using namespace std;

#define MP make_pair
#define PB push_back
#define SZ(a) ((int)((a).size()))
#define FOR(i,n) for(int i=0; (i)<(n); (i)++)
#define ALL(a) (a).begin(),(a).end()

typedef vector<vector<int> > VVI;
typedef vector<int> VI;
typedef pair<int, int> II;
typedef long long LL;


int main()
{
    ifstream be("A-large.in");
    ofstream ki("ki.txt");
    int t;
    be>>t;
    FOR(i,t)
    {
        vector<vector<char> > table;
        int r,c;
        be>>r>>c;
        FOR(j,r)
        {
            vector<char> v;
            FOR(k,c)
            {
                char ch;
                be>>ch;
                v.PB(ch);
            }
            table.PB(v);
        }

        bool jo=true;
        for(int j=0;(j<r-1)&&jo;j++)
        {
            for(int k=0;(k<c-1)&&(jo);k++)
            {
                if(table[j][k]=='#')
                {
                    jo=(table[j+1][k]=='#')&&(table[j][k+1]=='#')&&(table[j+1][k+1]=='#');
                    if(jo)
                    {
                        table[j][k]='/';
                        table[j+1][k]=92;
                        table[j][k+1]=92;
                        table[j+1][k+1]='/';
                    }
                }
            }
            if(jo)
            {
                jo=(table[j][c-1]!='#');
            }
        }
        for(int k=0;k<c&&(jo);k++)
        {
            jo=(table[r-1][k]!='#');
        }

        ki<<"Case #"<<i+1<<":"<<endl;

        if(jo)
        {
            FOR(j,r)
            {
                FOR(k,c)
                {
                    ki<<table[j][k];
                }
                ki<<endl;
            }
        }else
        {
            ki<<"Impossible"<<endl;
        }

    }
    ki.close();
    be.close();

    return 0;
}
