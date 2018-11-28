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
typedef vector<string> vstr;



inline int str_to_int(string in)
{
	return stoi(in);
}


/*******************************************************/

vint init_bestres_nosurprise()
{
	vint bestres(31, 0);

	for(int i=3; i<=30; ++i)
	{
		int q = i / 3;
		int r = i % 3;

		bestres[i] = q + (r>0 ? 1 : 0);
	}

	return bestres;
}

vint init_bestres_surprise()
{
	vint bestres(31, 0);

	for(int i=4; i<=30; ++i)
	{
		int q = i / 3;
		int r = i % 3;

		bestres[i] = q + (r>0 ? r : 1);
		if(bestres[i]>10)
			bestres[i] = 10;
	}

	return bestres;
}



inline int bestres_nosurprise(const int total)
{
	static vint bestres = init_bestres_nosurprise();
	return bestres[total];
}

inline int bestres_surprise(const int total)
{
	static vint bestres = init_bestres_surprise();
	return bestres[total];
}


int get_max_scorers(const int N, const int S, const int p, const vint& t) throw(...)
{

	if( t.size()!=N )
		throw exception("get_max_scorers -- score vector doesn't match number of Googlers");

	int n_achieve_nosurprise = 0;
	int n_achieve_surprise = 0;


	// find number who could have gotten a best result of p without surprises and number who
	// could do so only if they got a surprising result
	for( int i=0; i<N; ++i )
	{
		const int t_i = t[i];
		if( bestres_nosurprise(t_i)>=p )
			++n_achieve_nosurprise;
		else if( bestres_surprise(t_i)>=p )
			++n_achieve_surprise;
	}

	return n_achieve_nosurprise + min(n_achieve_surprise, S);
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
		vint input;
		getline(fin, line);
		transform( istream_iterator<string>(istringstream(line)),
					istream_iterator<string>(),
					back_inserter< vint >(input),
					str_to_int );

		int N = input[0];
		int S = input[1];
		int p = input[2];
		vint t(input.begin()+3, input.end());


		int max_scorers = get_max_scorers(N, S, p, t);


		fout << "Case #" << (i+1) << ": " << max_scorers << endl;
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