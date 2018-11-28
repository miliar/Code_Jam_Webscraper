#include <vector>
#include <fstream>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
using namespace std;

#define RET return
#define FOR(i,n) for(int i=0;i<(int)n;++i)
#define SZ(n) ((int)n.size())

#define FORN(i,start,end) for(int i=start;i<end;++i)
#define FORD(i,n) for(int i=(int)n;i>=0;--i)
#define SET(a,n) memset(a,n,sizeof(a))
#define foreach(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define PB push_back

typedef vector<string> VS;
typedef vector<int> VI;
typedef stringstream SS;

#define MAX 101

int main()
{
    int test, line = 1, A, B;
    char input_line[MAX];
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>test;
    while(line <= test ) {
	    fin>>A>>B;
	    fout<<"Case #"<<line<<": ";
	    string str_a, str_b;
	    int ans = 0;
	    FORN(n, A, B) {
			SS ss1;
			ss1<<n;
			string str_n, str_m;
			ss1>>str_n;
			int ln1 = SZ(str_n);
		    FORN(m, n+1, B+1) {
				SS ss2;
				ss2<<m;
				ss2>>str_m;
				int ln2 = SZ(str_m);
				if (ln1 < ln2)
				   break;
	   			string double_m = str_m + str_m;
	   			int index = -1;
				if ((index = double_m.find(str_n)) != -1) {
				   	 ans++;
	   			}  
			}
        }
		fout<<ans<<endl;
		line++;
	}
 	system("pause");
 	return 0;
}
