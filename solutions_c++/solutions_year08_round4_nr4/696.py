#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>  
using namespace std;


#define INF (int)1e9
#define PB push_back
#define SZ(a) ((int)((a).size()))
#define FOR(i,a,b) for(int i = a; i < (b); ++i)
#define FORE(it,x) for(typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define ALL(a) (a).begin(),(a).end()
#define CLR(a,v) memset((a),(v),sizeof(a))
#define FINDA(c,x) ((c).find(x) != (c).end()) 
#define FIND(c,x) (find(ALL(c),x) != (c).end()) 

typedef pair<int,int> II; 
typedef stringstream ss;
typedef long long ll;
typedef long double ld;
typedef vector<string> VS;
typedef vector<int> VI;
typedef vector<II> VII;
typedef vector< VI > VVI;

int en(string s)
{
    char last='#';
    int ret=0;
    for(int i=0;i<SZ(s);++i)
        if(s[i]!=last)
        {
         last=s[i];
         ret++;   
        }
    return ret;
}

int main()
{
    ifstream fin;
    fin.open("C:\\data\\D-small-attempt0.in");
    ofstream fout;
    fout.open("C:\\data\\ds.txt");
    int t;
    fin>>t;
    int cas;
    int k;
    string s;
    for(int cas=1;cas<=t;++cas)
    {
        fin>>k;
        fin>>s;
        vector<int> p(k);
        for(int i=0;i<k;++i)
            p[i]=i;
        int best=INF;
        do
        {
        string ret(SZ(s),' ');
        for(int b=0;b<SZ(s);b+=k)
            for(int j=0;j<k;++j)
                ret[b+j]=s[b+p[j]];
        
         best<?=en(ret);
                     
        }while(next_permutation(ALL(p)));
        fout<<"Case #"<<cas<<": "<<best<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}

