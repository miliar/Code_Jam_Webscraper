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

void doOperation(int caseNo)
{
char ttable[256] = { 0, };
ttable[' '] = ' ';
ttable['y'] = 'a';
ttable['n'] = 'b';
ttable['i'] = 'd';
ttable['l'] = 'g';
ttable['w'] = 'f';
ttable['k'] = 'i';
ttable['o'] = 'k';
ttable['u'] = 'j';
ttable['x'] = 'm';
ttable['m'] = 'l';
ttable['s'] = 'n';
ttable['v'] = 'p';
ttable['p'] = 'r';
ttable['j'] = 'u';
ttable['r'] = 't';
ttable['t'] = 'w';
ttable['q'] = 'z';
ttable['z'] = 'q';
ttable['a'] = 'y';
ttable['b'] = 'h';
ttable['c'] = 'e';
ttable['d'] = 's';
ttable['e'] = 'o';
ttable['f'] = 'c';
ttable['g'] = 'v';
ttable['h'] = 'x';
	string line = getstringline();

	char result[256] = { 0, };
	int index = 0;

	for ( size_t i=0; i<line.size(); ++i )
	{
		result[i] = ttable[line[i]];
	}

	cout << "Case #" << caseNo << ": " << result << endl;
}

int main(int argc, char * [])
{
	DP << "Start testing..." << endl;

	int numberOfCase = getintline();

	for ( int i=0; i<numberOfCase; ++i )
	{
		doOperation(i+1);
	}
	return 0;
}

