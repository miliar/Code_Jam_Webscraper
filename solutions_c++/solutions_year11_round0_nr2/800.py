#include <iostream>
#include <array>
#include <vector>
#include <cassert>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

class StringFilter {
	virtual void operator()(string & r) = 0;
};

class CombineFilter {
public:
	CombineFilter(char c1,char c2,char res) :
		orig_a(c1),orig_b(c2),result(res){}

	void apply(string & r) const {
		if (r.size() >= 2) {
			char c = *r.rbegin();
			char p = *(++r.rbegin());

			if ( (c == orig_a && p == orig_b) ||
				 (c == orig_b && p == orig_a)) {
				r.erase(r.size()-1);
				*r.rbegin() = result;
			}
		}
	}
private:
	char orig_a,orig_b,result;
};

class ClearerFilter {
public:
	ClearerFilter(char c1,char c2) :
		orig_a(c1),orig_b(c2) {}

	void apply(string & r) const {
		auto iter1 = std::find(r.begin(),r.end(),orig_a);
		auto iter2 = std::find(r.begin(),r.end(),orig_b);

		if (iter1 == r.end() || iter2 == r.end()) return;

		if (iter1 > iter2)
			std::swap(iter1,iter2);
		r.erase(iter1,iter2+1);
	}

private:
	char orig_a,orig_b;
};

string output_string(const string & r) {
	string ans = "[";
	if (r.size()) ans+=r[0];

	for (int i=1;i < r.size();++i) {
		ans+=", ";
		ans+=r[i];
	}
	ans+="]";
	return ans;
}

string solve(const vector<CombineFilter> & c,
		   const vector<ClearerFilter> & q,
		   const string & str) {

	string ans;

	for (int i=0;i < str.size();++i) {
		char m = str[i];
		ans+=m;

		std::for_each(c.begin(),c.end(),[&ans](const CombineFilter & filt) {
			filt.apply(ans);
		});

		std::for_each(q.begin(),q.end(),[&ans](const ClearerFilter & filt) {
			filt.apply(ans);
		});
	}
	return output_string(ans);
}

int main(int argc, char **argv) {
	int T;

	cin >> T;

	for(int i=0;i < T;++i) {
		int C;
		cin >> C;

		vector<CombineFilter> comb;
		for (int j=0;j < C;++j) {
			char seq[3];
			cin >> seq;
			comb.push_back(CombineFilter(seq[0],seq[1],seq[2]));
		}

		int D;
		cin >> D;
		vector<ClearerFilter> opp;
		for (int j=0;j < D;++j) {
			char seq[2];
			cin >> seq;
			opp.push_back(ClearerFilter(seq[0],seq[1]));
		}

		string seq;
		int N;
		cin >> N >> seq;

		cout << "Case #" << (i+1) << ": " << solve(comb,opp,seq) << endl;
	}
	
    return 0;
}
