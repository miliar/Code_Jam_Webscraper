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
	int tc ; cin >> tc ; int TC = tc ;
	while(TC--)
	{
		int N ; cin >> N ;
		vector<pair<int, int> > wires ;
		loop(i, 0, N)
		{
			int temp1, temp2 ; cin >> temp1 >> temp2 ;
			pair<int, int> tempp = make_pair(temp1, temp2) ;
			wires.push_back(tempp) ;
		}
		wires.clear() ;
		
		int count = 0 ;
		loop(i, 0, N)
		{
			loop(j, 0, N)
			{
				if((wires[i].first-wires[j].first)*(wires[i].second-wires[j].second) < 0) count++ ;
			}
		}
		cout << "Case #" << tc-TC << ": " << count/2 << endl ;
	}
	return 0 ;
}
