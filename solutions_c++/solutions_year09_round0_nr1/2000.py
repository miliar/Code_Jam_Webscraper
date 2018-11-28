#include <iostream>
#include <cassert>

struct Pattern
{
	std::string _pats;
	const char *_pat;
	int _len;
	int _num;

	Pattern()
	{
		std::cin >> _pats;
		_pat = _pats.c_str();
		_len = _pats.length();
	}

	bool process(const char *w, int total )
	{
		bool alt = false;
		/*std::cout << "------------" << std::endl;
		for(int i = 0; i < total; ++i) std::cout << w[i];
		std::cout << std::endl << _pats << std::endl;
		*/
		for(int i = 0; i < _len; ++i)
		{
			//std::cout << i << " " << _pat[i] <<  "  *" << (char) *w << std::endl;
			if (_pat[i] == '(') { alt = true; continue; }
			else if (_pat[i] == ')') { return false; }
			else if (_pat[i] == *w ) {
				w++;
				//std::cout << "!" << std::endl;
				if (--total == 0) return true;
				if (alt == true)
				{
					while (_pat[i] != ')') i++;
					alt = false;
				}
			}
			else if (!alt) return false;
		}
		exit(2);
	}

};

struct Problem
{
	int L, D, N;
	char *words;
	Pattern *pats;

	void exec()
	{
		std::cin >> L >> D >> N;
		std::cin.get();
		readWords();
		pats = new Pattern[N];
		test();
	}

	void readWords()
	{
		words = new char [L*D];
		std::string s;
		int p = 0;
		for(int i = 0; i < D; ++i)
		{
			for (int j = 0; j < L; j++)
			{
			 	words[p++] = std::cin.get();
			}
			std::cin.get(); // CR
		}
	}

	void test()
	{
		for(int i = 0; i < N; ++i)
		{
			int c = 0; 
			for(int j = 0; j < D; j++)
			{
				if (pats[i].process(words + j*L ,L)) c++;
			}
			std::cout << "Case #" << i+1 << ": " << c << std::endl;
		}
	}

	~Problem()
	{
		delete[] words;
		delete[] pats;
	}
};

int main(int argc, char **argv)
{
	Problem p; 
	p.exec();

	return 0;
}
