#include <iostream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

template <typename T>
void print(vector<T> a)
{
	cout << "[";
	for (size_t i = 0 ; i < a.size() ; ++i)
	{
		cout << (i > 0 ? "," : "") << a[i];
	}
	cout << "]" << endl;
}

vector< vector<char> > split_digit_set(size_t n, string s)
{
	vector< vector<char> > result;
	for (size_t i = 0 ; i < n ; ++i)
		result.push_back( vector<char>() );

	size_t x = 0;
	bool in_brace = false;
	for (size_t i = 0 ; i < s.length() ; ++i)
	{
		if ( s[i] == '(' )
			in_brace = true;

		if ( s[i] == ')' )
			in_brace = false;

		if ( s[i] != '(' && s[i] != ')' ) 
		{
			result[x].push_back(s[i]);
		}

		if ( result[x].size() > 0 && ! in_brace )
		{
			x++;
		}
	}

	return result;
}

bool is_matched(string word, const vector< vector<char> > & patterns)
{
	if ( word.length() != patterns.size() )
		return false;

	for (size_t i = 0 ; i < word.length() ; ++i)
	{
		vector<char>::const_iterator it = find(
				patterns[i].begin(), patterns[i].end(), word[i] );

		if ( it == patterns[i].end() )
			return false;
	}
	return true;
}

size_t count_matched_word(
	const vector<string> & words, 
	const vector< vector<char> > & patterns )
{
	size_t count = 0;
	for (size_t i = 0 ; i < words.size() ; ++i )
	{
		if ( is_matched( words[i], patterns ) )
			count++;
	}
	return count;
}

int main( int argc, char ** argv )
{
	size_t nDigits, nWords, nCase;
	cin >> nDigits >> nWords >> nCase;

	vector<string> words;
	words.reserve( nWords );

	for (size_t i = 0 ; i < nWords ; ++i)
	{
		string s;
		cin >> s;
		words.push_back(s);
	}

	for (size_t i = 0 ; i < nCase ; ++i)
	{
		string s;
		cin >> s;
		vector< vector<char> > patterns = split_digit_set( nDigits, s );
		cout << "Case #" << i + 1;
	    cout << ": " << count_matched_word(words, patterns ) << endl;
	}

	return 0;
}

