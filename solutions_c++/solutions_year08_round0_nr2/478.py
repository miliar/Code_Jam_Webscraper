#include<iostream>
#include<vector>
#include<list>
#include<algorithm>

using namespace std;

class TripTime
{
public:
	int departure;
	int arrival;
};

inline bool TT_lessthan(TripTime &x, TripTime &y)
{
	return x.departure < y.departure;
}

int main()
{
	int N;
	cin >> N;

	for(int n=1; n <= N; ++n)
	{
		int T;
		cin >> T;

		int NA, NB;
		cin >> NA >> NB;

		vector<TripTime> tripFromA(NA), tripFromB(NB);

		for(int i=0; i < NA; ++i)
		{
			int h, m;
			char sep;

			cin >> h >> sep >> m;
			tripFromA[i].departure = h*60 + m;

			cin >> h >> sep >> m;
			tripFromA[i].arrival = h*60 + m;
		}

		for(int i=0; i < NB; ++i)
		{
			int h, m;
			char sep;

			cin >> h >> sep >> m;
			tripFromB[i].departure = h*60 + m;

			cin >> h >> sep >> m;
			tripFromB[i].arrival = h*60 + m;
		}

		//	----  //

		sort( tripFromA.begin(), tripFromA.end(), TT_lessthan );
		sort( tripFromB.begin(), tripFromB.end(), TT_lessthan );

		list<int> availatA, availatB;

		int numTrainsFromA=0, numTrainsFromB=0;

		int i=0, j=0;

		while( i < NA && j < NB)
		{
			if( tripFromA[i].departure < tripFromB[j].departure )
			{
				if( availatA.size() && (availatA.front() <= tripFromA[i].departure) )
					availatA.pop_front();
				else
					++numTrainsFromA;

				list<int>::iterator pos = upper_bound( availatB.begin(), availatB.end(), tripFromA[i].arrival + T );
				availatB.insert( pos, tripFromA[i].arrival + T );

				++i;
			}

			else if( tripFromA[i].departure > tripFromB[j].departure )
			{
				if( availatB.size() && (availatB.front() <= tripFromB[j].departure) )
					availatB.pop_front();
				else
					++numTrainsFromB;

				list<int>::iterator pos = upper_bound( availatA.begin(), availatA.end(), tripFromB[j].arrival + T );
				availatA.insert( pos, tripFromB[j].arrival + T );

				++j;
			}

			else
			{
				if( availatA.size() && (availatA.front() <= tripFromA[i].departure) )
					availatA.pop_front();
				else
					++numTrainsFromA;

				if( availatB.size() && (availatB.front() <= tripFromB[j].departure) )
					availatB.pop_front();
				else
					++numTrainsFromB;

				list<int>::iterator pos;

				pos = upper_bound( availatB.begin(), availatB.end(), tripFromA[i].arrival + T );
				availatB.insert( pos, tripFromA[i].arrival + T );

				pos = upper_bound( availatA.begin(), availatA.end(), tripFromB[j].arrival + T );
				availatA.insert( pos, tripFromB[j].arrival + T );

				++i;
				++j;
			}
		}

		while(i < NA)
		{
			if( availatA.size() && (availatA.front() <= tripFromA[i].departure) )
				availatA.pop_front();
			else
				++numTrainsFromA;

			++i;
		}

		while(j < NB)
		{
			if( availatB.size() && (availatB.front() <= tripFromB[j].departure) )
				availatB.pop_front();
			else
				++numTrainsFromB;

			++j;
		}

		cout << "Case #" << n << ": " << numTrainsFromA << " " << numTrainsFromB << endl;
	}

	return 0;
}