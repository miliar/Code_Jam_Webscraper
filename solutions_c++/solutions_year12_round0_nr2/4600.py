// http://algospot.com/discussion/369/google-code-jam-round-1a-%ED%92%80%EC%9D%B4/p1
#include <algorithm>
#include <vector>
#include <stack>
#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

stringstream emptyOut;

#define DP_ON 0

#if DP_ON
#define DP std::cout << "[DebugPrint]:"
#else
#define DP emptyOut
#endif

const int CANNOT_GO = -1;

int getintline()
{

	string data;
	getline(cin, data);

	stringstream s;
	s << data;

	int ret;
	s >> ret;

	return ret;
}

vector < int > getintvectorline()
{
	vector < int > ret;

	string data;
	getline(cin, data);

	stringstream s, debugstream;
	s << data;

	debugstream << "getintvector : ";

	while ( !s.eof() )
	{
		int v;
		s >> v;

		debugstream << " " << v;

		ret.push_back(v);
	}
	DP << debugstream.str().c_str() << endl;

	return ret;
}

string getstringline()
{
	string data;
	getline(cin, data);

	return data;
}

struct P2
{
	int max1;
	int max2;
};

vector < P2 > g;

P2 getV(int input)
{
	if ( g[input].max1 >= 0 ) return g[input];

	P2 result;

	int v = input/3;

	vector < int > r;
	r.push_back(v);
	r.push_back(v);
	r.push_back(v);

	int current = r[0] + r[1] + r[2];

	result.max1 = -1;
	result.max2 = -1;

	if ( current < input )
	{
		r[2] = r[2] + 1;
	}
	current = r[0] + r[1] + r[2];

	if ( current < input )
	{
		r[1] = r[1] + 1;
	}

	result.max1 = result.max2 = r[2];

	bool bChanged = false;
	for ( int i=0; i<3; ++i )
	{
		for ( int j=0; j<3; ++j )
		{
			if ( i == j ) continue;

			if ( r[i] == r[j] && r[i] != 0 )
			{
				DP << "same found" << endl;
				r.push_back(r[0]);
				r.push_back(r[1]);
				r.push_back(r[2]);
				r[3+i] = r[3+i] - 1;
				r[3+j] = r[3+j] + 1;

				result.max2 = r[3+j];
			
				bChanged = true;
				break;
			}
		}

		if ( bChanged ) break;
	}

	for ( int i=0; i<r.size(); ++i )
	{
		DP << "r[" << i << "] : " << r[i] << endl;
	}
	g[input] = result;
	return result;
}

void doOperation(int caseNo)
{
	vector < int > singleline = getintvectorline();

	int N_numberOfGooglers = singleline[0];
	int S_numberOfSurprising = singleline[1];
	int p = singleline[2];

	int answer = 0;

	P2 * points = new P2[N_numberOfGooglers];

	for ( size_t i=0; i<N_numberOfGooglers; ++i )
	{
		points[i] = getV(singleline[i+3]);
		DP << "before points " << points[i].max1 << "," << points[i].max2 << endl;

		if ( points[i].max1 < p && points[i].max2 >= p 
				&& S_numberOfSurprising > 0 )
		{
			--S_numberOfSurprising;

			points[i].max1 = points[i].max2;
		}
		DP << "after points " << points[i].max1 << "," << points[i].max2 << endl;
	}

	for ( size_t i=0; i<N_numberOfGooglers; ++i )
	{
		if ( points[i].max1 >= p )
		{
			++answer;
		}
	}

	cout << "Case #" << caseNo << ": " << answer << endl;

	delete [] points;
}

void init()
{
	DP << "init..." << endl;

	g.resize(31);

	for ( int i=0; i<= 30; ++i )
	{
		g[i].max1 = -1;
		g[i].max2 = -1;
	}
}

int main(int argc, char * [])
{
	DP << "Start testing..." << endl;

	init();

	int numberOfCase = getintline();

	for ( int i=0; i<numberOfCase; ++i )
	{
		doOperation(i+1);
	}
	return 0;
}

