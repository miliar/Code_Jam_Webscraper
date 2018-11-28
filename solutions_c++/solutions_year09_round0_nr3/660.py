//
// /home/xenosoz/work/gcj/2009/C_Welcome_to_Code_Jam
//

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <cassert>
#include <iomanip>

using namespace std;


string g_welcome_str("welcome to code jam");


struct warp
{
	size_t from, to;
	warp(const size_t& _from, const size_t& _to)
		: from(_from), to(_to) {
	}
};
typedef vector<warp> warp_vector;


struct action_map
{
	typedef map<char, warp_vector> value_type;
	value_type v;

	action_map() {
	}

	action_map generate(const string& str) {
		action_map ret;
		for(string::const_iterator i = str.begin(); i != str.end(); ++i) {
			const string::value_type &c = *i;
			size_t cnt = i - str.begin();
			ret.append(c, cnt, cnt+1);
		}
		return ret;
	}

	void append(const char &id, const size_t &from, const size_t &to) {
		v[id].push_back(warp(from, to));
		//cerr << "(" << id << " " << v[id].size() << " " << from << " " << to << ")\n";
	}

	action_map(const string &str) {
		action_map newone = generate(str);
		swap(*this, newone);
	}
};


struct apple_box
{
	typedef vector<int> value_type;
	value_type v;

	apple_box(const size_t &str_size)
		: v(str_size+1, 0)
	{
		v[0] = 1;
	}
	static const int filter(const int& v) {
		return (v % 10000);
	}
	const int enumeration() {
		assert(!v.empty());
		//cerr << "(" << (v.size()-1) << ")\n";
		return apple_box::filter(v[v.size()-1]);
	}
};


void apply(apple_box& ret, const apple_box& a, const action_map &m, const char &c) {
	action_map::value_type::const_iterator f = m.v.find(c);
	if(f == m.v.end()) {
		return;
	}
	const warp_vector &wv = (*f).second;

	for(warp_vector::const_iterator i = wv.begin(); i != wv.end(); ++i) {
		const warp_vector::value_type &c = *i;
		ret.v[c.to] = apple_box::filter(ret.v[c.to] + a.v[c.from]);
		//cerr << c.to << " " << ret.v[c.to] << "\n";
	}
}

int solve(const action_map &m, const string &str) {
	const size_t str_size = g_welcome_str.size();
	apple_box active(str_size), passive(str_size);
	for(string::const_iterator i = str.begin(); i != str.end(); ++i) {
		const string::value_type &c = *i;
		passive = active;
		apply(active, passive, m, c);
	}
	return active.enumeration();
}


int main(void)
{
	int N = 0;
	if(!(cin >> N)) {
		assert(false && "input error");
	}
	if(const bool enable_triming = true) {
		string s;
		getline(cin, s);
	}

	action_map welcome_msg(g_welcome_str);

	cout << setfill('0');
	for(int i = 0; i < N; ++i) {
		string s;
		getline(cin, s);
		assert(cin && "unexpected end of input buffer");

		cout << "Case #" << (i+1) << ": ";
		//cerr << "[" << s << "] ";
		cout << setw(4) << solve(welcome_msg, s) << "\n";
	}
	return 0;
}
