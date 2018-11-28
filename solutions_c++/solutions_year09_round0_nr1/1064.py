#include <iostream>
#include <vector>
using namespace std;

const int mn = 5001 , mprod = 15;
string dict[mn];
int L,D,N;

/*
The first line of input contains 3 integers, L, D and N separated by a space. D lines follow, each containing one word of length L. These are the words that are known to exist in the alien language. N test cases then follow, each on its own line and each consisting of a pattern as described above. You may assume that all known words provided are unique.
*/
int main()
{
	cin >> L >> D >> N;
	for ( int i=0;i<D;i++ )
		cin >> dict[i];

	for ( int kase=1;kase<=N;kase++ )
	{
		vector < string > prod;
		int res = 0;
		string token;
		cin >> token;
		for ( int j=0;j<token.length();j++ )
		{
			if ( token[j] == '(' )
			{
				string t;
				j++;
				while ( token[j] !=')' )
					t+=token[j++];
				prod.push_back(t);
			}
			else
				prod.push_back(string(1,token[j]));
		}
	
		for ( int i=0;i<D;i++ )
		{
			string pres = dict[i];			
			if ( prod.size() != dict[i].length() )
				continue;
				
			int l=pres.length();
			int cand = 0;
			for ( int j=0;j<l;j++ ) 
			{
				char req = pres[j];
				for ( int k=0;k<prod[j].length();k++ ) if ( prod[j][k] == req ) 
				{
					cand ++;
					break;
				}
			}
			
			if ( cand == l )
				res ++;
		}
		cout << "Case #" << kase <<": " << res << endl;
	}
	return 0;
}
