#include "iostream"
#include "fstream"
#include "string"
#include "vector"
#include "algorithm"
#include "map"
using namespace std;

#define FILENAME "C-Small"

#define PROBLEM_1 0
#define PROBLEM_2 0
#define PROBLEM_3 1

#if PROBLEM_1
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

	int L,D,N;
	ip>>L>>D>>N;

	vector<string> dict;
	for(int i=1;i<=D;++i)
	{
		string str;
		ip>>str;
		dict.push_back( str );
	}
	for(int j=1; j<=N; ++j)
	{
		string str;
		ip>>str;
		vector< string > onecase;
		string inbrace;
		for( unsigned int k=0; k<str.size(); ++k )
		{
			switch( str[k] )
			{
			case '(':
				inbrace = '(';
				break;
			case ')':
				{
					inbrace.erase( inbrace.begin() );
					onecase.push_back( inbrace );
					inbrace.clear();
				}
				break;
			default:
				if( inbrace.empty() )
				{
					string tmp;
					tmp.push_back( str[k] );
					onecase.push_back( tmp );
				}
				else
					inbrace = inbrace + str[k];
				break;
			}
		}
		int retval = 0; 
		for( unsigned int itrwords=0; itrwords < dict.size(); ++itrwords )
		{
			bool done = false;
			for( unsigned int itrchars = 0; !done && itrchars < L; ++itrchars )
			{
				if(onecase.size() <= itrchars )
					done = true;
				else if( onecase[itrchars].end() == find(onecase[itrchars].begin(), onecase[itrchars].end(), dict[itrwords][itrchars]) )
					done = true;
			}
			if( !done )
				++retval;
		}
		op<<"Case #"<<j<<": "<<retval<<endl;
	}

	ip.close();
	op.close();
}
#endif 

#if PROBLEM_2
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

#if PROBLEM_3
string wtcj = "welcome to code jam";

void countphrase( vector< vector<int> >& allindices, int cur, int curlocation, int& count )
{
	if( cur >= wtcj.size() )
	{
		++count;
		count = count % 10000;
		return;
	}

	vector<int> currentChar = allindices[ cur ];
	for( unsigned int i=0; i<currentChar.size(); ++i )
	{
		if( currentChar[i] > curlocation )
			countphrase( allindices, cur+1, currentChar[i], count );
	}
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
	char buffer[550];
	ip>>N;
	ip.getline((char *)buffer,550);

	for(int i=1;i<=N;++i)
	{
		vector< vector<int> > allindices( wtcj.size(), vector<int>() );
		memset( buffer, 0, 550 );
		ip.getline((char *)buffer,550);
		string str( buffer );
		for( unsigned int j=0; j<str.size(); ++j )
		{
			switch( str[j] )
			{
			case 'w':
				allindices[ 0 ].push_back( j );
				break;
			case 'e':
				allindices[ 1 ].push_back( j );
				allindices[ 6 ].push_back( j );
				allindices[ 14 ].push_back( j );
				break;
			case 'l':
				allindices[ 2 ].push_back( j );
				break;
			case 'c':
				allindices[ 3 ].push_back( j );
				allindices[ 11 ].push_back( j );
				break;
			case 'o':
				allindices[ 4 ].push_back( j );
				allindices[ 9 ].push_back( j );
				allindices[ 12 ].push_back( j );
				break;
			case 'm':
				allindices[ 5 ].push_back( j );
				allindices[ 18 ].push_back( j );
				break;
			case ' ':
				allindices[ 7 ].push_back( j );
				allindices[ 10 ].push_back( j );
				allindices[ 15 ].push_back( j );
				break;
			case 't':
				allindices[ 8 ].push_back( j );
				break;
			case 'd':
				allindices[ 13 ].push_back( j );
				break;
			case 'j':
				allindices[ 16 ].push_back( j );
				break;
			case 'a':
				allindices[ 17 ].push_back( j );
				break;
			default:
				break;
			}
		}
		int retval = 0;
		countphrase( allindices, 0, -1, retval );
		sprintf(buffer,"Case #%d: %4.4d\n",i,retval);
		op<<buffer;
	}

	ip.close();
	op.close();
}
#endif 
