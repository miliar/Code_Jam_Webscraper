// alien_language.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <vector>
#include <string>

typedef std::vector<std::string> token_t;
typedef std::string word_t;
typedef std::vector<unsigned int> result_t;

typedef std::vector<token_t> tokenlist_t;
typedef std::vector<word_t> wordlist_t;
typedef std::vector<result_t> resultlist_t;

template <class T, class C>
void split(const T &source, C &items)
{
    //
    items.clear();

    //
    T::size_type i = 0, j;

	for (i = 0; i < source.length(); i++) {
		T value;

		if (source[i] == '(') {
			for (j = i + 1; source[j] != ')'; j++)
				;

            value = source.substr(i + 1, j - (i + 1));

			i = j;
		} else {
			value = source.substr(i, 1);
		}

		items.push_back(value);
	}
}

unsigned int process_token(const wordlist_t &wl, const token_t &t)
{
    unsigned int c = 0U;

    result_t r;
    r.resize(wl.size());

    for (unsigned int j = 0; j < r.size(); j++)
        r[j] = wl[0].length();

    for (unsigned int i = 0; i < t.size(); i ++) {
        for (unsigned int j = 0; j < wl.size(); j++) {
			if (t[i].find(wl[j][i]) != std::string::npos) {
                r[j] -= 1U;

                if (r[j] == 0U)
                    c += 1U;
            }
        }
    }

    return c;
}

void process(std::ostream &out, const wordlist_t &wl, const tokenlist_t &tl)
{
    for (unsigned int i = 0; i < tl.size(); i++)
		out << "Case #" << (i + 1) << ": " << process_token(wl, tl[i]) << std::endl;
}

void load_data(std::istream &in, wordlist_t &wl, tokenlist_t &tl)
{
	unsigned int L, D, N;

	in >> L;
	in >> D;
	in >> N;

	for (unsigned int i = 0U; i < D; i++) {
		std::string w;

		in >> w;

		wl.push_back(w);
	}

	for (unsigned int j = 0U; j < N; j++) {
		std::string t;

		in >> t;

		token_t tv;
		split(t, tv);

		tl.push_back(tv);
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
//	std::ifstream in("A-sample.in");
//	std::ofstream out("A-sample.out");
//	std::ifstream in("A-small-attempt0.in");
//	std::ofstream out("A-small.out");
	std::ifstream in("A-large.in");
	std::ofstream out("A-large.out");

	wordlist_t wl;
	tokenlist_t tl;

	load_data(in, wl, tl);
	process(out, wl, tl);

	return 0;
}

