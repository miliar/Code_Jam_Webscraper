#include "iostream"
#include "fstream"
#include "vector"
#include "string"
#include "map"
using namespace std;

#define SIZE 200

int main()
{
	ifstream ip( "A-small.in" );
	ofstream op( "A-small.out" );
	if( !ip )
	{
		cout<<"Cant open input"<<endl;
		return 1;
	}
	if( !op )
	{
		cout<<"Cant open output"<<endl;
		return 1;
	}

	int count;
	ip>>count;

	for( int itr = 1; itr <= count; ++itr )
	{
		int M,N;
		ip>>N>>M;
		map<string, bool> existmap;
		char junk;
		ip.getline(&junk,1);
		for( int exist = 0; exist < N; ++exist )
		{
			string existdir;
			char ch[SIZE] = {0};
			ip.getline(ch,SIZE,'\n');
			int index = 0;
			while( 0 != ch[index] )
			{
				if( ( '/' == ch[index] ) &&  ( existdir.size() ) )
					existmap[existdir] = 1;
				existdir += ch[index++];
			}
			if( existdir.size() )
				existmap[existdir] = 1;
		}
		long long retval = 0;
		for( int needed = 0; needed < M; ++needed )
		{
			string neededdir;
			char ch[SIZE] = {0};
			ip.getline(ch,SIZE,'\n');
			int index = 0;
			while( 0 != ch[index] )
			{
				if( ( '/' == ch[index] ) &&  ( neededdir.size() ) )
				{
					map<string,bool>::iterator check = existmap.find( neededdir );
					if( check == existmap.end() )
					{
						++retval;
						existmap[ neededdir ] = 1;
					}
				}
				neededdir += ch[index++];
			}
			if( neededdir.size() )
			{
				map<string,bool>::iterator check = existmap.find( neededdir );
				if( check == existmap.end() )
				{
					++retval;
					existmap[ neededdir ] = 1;
				}
			}
		}
		op<<"Case #"<<itr<<": "<<retval<<endl;
	}
	ip.close();
	op.close();
	return 0;
}