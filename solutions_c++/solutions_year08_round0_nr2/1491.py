#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

struct A
{
	int start;
	int end;
	int count;
};

bool Cmp( A & a, A & b)
{
	if( a.start != b.start)
		return a.start < b.start;
	if( a.end != b.end)
		return a.end < b.end;
	return a.count < b.count;
}




int main()
{
	ifstream in ( "input.txt" , ifstream::in );
	ofstream out ( "output.txt" , ifstream::out );
	vector<A> trains;
	int n ;
	in >> n ;
	const int lim = 24 * 60 ;
	int m[lim+1][2] ;

	for( int casen = 0 ; casen < n ; ++casen )
	{
		trains.clear();
		int t ;
		in >> t;

		int na, nb ;
		in >> na >> nb;

		for( int i = 0 ; i <= lim ; ++i)
		{
			m[i][0] = m[i][1] = 0;
		}
		int atob = 0;
		int btoa = 0;

		for( int i = 0 ; i < na ; ++i)
		{
			string cur ;
			in >> cur;
			int froms,fromm, tos,tom;
			sscanf(cur.c_str(),"%d:%d",&fromm,&froms);
			in >> cur;
			sscanf(cur.c_str(),"%d:%d",&tom,&tos);
			
			int from = fromm * 60 + froms;
			int to = tom * 60 + tos;

			A a;
			a.start = from;
			a.end = to;
			a.count = 0;
			trains.push_back(a);
		}

		for( int i = 0 ; i < nb ; ++i)
		{
			string cur ;
			in >> cur;
			int froms,fromm, tos,tom;
			sscanf(cur.c_str(),"%d:%d",&fromm,&froms);
			in >> cur;
			sscanf(cur.c_str(),"%d:%d",&tom,&tos);
			
			int from = fromm * 60 + froms;
			int to = tom * 60 + tos;

			A a;
			a.start = from;
			a.end = to;
			a.count = 1;
			trains.push_back(a);

		}

		sort(trains.begin(),trains.end(),Cmp);

		for( int i = 0 ; i < trains.size();++i)
		{
			int from = trains[i].start;
			int to = trains[i].end;

			// we are from a to b.
			if( trains[i].count == 0 )
			{
				if( m[from][0] > 0)
				{
					for( int j = from ; j <= lim ; ++j)
					{
						m[j][0]--;
					}

					for( int j = to + t ; j <= lim ; ++j) 
					{
						m[j][1]++;
					}
				}
				else
				{
					atob++;
					for( int j = to + t ; j <= lim ; ++j) 
					{
						m[j][1]++;
					}
				}
			}
			else
			{
				// we are from b to a now.
				if( m[from][1] > 0)
				{
					for( int j = from ; j <= lim ; ++j)
					{
						m[j][1]--;
					}

					for( int j = to + t ; j <= lim ; ++j) 
					{
						m[j][0]++;
					}
				}
				else
				{
					btoa++;
					for( int j = to + t ; j <= lim ; ++j) 
					{
						m[j][0]++;
					}
				}
			}

		}

		out << "Case #" << casen + 1 << ": " << atob << " " << btoa << endl; 


	}



	
	
	
	
	getchar();
	return 0;
}
