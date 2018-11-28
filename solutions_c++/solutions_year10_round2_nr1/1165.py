# include <iostream>
# include <string>
# include <algorithm>
# include <sstream>
# include <cmath>
# include <cstdio>
# include <vector>

# define loop(i, a, b) for(int i=a ; i<b ; ++i)
# define puke(v, i) loop(i, 0, v.size()) cout << v[i] << " " ;
# define dpuke(v, i, j) loop(i, 0, v.size()) { puke(v[i], j) cout << endl ; } 
# define lastel(v) v[v.size()-1]
# define bigint unsigned long long int
# define here cout << "here\n" ;

using namespace std ;

vector<string> oldpaths, newpaths ;

int maxsim(int x)
{
	int ret, maxret=0 ;
	loop(i, 0, oldpaths.size())
	{//cout << "i is: " << i << " " ;
		ret = -1 ;
		for(int j=0 ; j<newpaths[x].size(), j<oldpaths[i].size() ; ++j)
		{//cout << newpaths[x][j] ;
			if(newpaths[x][j] != oldpaths[i][j]) break ;
			if(newpaths[x][j] == '/') ret++ ;
		}//cout << endl ;
		if(ret > maxret) maxret = ret ;
	}
	return maxret ;
}

int main()
{
	int tc ; cin >> tc ; int TC = tc ;
	while(TC--)
	{
		int N, M ; cin >> N >> M ;
		int mkdirs=0 ;
		loop(i, 0, N) { string s ; cin >> s ; s += '/' ; oldpaths.push_back(s) ; }
		loop(i, 0, M) { string s ; cin >> s ; s += '/' ; newpaths.push_back(s) ; }
//		dpuke(oldpaths, i, j) ;
//		cout << endl ;
//		dpuke(newpaths, i, j) ;
		loop(i, 0, M)
		{
			int c = count(newpaths[i].begin(), newpaths[i].end(), '/')-1 ; //cout << "count is: " << c << endl ;
			mkdirs += c - maxsim(i) ; //cout << "maxsim is: " << maxsim(i) << endl ;
			oldpaths.push_back(newpaths[i]) ;
		}
		cout << "Case #" << tc-TC << ": " << mkdirs << endl ;
		oldpaths.clear() ; newpaths.clear() ;
	}
	return 0 ;
}

