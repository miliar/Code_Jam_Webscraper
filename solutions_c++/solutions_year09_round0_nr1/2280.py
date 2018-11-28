#include <iostream>
#include <fstream>

#include <string>

#include <vector>
#include <set>

using namespace std;

class e_token
{
public:
	e_token()
		: _alphabet('z' - 'a' + 1, false)
	{
	}
	e_token(const e_token& e)
		: _alphabet(e._alphabet)
	{
	}
	e_token(const string& s)
		: _alphabet('z' - 'a' + 1, false)
	{
		for(int i = 0; i < s.size(); ++i)
			this->_alphabet[int(s[i])] = true;
	}

	inline void reset(const string& s)
	{
		this->_alphabet.clear();
		this->_alphabet.resize('z' - 'a' + 1, false);
		for(int i = 0; i < s.size(); ++i)
			this->_alphabet[s[i] - 'a'] = true;
	}

	inline bool match_letter(char c) const
	{
		return this->_alphabet[c - 'a'];
	}


private:
	vector<bool> _alphabet;
};

class e_pattern
{
public:
	e_pattern()
		: _str_pat()
		, _pat_size(0)
		, _tokens()
	{}
	e_pattern(const e_pattern& e)
		: _str_pat(e._str_pat)
		, _pat_size(e._pat_size)
		, _tokens(e._tokens)
	{}

	inline int get_size() const
	{
		return this->_pat_size;
	}
	inline void set_size(int s)
	{
		this->_pat_size = s;
	}
	inline const string& get_pat() const
	{
		return this->_str_pat;
	}
	inline void set_pat(const string& p)
	{
		this->_str_pat = p;
	}

	bool match_word(const string& w) const
	{
		for(int i = 0; i < w.size(); ++i)
		{
			if( !this->_tokens[i].match_letter(w[i]) )
				return false;
		}
		return true;
	}

	void tokenize()
	{
		int rp; // right paren
		int pp = 0; // pattern position
		string str;

		this->_tokens.resize(this->get_size());
		for(int i = 0; i < this->get_size(); ++i)
		{
			if( this->_str_pat[pp] == '(' )
			{
				rp = this->_str_pat.find(')', pp + 1);
				str = this->_str_pat.substr(pp + 1, rp - pp - 1);
				pp = rp + 1;
			}
			else
			{
				str = this->_str_pat.substr(pp, 1);
				++pp;
			}
			this->_tokens[i].reset(str);
		}
	}

private:


private:
	string _str_pat;
	int _pat_size;
	vector<e_token> _tokens;
};

int main(int argc, char** argv)
{
	int L, D, N;
	vector<string> word;
	string pattern;


//#	define __USINGFILE 1
#	if defined( __USINGFILE)
	if( argc < 2 )
	{
		cerr << "error: no input file" << endl;
		return -1;
	}
	ifstream in(argv[1]);
#	else
	istream& in = cin;
#	endif


	in >> L >> D >> N;
/*
	cout << "L: " << L << endl
		<< "D: " << D << endl
		<< "N: " << N << endl;

*/
	// read D words
	word.resize(D);
	for(int i = 0; i < D; ++i)
	{
		in >> word[i];
	}
	/*
	for(int i = 0; i < D; ++i)
	{
		cout << "word " << i << ": " << word[i] << endl;
	}
	*/

	// read N cases
	int result = 0;
	e_pattern p;
	p.set_size(L);
	for(int i = 0; i < N; ++i)
	{
		in >> pattern;
		//cout << "pattern: " << pattern << endl;


		// solve case
		p.set_pat(pattern);
		p.tokenize();

		result = 0;
		for(int k = 0; k < word.size(); ++k)
		{
			if( p.match_word(word[k]) )
			{
				//cout << word[k] << " match" << endl;
				++result;
			}
			/*
			else
			{
				cout << word[k] << " NO match" << endl;
			}
			*/
		}
		// end solving

		cout << "Case #" << (i+1) << ": " << result << endl;
	}


	return 0;
}