#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <algorithm>
#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>

using namespace std;

#define d_print(x) cout<<#x<<"="<<(x)<<endl;

typedef vector<string> vecs;
typedef unsigned long long ull;
typedef long long ll;

#define in(x,y) ((x).find((y)) != (x).end())

double simulate( vector<int> & boosters, vector<ll> & dists, double t )
{
	int N = boosters.size();
	double time = 0;
	int star = 0;
	while( star != N )
	{
		double speed_to_next = 0.5;
		double dist_to_next = dists[star];
		double time_to_next = dist_to_next / speed_to_next;

		if( boosters[star] == 1 )
		{
			if( t < ( time + time_to_next) )
			{
				if( t < time )
				{
					speed_to_next = 1.0;
				}
				else
				{
					double slow_time = t - time;
					double slow_dist = slow_time * 0.5;
					double fast_time = ( double( dists[star] ) - slow_dist );
					time += slow_time;
					speed_to_next = 1.0;
					dist_to_next =  ( double( dists[star] ) - slow_dist );
				}
			}
		}

			time += dist_to_next / speed_to_next;

		star++;
	}
	return time;
}

int main( int argc, char ** argv )
{
	int T;
	cin>>T;
	for( int CASE = 1; CASE <= T; ++ CASE  )
	{
		ll L,t,N,C;
		cin>>L>>t>>N>>C;
		vector<ll> a;
		for( int i = 0; i < C; ++i )
		{
			ll z;
			cin>>z;
			a.push_back(z);
		}
		if( a.size() < N )
		{
			int z = a.size();
			int k = z;
			while( a.size() != N )
			{
				a.push_back(a[k%z]);
				++k;
			}
		}
		for( int i = 0; i < a.size(); ++i )
		{
		//	cout<<a[i]<<" ";
		}
		//cout<<endl;

		vector<int> boosters(N, 0);
		for( int i = 0; i < L; ++i )
		{
			boosters[i] = 1;
		}
		double min_time = ll(1)<<40;
		sort( boosters.begin(), boosters.end() );
		while( true )
		{
			for( int i = 0; i < boosters.size(); ++i )
			{
		//		cout<<boosters[i]<<" ";
			}
		//	cout<<endl;
			double sim = simulate( boosters, a, t  );
		//	cout<<sim<<endl;
			min_time = min( sim, min_time );
			if( ! next_permutation( boosters.begin(), boosters.end() ))
			{
				break;
			}
		}
		cout<<"Case #"<<CASE<<": "<<ll(min_time)<<endl;

	}
}
