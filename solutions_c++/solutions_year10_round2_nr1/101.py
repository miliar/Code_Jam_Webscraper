#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <sstream>
#include <queue>

#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>

#define forn(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define ALL(x)   (x).begin(),(x).end()
#define SIZE(x)   (int)(x).size()
#define SORT(x) sort(ALL(x))
using namespace std;
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
typedef long long ll;
// NUNCA DEFINIR int max....
vector<int> vec[110010];
map<string,bool> seen;
map<string,int> indice;
int ind;




int main()
{
    int casos;
    ifstream ifs("A-large.in", ifstream::in );
    ofstream ofs("A-large.txt");
    ifs >> casos;

    for( int t = 0 ; t < casos; t++ )
    {
        seen.clear();

        int hay, poner;
        ifs >> hay >> poner;
        //cout << hay << poner << endl;
        seen["/"] = true;
        seen[""] = true;
        for( int i = 0 ; i < hay ; i ++ )
        {
            string s;
            ifs >> s;
            s += '/';
            string name;
            for( int j = 0 ; j < s.size(); j ++ )
            {
                if( s[j] == '/' )
                {
                    seen[name] = true;
          //          cout << name << endl;
                }
                name += s[j];

            }
        }

        int res = 0 ;
        for( int i = 0 ; i < poner; i ++ )
        {
            string s;
            ifs >> s;
            s += '/';
            string name;

            for( int j = 0 ; j < s.size(); j ++ )
            {
                if( s[j] == '/' )
                {

                    if( !(seen[name] == true) )
                    {
            //            cout << name << endl;
                        res++;
                        seen[name] = true;
              //          cout << " res " << res << endl;

                    }
                }
                name += s[j];

            }
        }

        ofs << "Case #" << (t+1) << ": " << res << "\n";
    }
    return 0;
}

