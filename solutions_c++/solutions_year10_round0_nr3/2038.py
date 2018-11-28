# include <iostream>
# include <vector>

# define loop(i, a, b) for(int i=a ; i<b ; ++i)
# define puke(v, i) loop(i, 0, v.size()) cout << v[i] << endl
# define puke2(v, i, j) loop(i, 0, v.size()) puke(v[i], j)
# define bigint unsigned long long int
# define addall(v, i, c) loop(i, 0, v.size()) c+= v[i]

using namespace std ;

int main()
{
	int TC, tc, N ;
	cin >> TC ; tc = TC ;
	bigint R, k ;
	vector<bigint> groups ;
	
	while(tc--)
	{
		cin >> R >> k >> N ;
		bigint totalQueue=0 ;
		loop(i, 0, N)
		{
			bigint gi ; cin >> gi ;
			groups.push_back(gi) ;
			totalQueue += gi ;
		}
		if(totalQueue < k) { cout << "Case #" << TC-tc << ": " << totalQueue*R << endl ; groups.clear() ; continue ; }
		int gsize = groups.size() ;
		vector<pair<int, bigint> > dpMem ;
		bigint currentTotal=0, counter=0 ;
		loop(i, 0, 2*N)
		{
			currentTotal += groups[i%gsize] ;
//			cout << "currtot is: " << currentTotal << " and i is: " << i << endl ;
			if((currentTotal + groups[(i+1)%gsize]) > k)
			{
				dpMem.push_back(make_pair((i+1)%gsize, currentTotal)) ;
				currentTotal -= groups[(counter++)%gsize] ;
				if((currentTotal + groups[(i+1)%gsize]) > k)
				{
					currentTotal -= groups[i%gsize] ;
					i-- ;
				}
			}
			if(counter == N) break ;
		}
//		cout << "memory size: " << dpMem.size() << endl ;
//		loop(i, 0, dpMem.size()) cout << dpMem[i].first << " " << dpMem[i].second << endl ;
		
		bigint gtotal=0 ;
		int nowat=0 ;
		loop(i, 0, R)
		{
			gtotal += dpMem[nowat].second ;
			nowat = dpMem[nowat].first ;
		}
		
		cout << "Case #" << TC-tc << ": " << gtotal << endl ;
		groups.clear() ; dpMem.clear() ; cin.clear() ;
	}
	return 0 ;
}
