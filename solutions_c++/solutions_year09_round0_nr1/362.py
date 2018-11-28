#include <cstdio>
#include <iostream>
#include <iomanip>
#include <set>
#include <vector>
using namespace std;


int main()
{
       int i,j ,k;
       set<char> S[20];
       vector<string> vec;
       int L, D, N;
       cin >> L >> D >> N;
       for( i = 0 ; i < D; i ++ ) { string s; cin >> s; vec.push_back(s); }
       for( int h = 1; h <= N ; h ++ )
       {
	      string s;cin >> s;
	      for( i =0 ; i < 20; i ++ ) S[i].clear();
	      for( i = 0 ; i < L; i++ )
	      {
		     if( s[0] != '(') S[i].insert(s[0]), s = s.substr(1);
		     else
		     {
			    int ind = 1;
			    while( s[ind] != ')' )
			    {
				   S[i].insert(s[ind++]);
			    }
			    s = s.substr(ind+1);
		     }
	      }
	      int res = 0 ;
	      for( i = 0 ; i < vec.size() ; i ++ )
	      {
		     int sum = 1;
		     for( j = 0 ; j < vec[i].size(); j ++ ) if( !S[j].count(vec[i][j]) ) sum = 0;
		     res+= sum;
	      }
	      cout << "Case #" << h << ": " << res << endl;
       }
       return 0;
}
