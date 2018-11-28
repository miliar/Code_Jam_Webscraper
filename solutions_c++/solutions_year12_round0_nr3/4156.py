#include <exception>

#include <iostream>
#include <fstream>
#include <sstream>

#include <string>
#include <vector>
#include <map>

#include <algorithm>
#include <iterator>



using namespace std;


typedef vector<int> vint;
typedef vector<long> vlong;
typedef vector<string> vstr;

typedef pair<long,long> lpair;

inline long str_to_long(string in)
{
	return stol(in);
}


/*******************************************************/

int get_num_recycled(const long A, const long B) throw(...)
{
	if( A>B )
		throw exception("A>B");

	map<lpair,int> recycled_pairs;

	for(long n=A; n<=B; ++n)
	{
		stringstream ss;
		ss << n;
		
		string n_str = ss.str();
		string m_str = n_str;

		int str_len = n_str.length();
		for(int i=1; i<str_len; ++i)
		{
			m_str = m_str[str_len-1] + m_str.substr(0, str_len-1);

			if(m_str[0]=='0')
				continue;

			long m = stol(m_str);
			if( m>n && m<=B )
				recycled_pairs[lpair(n,m)] = 1;
		}
	}

	return recycled_pairs.size();
}


/*******************************************************/



int main(int argc, char** argv)
try
{
	if( argc!=3 )
		throw exception("must specify filename",1);



	string fname(argv[1]);
	ifstream fin(fname);
	if( !fin.is_open() )
		throw exception("unable to open file");

	fname = argv[2];
	ofstream fout;
	fout.open(fname);


	string line;

	// number of test cases
	int T;
	getline(fin, line);
	T = stoi(line);

	for( int i=0; i<T; ++i )
	{
		vlong input;
		getline(fin, line);
		transform( istream_iterator<string>(istringstream(line)),
					istream_iterator<string>(),
					back_inserter< vlong >(input),
					str_to_long );

		if( input.size()!=2 )
			throw exception("incorrect number of inputs in line");

		long A = input[0];
		long B = input[1];


		long num_recycled = get_num_recycled(A, B);


		fout << "Case #" << (i+1) << ": " << num_recycled << endl;
	}


	fin.close();
	fout.close();
}
catch( exception& e )
{
	cout << "**** Error -- " << e.what() << " ****\n";
	exit(1);
}
catch( ... )
{
	cout << "ERROR!\n";
	exit(1);
}