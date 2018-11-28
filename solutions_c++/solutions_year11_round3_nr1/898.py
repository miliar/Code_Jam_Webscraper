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
#include <queue>
using namespace std;

#define GI ({int t ;scanf("%d",&t);t;})
#define FORZ(i,n) for(typeof(n)i=0;i<n;i++)
#define all(x) (x).begin(), (x).end()
#define PB push_back
#define sz size()
#define FF first
#define SS second
#define pr(x) cout<<#x<<" : "<<x<<endl<<flush; 
typedef vector<int> VI;
typedef long long LL;
typedef unsigned long long uLL;
typedef pair<int,int> pII;
typedef pair<string,int> pSI;
typedef map<int,int> mII;
typedef map<string,int> mSI;
typedef vector<string> VS;


int main ()
{
	int T = GI;
	
	FORZ (t, T) {
		int r, c;
		cin >> r >> c;
		
		char tile[r][c];
		
		FORZ (i, r)
			FORZ (j, c)
				cin >> tile[i][j];
				
		FORZ (i, r) {
			FORZ (j, c) {
				if (tile[i][j] == '#' && j + 1 < c && tile[i][j + 1] == '#' && i + 1 < r && tile[i + 1][j] == '#' && i + 1 < r && j + 1 < c && tile[i + 1][j + 1] == '#') {
					tile[i][j] = '/'; tile[i][j + 1] = '\\'; tile[i + 1][j] = '\\'; tile[i + 1][j + 1] = '/';
				}	
			}			
		}	
		
		bool can = true;
		FORZ (i, r) {
			FORZ (j, c) {
				if (tile[i][j] == '#')
					can = false;
				}			
			}	
		
		if (!can)
			printf ("Case #%d:\nImpossible\n", t + 1);
			
		else {
			printf ("Case #%d:\n", t + 1);
			FORZ (i, r) {
				FORZ (j, c) {
					cout << tile[i][j];
				}			
				cout << "\n";
			}	
		}	
				
	}
	
	return 0;
}


