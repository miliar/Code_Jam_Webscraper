#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

typedef pair<char,char> chpair_t;
typedef map<chpair_t,char> transforms_t;
typedef map<char,char> oppose_t;

int to_index(char c)
{
	return c - 'A';
}

string solve(const transforms_t& trans, const oppose_t& oppos, const string& invoke)
{
	vector<int> contained('Z'-'A'+1);
	std::string ans;
	
	for (string::const_iterator it = invoke.begin(); it != invoke.end(); ++it) {
		if (ans.size()>=1) {
			transforms_t::const_iterator transit = trans.find(chpair_t(ans[ans.size()-1], *it));
			if (transit != trans.end()) {
				--contained[to_index(ans[ans.size()-1])];
				ans[ans.size()-1] = transit->second;
				++contained[to_index(transit->second)];
			}
			else {
				oppose_t::const_iterator opposit = oppos.find(*it);
				if (opposit != oppos.end() && contained[to_index(opposit->second)]) {
					ans.clear();
					fill(contained.begin(), contained.end(), 0);
				}
				else {
					ans += *it;
					++contained[to_index(*it)];
				}
			}
		}
		else {
			ans += *it;
			++contained[to_index(*it)];
		}
	}
	return ans;
}

// 1 QSM 1 SD 10 SQRFADSAAF


string convert(const string& unform)
{
	string ans;
	ans += '[';
	for (string::const_iterator it = unform.begin(); it != unform.end(); ++it) {
		ans += *it;
		if (it+1 != unform.end()) {
			ans += ", ";
		}
	}
	ans += ']';
	return ans;
}

int main(int argc, char **argv) 
{
	int T;
	cin >> T;
	for (int t=0; t<T; ++t) {
		int C;
		cin >> C;
		transforms_t transforms;
		for (int i=0; i<C; ++i) {
			chpair_t from;
			char to;
			cin >> from.first >> from.second >> to;
			transforms.insert(transforms_t::value_type(from, to));
			swap(from.first, from.second);
			transforms.insert(transforms_t::value_type(from, to));
		}
		
		int D;
		cin >> D;
		oppose_t oppositions;
		for (int i=0; i<D; ++i) {
			chpair_t next;
			cin >> next.first >> next.second;
			oppositions.insert(next);
			swap(next.first, next.second);
			oppositions.insert(next);
		}
		
		int N;
		cin >> N;
		string invokes;
		cin >> invokes;
		
		cout << "Case #" << t+1 << ": " << convert(solve(transforms, oppositions, invokes)) << endl;
	}
	
	return 0;
}
