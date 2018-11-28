// codejam minscalar.cpp
#include<iostream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cctype>
#include<climits>
#include<cfloat>

using namespace std;

int main()
{
    int t;
    cin >> t;
    int c = 1;
    while( t-- )
    {
        cout << "Case #" << c << ": ";
	int n;
	cin >> n;
	vector<int> v1( n );
	for( int i = 0; i < n; i++ )
	    cin >> v1[i];
	vector<int> v2( n );
	for( int i = 0; i < n; i++ )
	    cin >> v2[i];
	sort( v1.begin(), v1.end() );
	sort( v2.begin(), v2.end() );
	reverse( v2.begin(), v2.end() );
	int x = 0; 
	for( int i = 0; i < n; i++ )
	    x += ( v1[i] * v2[i] );
	cout << x << endl;
	c++;
	
    }
    return 0;
}
