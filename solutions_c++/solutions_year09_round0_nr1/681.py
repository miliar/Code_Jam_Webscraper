#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/io.hpp>

using namespace std;
boost::numeric::ublas::matrix<double> m;

vector<string> dict;

typedef vector<string> StringVect;

class Match
{
	public:
	StringVect expr;
	Match(StringVect& s)
	{
		expr = s;
	}

	bool operator() ( const string & dictword ) const
	{
		// cout << expr << endl;
		for(int i = 0;i<dictword.size();i++)
		{
			if (expr[i].find(dictword[i])==string::npos)
				return 0;
		}
		return 1;
	}
};


int main()
{
	int LanguageLength,DictionaryEntries,N;
	string dummy;
	cin >> LanguageLength >> DictionaryEntries >> N;
	getline(cin, dummy);

	// Read known words
	for (int d = 0; d<DictionaryEntries; d++)
	{
		string word;
		getline(cin, word);
		// cout << word << endl;
		dict.push_back(word);
	}

	for(int n = 0;n<N; n++)
	{
		string line;
		getline(cin, line);

		StringVect expr;
		for(int i = 0; i<line.size();i++)
		{
			string alternatives;

			if (line[i]!='(')
			{
				alternatives ="X";
				alternatives[0]=line[i];
			}
			else
			{
				i++;

				for(; line[i]!=')'; )
					alternatives.push_back( line[i++] );
					;
				
			}

			// cout << alternatives << endl;
			expr.push_back(alternatives);
		}
		cout << "Case #" << n+1<<": "<< count_if( dict.begin(),dict.end(), Match( expr ) ) <<endl;
	}
	return 0;
}
