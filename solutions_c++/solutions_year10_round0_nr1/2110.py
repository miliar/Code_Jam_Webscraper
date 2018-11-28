# include <iostream>
# include <string>
# include <vector>
# include <algorithm>
# include <cstdio>
# include <cmath>
# include <sstream>

# define loop(i, a, b) for(int i=a ; i<b ; ++i)
# define puke(v, i) loop(i, 0, v.size()) cout << v[i] << endl
# define puke2(v, i, j) loop(i, 0, v.size()) puke(v[i], j)
# define bigint unsigned long long int
# define addall(v, i, c) loop(i, 0, v.size()) c+= v[i]

using namespace std ;

int main()
{
	int powers[] = {2, 4, 8, 16, 32} ;
	int TC, tc ; cin >> TC ; tc = TC ;
	while(tc--)
	{
		int N, thePower ; bigint K ;
		cin >> N >> K ;
//		for(int i=4 ; i>=0,powers[i]>N ; --i) thePower=powers[i] ;
		thePower = pow(2, N) ;
		if((K+1)%thePower == 0) cout << "Case #" << TC-tc << ": " << "ON\n" ;
		else cout << "Case #" << TC-tc << ": " << "OFF\n" ;
	}
	return 0 ;
}
