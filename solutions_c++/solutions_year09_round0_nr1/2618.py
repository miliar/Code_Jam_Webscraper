#include "iostream"
#include "fstream"
#include "string"
#include "vector"
#include "algorithm"
#include "map"
using namespace std;

#define FILENAME "A-Small"

#define PROBLEM_1 1
#define PROBLEM_2 0
#define PROBLEM_3 0
#define PROBLEM_4 0
#define PROBLEM_5 0

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

#if PROBLEM_4
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

#if PROBLEM_5
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

