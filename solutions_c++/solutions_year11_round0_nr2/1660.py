#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
using namespace std;

class Keys 
{
	public:
	Keys(char k1, char k2) : key1(k1), key2(k2) { }
	bool operator<(const Keys &right) const 
	{
		return (key1 < right.key1 && key2 < right.key2);
	}
	char key1;
	char key2;
};

int main()
{
	freopen( "data_in.txt" , "r" , stdin );
	freopen( "data_out.txt" , "w" , stdout );

	int T , C , D , N;

	cin >> T;

	for( int t = 1 ; t <= T ; t ++ )
	{
		cout << "Case #" << t << ": [";

		cin >> C;

		map<std::pair<char,char>,char> c_emt;
		for( int c = 0 ; c < C ; c ++ )
		{
			string c_str;
			cin >> c_str;

			c_emt[ std::make_pair( c_str[ 0 ] , c_str[ 1 ] ) ] =  c_str[ 2 ];
		}

		cin >> D;

		multimap<char,char> d_emt;

		for( int d = 0 ; d < D ; d ++ )
		{
			string d_str;
			cin >> d_str;

			d_emt.insert( pair<char,char>( d_str[ 0 ] , d_str[ 1 ] ) );
			d_emt.insert( pair<char,char>( d_str[ 1 ] , d_str[ 0 ] ) );
		}

		cin >> N;

		vector<char> cur_emt;
		for( int n = 0 ; n < N ; n ++ )
		{
			char cc;
			cin >> cc;

			bool insert = true;

			if( cur_emt.size() >= 1 )
			{
				map<std::pair<char,char>,char>::iterator it1 = c_emt.find( std::make_pair( cur_emt[ cur_emt.size() - 1 ]  , cc ) );

				if( it1 != c_emt.end() )
				{
					cur_emt[ cur_emt.size() - 1 ] = it1->second;
					insert = false;
				}
				
				map<std::pair<char,char>,char>::iterator it2 = c_emt.find( std::make_pair( cc , cur_emt[ cur_emt.size() - 1 ] ) );

				if( it2 != c_emt.end() )
				{
					cur_emt[ cur_emt.size() - 1 ] = it2->second;
					insert = false;
				}
			}
			
			if( insert && d_emt.find( cc ) != d_emt.end() )
			{
				set<char> tmp_set;
				for( int i = 0 ; i < cur_emt.size() ; i ++ )
					tmp_set.insert( cur_emt[ i ] );

				pair<multimap<char,char>::iterator,multimap<char,char>::iterator> ret = d_emt.equal_range( cc );

				for(multimap<char,char>::iterator it=ret.first; it!=ret.second; ++it)
				{
					if( tmp_set.find( (*it).second ) != tmp_set.end() )
					{
						insert = false;
						cur_emt.clear();
						break;
					}
				}
			}
			
			if( insert )
				cur_emt.push_back( cc );
		}

		if( cur_emt.size() >= 1 )
		{
			cout << cur_emt[ 0 ];
			for( int i = 1 ; i < cur_emt.size() ; i ++ )
				cout << ", " << cur_emt[ i ];
		}
		cout << "]\n";
	}
	return 0;
}