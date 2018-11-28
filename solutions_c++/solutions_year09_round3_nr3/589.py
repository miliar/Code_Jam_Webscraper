#include "iostream"
#include "fstream"
#include "string"
#include "vector"
#include "algorithm"
#include "map"
#include "list"
#include "math.h"
using namespace std;

#define FILENAME "C-small-attempt0"

#define PROBLEM_A 0
#define PROBLEM_B 1
#define PROBLEM_C 0

#if PROBLEM_A
int main()
{
	ifstream ip(FILENAME".in");
	ofstream op(FILENAME".out");

	if(!ip)
	{
		cout<<"Cant open input file";
		return -1;
	}
	if(!op)
	{
		cout<<"Cant open output file";
		return -1;
	}

	unsigned int N;
	ip>>N;

	int arr[] = { 1, 0, 2, 3, 4, 5, 6, 7, 8, 9 };
	for(int i=1;i<=N;++i)
	{
		int index = 0;
		string input,backup;
		if( 1 == input.size() )
		{
			op<<"Case #"<<i<<": 0"<<endl;
			continue;
		}
		ip>>input;
		backup = input;
		sort( input.begin(), input.end() );
		string::iterator itr = unique( input.begin(), input.end() );
		input.erase( itr, input.end() );
		int base = input.size();
		if( 1 == base )
			base = 2;
		map<char,int> lukupmap;
		vector<int> lukup(backup.size(), -1 );
		unsigned long long val = 0;
		unsigned long long wt = 1;
		map<char,int>::const_iterator mapitr = lukupmap.end();
		for( int j=0; j<backup.size(); ++j )
		{
			mapitr = lukupmap.find( backup[j] );
			if( lukupmap.end() ==  mapitr )
			{
				lukup[ j ] = arr[ index ];
				lukupmap[ backup[j] ] = arr[ index++ ];
			}
			else
				lukup[ j ] = mapitr->second;
		}
		for( int k=backup.size()-1; k>=0; --k )
		{
			val = val + wt*lukup[k];
			wt *= base;
		}
		op<<"Case #"<<i<<": "<<val<<endl;
	}
	ip.close();
	op.close();
}
#endif 

#if PROBLEM_B
unsigned long long getmoney( const vector<int>& release, const int P )
{
	unsigned long long retval = 0;
	vector<bool> cells( P, true );
	for( int i=0; i<release.size(); ++i )
	{
		int cur = release[i]-1;
		cells[ cur ] = false;
		int fwd = cur + 1;
		int bk = cur - 1;
		while( fwd < P && cells[fwd++] )
			++retval;
		while( bk >= 0 && cells[bk--] )
			++retval;
	}
	return retval;
}
int main()
{
	ifstream ip(FILENAME".in");
	ofstream op(FILENAME".out");

	if(!ip)
	{
		cout<<"Cant open input file";
		return -1;
	}
	if(!op)
	{
		cout<<"Cant open output file";
		return -1;
	}

	int N;
	ip>>N;

	for(int i=1;i<=N;++i)
	{
		int P, Q;
		ip>>P>>Q;
		vector<int> release;
		for( int j=0; j<Q; ++j )
		{
			int tmp;
			ip>>tmp;
			release.push_back( tmp );
		}
		sort( release.begin(), release.end() );
		unsigned long long bestval = P*Q;
		do
		{
			unsigned long long tmp = getmoney( release, P );
			if( bestval > tmp )
				bestval = tmp;
		}while( next_permutation(release.begin(), release.end() ) );
		op<<"Case #"<<i<<": "<<bestval<<endl;
	}
	ip.close();
	op.close();
}
#endif 

#if PROBLEM_C
int main()
{
	ifstream ip(FILENAME".in");
	ofstream op(FILENAME".out");

	if(!ip)
	{
		cout<<"Cant open input file";
		return -1;
	}
	if(!op)
	{
		cout<<"Cant open output file";
		return -1;
	}

	unsigned int N;
	ip>>N;

	for(int i=1;i<=N;++i)
	{
	}
	ip.close();
	op.close();
}
#endif 
