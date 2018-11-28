#include "iostream"
#include "fstream"
#include "string"
#include "vector"
#include "algorithm"
#include "map"
#include "list"
#include "math.h"
using namespace std;

#define FILENAME "A-small-attempt1"

#define PROBLEM_A 1
#define PROBLEM_B 0
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
