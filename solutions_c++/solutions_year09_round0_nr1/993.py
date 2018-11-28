#include <iostream>
#include <vector>
#include <string>

using namespace std;

static const size_t MAX_L = 15;

struct tword
{
	int letters[MAX_L];
	string seq;

	tword()
	{
		for(size_t i = 0; i < MAX_L; i++)
		{
			letters[i] = 0;
		}
	}

	tword(string& in)
	{
		setme(in);
	}

	void setme(string& in)
	{
		seq = in;
		for(size_t i = 0; i < MAX_L; i++)
		{
			letters[i] = 0;
		}

		size_t pos = 0;
		for(string::iterator i = in.begin(); i != in.end(); ++i, ++pos)
		{
			if(*i == '(')
			{
				while(*(++i) != ')')
				{
					letters[pos] |= 1 << (*i - 'a');
				}
			}
			else
			{
				letters[pos] = 1 << (*i - 'a');
			}
		}
	}

	bool operator==(const tword& other)
	{
		for(size_t i = 0; i < MAX_L && letters[i] != 0; i++)
		{
			if( (letters[i] & other.letters[i]) == 0)
			{
				return false;
			}
		}

		return true;
	}
};

istream& operator>>(istream& in, tword& var)
{
	string t;
	in >> t;
	var.setme(t);
	return in;
}

ostream& operator<<(ostream& o, const tword& me)
{
	o << me.seq;
	o << "(";
	for(size_t i = 0; i < MAX_L; i++)
	{
		o << hex << me.letters[i] << ",";
	}
	o << ")";
	return o;
}

int main()
{
	int L, D, N;

	cin >> L >> D >> N;
	vector<tword> dictionary;

	for(size_t i = 0; i < D; i++)
	{

		tword wd;
		cin >> wd;
		dictionary.push_back(wd);
	}

	for(size_t i = 0; i < N; i++)
	{
		tword test;
		cin >> test;

		size_t count = 0;
		for(vector<tword>::iterator dict = dictionary.begin();
			dict != dictionary.end(); ++dict)
		{
			//cerr << "Compare: " << *dict << "," << test;
			if(*dict == test)
			{
			//	cerr << "Yes";
				++count;
			}
			//cerr << endl;
		}

		cout << "Case #" << (i + 1) << ": " << count << endl;
	}

	return 0;
}
