#include <iostream>
#include <vector>
#include <cassert>
#include <string>

using namespace std;

struct charmap
{
	int v;

	charmap() : v(0) {}

	static int mask_of_char(const char &c) {
		assert('a' <= c && c <= 'z');
		return 1 << int(c - 'a');
	}
	void clear() {
		v = 0;
	}
	void append(const char &c) {
		int mask = charmap::mask_of_char(c);
		v |= mask;
	}
	charmap operator & (const charmap & rhs) const {
		const charmap &lhs = *this;
		charmap ret;
		ret.v = lhs.v & rhs.v;
		return ret;
	}
	bool empty() const {
		return v == 0;
	}
};

struct dictmap
{
	typedef vector<charmap> value_type;
	value_type v;

	dictmap() {
	}

	static dictmap generate(const string &str) {
		dictmap ret;

		charmap curmap;
		bool is_paren = false;
		for(string::const_iterator i = str.begin(); i != str.end(); ++i) {
			const char &c = *i;
			if('(' == c) {
				assert(false == is_paren);
				is_paren = true;
				continue;
			}
			if(')' == c) {
				assert(true == is_paren);
				is_paren = false;
				ret.v.push_back(curmap);
				curmap.clear();
				continue;
			}

			//
			curmap.append(c);

			if(false == is_paren) {
				ret.v.push_back(curmap);
				curmap.clear();
				continue;
			}
		}

		return ret;
	}

	dictmap(const string &str) {
		dictmap newone(dictmap::generate(str));
		swap(*this, newone);
	}

	dictmap operator & (const dictmap & rhs) const {
		dictmap ret;

		const dictmap& lhs = *this;
		size_t sl = lhs.v.size();
		size_t sr = rhs.v.size();
		if(sl != sr) {
			return ret;
		}
		assert(sl == sr);
		size_t s = (sl + sr) / 2;

		for(size_t i = 0; i < s; ++i) {
			const value_type::value_type &cl = lhs.v[i];
			const value_type::value_type &cr = rhs.v[i];
			charmap curmap = (cl & cr);
			ret.v.push_back(curmap);
		}
		return ret;
	}

	operator bool() const {
		if(v.empty()) {
			return false;
		}
		for(value_type::const_iterator i = v.begin(); i != v.end(); ++i) {
			const value_type::value_type &c = *i;
			if(c.empty()) {
				return false;
			}
		}
		return true;
	}
};

int main(void)
{
	int L = 0;
	int D = 0;
	int N = 0;

	vector<dictmap> strings;

	if(!(cin >> L >> D >> N)) {
		assert(false && "intput failed");
	}
	for(int i = 0; i < D; ++i) {
		string s;
		cin >> s;
		strings.push_back(dictmap(s));
	}
	for(int i = 0; i < N; ++i) {
		string s;
		cin >> s;

		dictmap pattern(s);
		int matched = 0;
		for(vector<dictmap>::iterator j = strings.begin(); j != strings.end(); ++j) {
			dictmap &c = *j;
			if(pattern & c) { ++matched; }
		}
		cout << "Case #" << (i+1) << ": " << matched << "\n";
	}
	return 0;
}
