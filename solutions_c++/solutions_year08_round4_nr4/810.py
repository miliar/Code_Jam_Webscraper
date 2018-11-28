#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>


using namespace std;

#define pb push_back
#define FOR(k,a,b) for(typeof(a) k = (a); k < (b); k++)
#define FORE(k,a,b) for(typeof(a) k = (a); k <= (b); k++)
#define REP(k,b) FOR(k,0,b)
#define ALL(x) (x).begin(),(x).end()
#define RALL(x) (x).rbegin(),(x).rend()
#define tr(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define nl endl
#define ll long long
typedef vector <int> vi;
typedef vector <bool> vb;
typedef vector <string> vs;
typedef vector <char> vc;
typedef vector < vector<int> > vvi;
typedef vector < vector<bool> > vvb;
typedef vector < vector<char> > vvc;
inline string itos(int a){  ostringstream stm;stm << a;return stm.str();}
int dy []= {-1,0,1,0};
int dx []= {0,1,0,-1};
int main()
{
    ofstream fout("ProbDSmall.out");
    ifstream fin("ProbDSmall.in");
    int tt;
    fin >> tt;
    for(int ii=0;ii<tt;ii++)
    {
        int k;
        fin >> k;
        string s;
        fin >> s;
        
        int sz = s.size();
        char arr[s.size()];
        for(int i=0;i<s.size();i++)
            arr[i] = s[i];
      //  cout << s<< " "<<sz;
        int min = 9999;
        vi perm(k);
        for(int i=1;i<=k;i++) perm[i-1] = i;
        do{
            string res = "";
            for(int i=0;i<sz;i+=k)
            {
                for(int j=0;j<k;j++)
                {
                    int p = perm[j];
                    //cout << p << "?";
                    res += s[p-1+i];
                }
            }
            //cout << nl;
            //cout << res << nl;
            int comp = 1;
            for(int j=1;j<sz;j++)
            {
                if(res[j-1]!=res[j])
                    comp++;
            }
            if(comp < min )
            min=comp;
            //break;
        }
        while( next_permutation( ALL(perm) ) );
        
        cout << (min) << nl;
        fout << "Case #" << ii+1 << ": "<< min << nl;
    }

    system("pause");
    return 0;
};
