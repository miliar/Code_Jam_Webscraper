#include <vector>
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

#define sz(a) (LL)a.size()
#define all(a) a.begin(), a.end()
#define pb push_back
typedef vector <int> vi;
typedef vector <string> vs;
typedef pair<int, int> pii;
#define LL long long
#define INF 1000000

vs split(const string& s, const string& delim = " ") { vector<string> res; string t; for ( unsigned int i = 0 ; i != s.size() ; i++ ) { if ( delim.find( s[i] ) != string::npos ) { if ( !t.empty() ) { res.push_back( t ); t = ""; } } else { t += s[i]; } } if ( !t.empty() ) { res.push_back(t); } return res; }

int n, m;
bool ans;
char A[55][55];
char B[55][55];

void process()
{
    ans = true;
    int i, j;
    for (i=0; i<n; i++) for (j=0; j<m; j++) B[i][j]=A[i][j];
    for (i=0; i<n; i++) for (j=0; j<m; j++) if (B[i][j]=='#')
    {
        if (i==n-1||j==m-1) { ans=false; return; }
        if (B[i+1][j]!='#') { ans=false; return; }
        if (B[i][j+1]!='#') { ans=false; return; }
        if (B[i+1][j+1]!='#') { ans=false; return; }
        B[i][j]=B[i+1][j+1]='/';
        B[i+1][j]=B[i][j+1]='\\';
    }
}

int main()
{
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "r", stdin);
	
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0b.out", "w", stdout);

    //freopen("A-small-attempt1.in", "r", stdin);
    //freopen("A-small-attempt1.out", "w", stdout);
     
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int numtest, test, i, j;
	cin >> numtest;

	for (test=1; test<=numtest; test++)
	{
        cin >> n >> m;
        ans = true;
        for (i=0; i<n; i++) for (j=0; j<m; j++) cin >> A[i][j];
        process();
        cout << "Case #" << (test) << ":\n";
        if (!ans)
        {
            cout << "Impossible\n";
            //for (i=0; i<n; i++) { for (j=0; j<m; j++) cout << A[i][j]; cout << endl; }
        }
        else
        {
            for (i=0; i<n; i++) { for (j=0; j<m; j++) cout << B[i][j]; cout << endl; }
        }
	}
	return 0;
}
