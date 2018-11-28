#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>
#include <cctype>
#include <vector>
#include <cassert>
#include <iomanip>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
typedef pair<int,int> PI;
#define dbg(x) cout << #x << " -> " << (x) << "\t";
#define dbge(x) cout << #x << " -> " << (x) << "\n";
const int mn=64;
string mat[mn];
int N;
int main()
{
	int kase_;
	cin >> kase_;
	for ( int kase=1;kase<=kase_;kase++ )
	{
		cin >> N;
		for ( int i=0;i<N;i++ ) cin >> mat[i];
		
		int result = 0;
		for ( int i=0;i<N;i++ )
		{
			bool good = true;
			for ( int j=i+1;j<N;j++ ) if ( mat[i][j] == '1' )
				good = false;
			
			if ( good ) continue;
			for ( int j=i+1;j<N;j++ )
			{
				for ( int k=i+1;k<N;k++ ) if ( mat[j][k] == '1' ) goto next;
				// foun
				for ( int k=j;k>i;k-- ) 
				{
					swap ( mat[k] , mat[k-1] );
					result ++;
				}
				break;
				next:;
			}
		}
		cout <<"Case #" << kase <<": " << result << endl;
	}
	return 0;
}
