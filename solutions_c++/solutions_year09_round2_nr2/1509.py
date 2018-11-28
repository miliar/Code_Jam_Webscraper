#include "iostream"
#include "fstream"
#include "string"
#include "vector"
#include "algorithm"
#include "map"
#include "list"
using namespace std;

#define FILENAME "B-small-attempt1"

#define PROBLEM_A 1
#define PROBLEM_B 0
#define PROBLEM_C 0

#if PROBLEM_A
void getDigits( unsigned int itr, vector<int>& vec )
{
	int index = vec.size() - 1;
	while( itr )
	{
		int digit = itr %10;
		itr /= 10;
		if( digit )
			vec[ index-- ] = digit;
	}
}
unsigned long long int makeNumber( const vector<int>& actual )
{
	unsigned long long retval = 0;
	for( unsigned int i=0; i<actual.size(); ++i )
	{
		retval *= 10 ;
		retval += actual[ i ];
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

	unsigned int T;
	ip>>T;

	for(int i=1;i<=T;++i)
	{
		unsigned long long N, retval;
		ip>>N;
		retval = N;
		vector<int> actual(11, 0);
		getDigits( N, actual );
		vector<unsigned long long> vec;
		do
		{
			unsigned long long next = makeNumber( actual );
			if( next > N )
			{
				retval = next;
				break;
			}
		}while( next_permutation( actual.begin(), actual.end() ) );
		op<<"Case #"<<i<<": "<<retval<<endl;
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
class wrker
{
public:
	wrker(){};
	wrker( const wrker& other )
	{
		val = other.val;
		exp = other.exp;
		x = other.x;
		y = other.y;
	}
	int val, x, y;
	string exp;
};
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
		unsigned int W, Q;
		ip>>W>>Q;
		vector< vector<char> > sqr;
		list<wrker *> listwrker;
		map<int, wrker> resultstore;
		for( unsigned int w1=0; w1 < W; ++w1 )
		{
			vector<char> tmp;
			for( unsigned int w2=0; w2 < W; ++w2 )
			{
				char ch;
				ip>>ch;
				tmp.push_back( ch );
				wrker onelistitem;
				if( ch >= '0' && ch <= '9' )
				{
					onelistitem.val = ch - '0' ;
					onelistitem.exp += ch;
					onelistitem.x = w2;
					onelistitem.y = w1;
					listwrker.push_back( new wrker(onelistitem) );
				}
			}
			sqr.push_back( tmp );
		}

		vector<int> queries;
		for( unsigned int q1=0; q1<Q; ++q1 )
		{
			int qry;
			ip>>qry;
			queries.push_back( qry );
		}
		vector<int>::const_iterator end = queries.end();
		vector<int>::const_iterator begin = queries.begin();
		vector<int>::const_iterator itr = end;
		int foundsize = 100;
		while( !listwrker.empty() )
		{
			wrker cur = *listwrker.front();
			if( cur.exp.size() > foundsize )
				break;
			listwrker.erase( listwrker.begin() );
			if( end == ( itr = find( begin, end, cur.val ) ) )
			{
				if( cur.x > 0 )
				{
					wrker next( cur );
					--next.x;
					char ch = sqr[next.y][next.x];
					next.exp += ch;
					if( isdigit(ch) )
					{
						char op = sqr[cur.y][cur.x];
						if( '+' == op )
							next.val += ch - '0';
						else
							next.val -= ch - '0';
					}
					listwrker.push_back( new wrker(next) );
				}
				if( cur.x + 1 < W )
				{
					wrker next( cur );
					++next.x;
					char ch = sqr[next.y][next.x];
					next.exp += ch;
					if( isdigit(ch) )
					{
						char op = sqr[cur.y][cur.x];
						if( '+' == op )
							next.val += ch - '0';
						else
							next.val -= ch - '0';
					}
					listwrker.push_back( new wrker(next) );
				}
				if( cur.y > 0 )
				{
					wrker next( cur );
					--next.y;
					char ch = sqr[next.y][next.x];
					next.exp += ch;
					if( isdigit(ch) )
					{
						char op = sqr[cur.y][cur.x];
						if( '+' == op )
							next.val += ch - '0';
						else
							next.val -= ch - '0';
					}
					listwrker.push_back( new wrker(next) );
				}
				if( cur.y + 1 < W )
				{
					wrker next( cur );
					++next.y;
					char ch = sqr[next.y][next.x];
					next.exp += ch;
					if( isdigit(ch) )
					{
						char op = sqr[cur.y][cur.x];
						if( '+' == op )
							next.val += ch - '0';
						else
							next.val -= ch - '0';
					}
					listwrker.push_back( new wrker(next) );
				}
			}
			else
			{
				map<int,wrker>::const_iterator resultitr = resultstore.find( *itr );
				if( resultstore.end() == resultitr )
				{
					resultstore[ *itr ] = cur;
					if( resultstore.size() == Q )
						foundsize = cur.exp.size();
				}
				else
				{
					wrker existingresult = resultitr->second;
					if( existingresult.exp > cur.exp )
					{
						resultstore[ *itr ] = cur;
						if( resultstore.size() == Q )
							foundsize = cur.exp.size();
					}
				}
			}
		}
		op<<"Case #"<<i<<":"<<endl;
		for( unsigned int res=0; res < Q; ++res )
		{
			map<int, wrker>::const_iterator itr = resultstore.find( queries[res] );
			if( resultstore.end() == itr )
				op<<""<<endl;
			else
			{
				wrker printer = itr->second;
				op<<printer.exp<<endl;
			}
		}
	}
	ip.close();
	op.close();
}
#endif 
