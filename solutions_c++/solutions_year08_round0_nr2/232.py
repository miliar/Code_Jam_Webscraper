#include <iostream>
#include <vector>
#include <set>
#include <string>

using namespace std;

class trip
{
public:
	int start;
	int end;
	int type;

	trip(int p_s, int p_e, int p_t)
	{
		start = p_s;
		end = p_e;
		type = p_t;
	}

	bool operator<(const trip &t) const
	{
		if( start != t.start )
			return start < t.start;
		return type > t.type;
	}
};

int make_time( string &s)
{
	int h, m;
	sscanf(s.c_str(), "%d:%d", &h, &m);
	return 60*h+m;
}

int main()
{
	int N;
	cin >> N;
	for(int n = 1; n <= N; n++)
	{
		int T;
		string s, t;
		cin >> T;
		int NA, NB;
		cin >> NA >> NB;

		multiset< trip > S;
		for(int i = 0; i < NA; i++)
		{
			cin >> s >> t;
			S.insert( trip( make_time( s ), make_time( t ), 0) );
		}

		for(int i = 0; i < NB; i++)
		{
			cin >> s >> t;
			S.insert( trip( make_time( s ), make_time( t ), 1) );
		}

		int resA = 0, resB = 0;
		int avA = 0, avB = 0;
		while( S.size() )
		{
			trip p = *S.begin();
			S.erase( S.begin() );

			switch(p.type)
			{
			case 0:
				if( avA )
					avA--;
				else
					resA++;

				S.insert( trip( p.end + T, 0, 3) );
				break;
			case 1:
				if( avB )
					avB--;
				else
					resB++;

				S.insert( trip( p.end + T, 0, 2) );
				break;
			case 2:
				avA++;
				break;
			case 3:
				avB++;
				break;
			}
		}

		cout << "Case #" << n << ": " << resA << ' ' << resB << endl;
	}
}