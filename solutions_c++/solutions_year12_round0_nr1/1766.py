#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<algorithm>
#include<cmath>
#include<set>
#include<queue>
#include<sstream>
#include<utility>

using std::pair;
using std::stringstream;
using std::next_permutation;
using std::sqrt;
using std::priority_queue;
using std::sort;
using std::stack;
using std::string;
using std::vector;
using std::cin;
using std::cout;
using std::endl;
using std::min;
using std::max;
using std::set;
using std::swap;
using std::random_shuffle;
using std::queue;
using std::sin;
using std::cos;
using std::make_pair;
using std::cos;
using std::cerr;

typedef long long ll; 
typedef pair<ll, ll> pll;
const long double PI = 3.14159265358979323846;  
string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
string s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
string s4 = "yqee";
string t4 = "azoo";

string t1 = "our language is impossible to understand";
string t2 = "there are twenty six factorial possibilities";
string t3 = "so it is okay if you want to just give up";

int main() {
	vector<int> map(26, 16);
	for (int i = 0; i < s1.size(); ++i)
		if (s1[i] != ' ')
			map[s1[i]-'a'] = t1[i] - 'a';
	for (int i = 0; i < s2.size(); ++i)
		if (s2[i] != ' ')
			map[s2[i]-'a'] = t2[i] - 'a';
	for (int i = 0; i < s3.size(); ++i)
		if (s3[i] != ' ')
			map[s3[i]-'a'] = t3[i] - 'a';
	for (int i = 0; i < s4.size(); ++i)
		if (s4[i] != ' ')
			map[s4[i]-'a'] = t4[i] - 'a';

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i) {
		char in[101];
		gets(in);
		string inp(in);
		string s;
		for (int i = 0; i < inp.size(); ++i) 
			if (inp[i] == ' ')
				s += ' ';
			else
				s += map[inp[i] - 'a'] + 'a';
		cout << "Case #" << i + 1 << ": " << s << endl;
		std::cerr << i << endl;
	}
	return 0;
}
