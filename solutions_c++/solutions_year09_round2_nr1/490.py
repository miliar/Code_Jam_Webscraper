#include <iostream>
#include <string>
#include <map>
#include <set>
#include <cassert>
#include <vector>
#include <boost/shared_ptr.hpp>
#include <ctype.h>
#include <sstream>
#include <iomanip>

using namespace std;
using namespace boost;


void skip_whitespace(istream &in) {
	char c = '\0';
	while(true) {
		if(!(in && isspace(in.peek()))) {
			break;
		}
		// advance
		in.get(c);
	}
}

void assume_character(istream &in, const char &_c) {
	char c;
	in.get(c);
	//cerr << "[" << c << "][" << _c << "]\n";
	assert(in && (c == _c));
}

bool check_character(istream &in, const char &c) {
	return (in.peek() == c) && in;
}

struct tree {
	double weight;
	string feature;
	shared_ptr<tree> decision[2];
	void parse(istream &in) {
		skip_whitespace(in);
		assume_character(in, '(');

		skip_whitespace(in);
		in >> weight;
		//cerr << weight;

		skip_whitespace(in);
		if(!check_character(in, ')')) {
			in >> feature;
			//cerr << feature;

			decision[0] = shared_ptr<tree>(new tree());
			(*decision[0]).parse(in);

			decision[1] = shared_ptr<tree>(new tree());
			(*decision[1]).parse(in);
		}

		skip_whitespace(in);
		assume_character(in, ')');
	}
	void print(ostream &out) {
		out << "( " << weight;
		if(!feature.empty()) {
			out << " " << feature << "\n";
			(*decision[0]).print(out);
			out << "\n";
			(*decision[1]).print(out);
			out << "\n";
		}
		out << ")";
	}
};


typedef string feature;
typedef set<feature> feature_set;
typedef string animal_name;
typedef map<animal_name, feature_set> animap;

double solve(double &ret, shared_ptr<tree> _tree, feature_set& fs) {
	ret *= _tree->weight;
	if(_tree->feature.empty()) {
		return ret;
	}
	bool is_found = (fs.find(_tree->feature) != fs.end());
	solve(ret, _tree->decision[!is_found], fs);

	return ret;
}

int main(void) {
	int N = 0;
	if(!(cin >> N)) {
		assert(false && "parse");
		return 1;
	}
	for(int i = 0; i < N; ++i) {
		int L = 0;
		if(!(cin >> L)) {
			assert(false && "parse");
			return 1;
		}
		
		// parse
		shared_ptr<tree> rule(new tree());
		{
			string s;
			getline(cin, s);
			assert(s.empty());

			stringstream ss;
			for(int j = 0; j < L; ++j) {
				getline(cin, s);
				ss << " " << s;
			}
			rule->parse(ss);
		}

		//rule->print(cerr);
		int A = 0;
		if(!(cin >> A)) {
			assert(false && "parse");
			return 1;
		}

		cout << "Case #" << (1+i) << ":\n";
		for(int j = 0; j < A; ++j) {
			animal_name name;
			int n = 0;
			feature_set fs;

			if(!(cin >> name >> n)) {
				assert(false && "parse");
				return 1;
			}
			for(int k = 0; k < n; ++k) {
				string s;
				cin >> s;
				fs.insert(s);
			}
			double ret = 1;
			cout << fixed;
			cout << setprecision(7) << solve(ret, rule, fs) << "\n";
		}
	}
	return 0;
}
