#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <algorithm>
#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <complex>

using namespace std;

int print_dbg = 1;

#define d_print(x) { if(print_dbg){  cerr << __LINE__ << " " << #x << " = " << x << endl; cerr.flush(); } }

typedef vector<string> vecs;
typedef vector<int> veci;
typedef unsigned long long ull;
typedef long long ll;

#define ALL(x) (x).begin(), (x).end()
#define IN(x,y) ((x).find((y)) != (x).end())


vector<string> expand( const string & input, string delimiters = " \t")
{
	#define string_find(del,k) ((del).find((k)) != string::npos)
	vector<string> out;
	size_t begin = 0;
	size_t i;
	for( i = 0; i < input.length( ); i++ )
	{
		if( i > 0 && string_find( delimiters, input[i] ) && !string_find( delimiters, input[i-1] ) )
		{
			out.push_back( input.substr( begin, i - begin ) );
			begin = i+1 ;
		}
		else
		{
			if( string_find( delimiters, input[i] ) ){ begin = i+1; }
		}
	}
	if( begin < i )
	{
		out.push_back( input.substr( begin ) );
	}
	return out;
}

bool cmp( const pair<pair<int,int>,int > & a, const pair<pair<int,int>,int > & b )
{
	//return ( a.first.second - a.first.first ) > (b.first.second - b.first.first );
	return a.second < b.second;
}

bool cmp2( const pair<pair<int,int>,int > & a, const pair<pair<int,int>,int > & b )
{
	//return ( a.first.second - a.first.first ) > (b.first.second - b.first.first );
	return a.first.first < b.first.first;
}


int main( int argc, char ** argv )
{
	//string p = "A";
//	freopen("sample.in","r",stdin);freopen("sample.out","w",stdout);

	//  freopen((p + "-small-attempt0.in").c_str(),"r",stdin);freopen((p + "-small-attempt0.out").c_str(),"w",stdout);
	//  freopen((p + "-small-attempt1.in").c_str(),"r",stdin);freopen((p + "-small-attempt1.out").c_str(),"w",stdout);
	//  freopen((p + "-small-attempt2.in").c_str(),"r",stdin);freopen((p + "-small-attempt2.out").c_str(),"w",stdout);
	//  freopen((p + "-large.in").c_str(),"r",stdin);freopen((p + "-large.out").c_str(),"w",stdout);

	if( argv[1] == "q" ) print_dbg = 0;

	int T;
	cin>>T;
	for( int CASE = 1; CASE <= T; ++CASE )
	{
		int X, S, R, N;
		double t;
		cin>>X>>S>>R>>t>>N;
		vector<pair<pair<int,int>,int > > walkways;
		vector<bool> covered(X+1, false );
		double left = X;
		for( int i = 0; i < N; ++i )
		{
			int B,E,W;
			cin>>B>>E>>W;
			walkways.push_back( make_pair( make_pair(B,E),W));
			left -= E - B;
			//for( int j =B; j <= E; ++j )
		//	{
			//	covered[j] = true;
		//	}
		}
		sort( ALL(walkways), cmp );




		//double left = X;
		double time = 0;

		if( left > 0 )
				{
					if( t > 0 )
					{
						double tt = left / double(R);
						if( tt >= t )
						{
						//	cout<<"FUCK"<<endl;
						//	d_print(tt);
						//	d_print(t);
							double d = double(left) - double(R) * t ;
						//	d_print(d);
							tt = t + d / double(S);
						//	d_print(tt);
							t = 0;
						}
						t -= tt;
						time += tt;
					}
					else
					{
						time += left / double(S);
					}
				}


		for( int i = 0; i < walkways.size(); ++i )
		{
			int length =abs(  walkways[i].first.second - walkways[i].first.first );

			double speed = double(S) + walkways[i].second;
			double tt = double(length)/speed;
			if( t > 0 )
			{
				speed = double(R) + walkways[i].second;
				tt = double(length)/speed;
				if( tt >= t )
				{
					//cout<<"SHIT"<<endl;
					double d = double(length) - (speed*t);
					tt = t + d / ( double(S) + walkways[i].second );
					t = 0;
				}
				else
				{
					t -= tt;
				}
			}

			time += tt;
			//d_print( time );
			//d_print(tt);
			//left -= length;
		}
		//d_print(left);
		//d_print(t);
	//	d_print(time);


		//cout<<"Case #"<<CASE<<": "<<time<<endl;
		//printf("%.2lf\n", answer);
		printf( "Case #%i: %.8lf\n", CASE, time );
	}

}
