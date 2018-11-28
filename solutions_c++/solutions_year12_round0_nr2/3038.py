#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <map>

using namespace std;
int S, p;
std::vector<int> total;


int solv()
{
	sort(total.begin(), total.end(), greater<int>() );
	
	int ans = 0;
	for( size_t i=0; i<total.size(); i++ ){
		int t = total[i];
		int maxv = t/3;
		int mod = t%3;
		
		if( t != 0 ){
			if( mod > 0 )
				maxv++;
			
			if( mod != 1 && maxv < p && S > 0 ){
				maxv++;
				S--;
			}
		}		
		
		if( maxv < p )
			break;
		
		ans++;
	}
	
	return ans;
}


int main()
{
	FILE *fin = fopen( "../../input.txt", "rt" );
	FILE *fout = fopen( "../../out.txt", "wt" );
//	FILE *fout = stdout;
	
	int tc = 0;
	fscanf( fin, "%d\n", &tc );
	
	for( int i=1; i<=tc; i++ )
	{
		int n;
		fscanf( fin, "%d %d %d", &n, &S, &p );
		
		total.clear();
		for( int j=0; j<n; j++ ){
			int t = 0;
			fscanf( fin, "%d", &t );
			total.push_back( t );
		}

		fscanf( fin, "\n" );
		fprintf( fout, "Case #%d: %d\n", i, solv() );
	}
	
    return 0;
}