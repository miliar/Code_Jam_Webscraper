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

vector < float > getfloatvectorline()
{
	vector < float > ret;

	string data;
	getline(cin, data);

	stringstream s, debugstream;
	s << data;

	debugstream << "getintvector : ";

	while ( !s.eof() )
	{
		float v;
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

float expected(float currentTyped, float totalCharacters, const vector < float > & probabilities)
{
	if ( currentTyped == 0 )
	{
		return totalCharacters + 1.0;
	}
	float expected_previous = expected(currentTyped-1, totalCharacters, probabilities) + 1;
	float keepTyping = 0.0f;

	{// calc keep
		float all_ok_probability = 1.0;
		for ( int i=0; i<currentTyped; ++i )
		{
			all_ok_probability *= probabilities[i];
		}

		keepTyping = all_ok_probability * (totalCharacters-currentTyped+1.0);
		keepTyping += (1.0-all_ok_probability) * (totalCharacters-currentTyped+1.0+totalCharacters+1.0);
	}

	float enterNow = 1.0 + totalCharacters + 1.0;

	float min = expected_previous < keepTyping ? expected_previous : keepTyping;

	min = min < enterNow ? min : enterNow;

	return min;
}


void doOperation(int caseNo)
{
	vector < int > singleline = getintvectorline();

	int A_currentTypedCharacters = singleline[0];
	int B_totalToTypeCharacters = singleline[1];

	vector < float > probabilities = getfloatvectorline();

	float min = expected(A_currentTypedCharacters, B_totalToTypeCharacters, probabilities);

	cout << "Case #" << caseNo << ": ";
	cout.setf(ios::fixed);
	cout.precision(6);
	cout << min << endl;
}

void init()
{
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

