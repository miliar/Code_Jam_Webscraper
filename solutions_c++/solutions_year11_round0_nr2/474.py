/* b-small.cc
 */
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <cstdio>
#include <cassert>
using namespace std;
int T, C, D, N;
int index(char a, char b)
{
    assert(a <= 'Z' && b <= 'Z');
    return (a-'A')*32+(b-'A');
}
int key(char a, char b)
{
    assert(a <= 'Z' && b <= 'Z');
    return (1u<<(a-'A'))+(1u<<(b-'A'));
}
string decorate(const string& src)
{
    string ret = "[";
    for (size_t i=0; i<src.size(); ++i) {
	ret += src[i];
	if (i+1<src.size())
	    ret += ", ";
    }
    return ret += "]";
}
int main() {
    cin >> T;
    for (int t=0; t<T; ++t) {
	char combine[32*32] = {0};
	vector<int> opposed;
	string a, s;
	cin >> C;
	for (int i=0; i<C; ++i) {
	    cin >> s;
	    assert(s.size() == 3);
	    combine[index(s[0],s[1])] = s[2];
	    combine[index(s[1],s[0])] = s[2];
	}
	cin >> D;
	for (int i=0; i<D; ++i) {
	    cin >> s;
	    assert(s.size() == 2);
	    opposed.push_back(key(s[0],s[1]));
	}
	sort(opposed.begin(), opposed.end());
	opposed.erase(unique(opposed.begin(), opposed.end()), opposed.end());
	cin >> N >> s;
	assert(s.size() == N);
	for (int i=0; i<N; ++i) {
	    char c = s[i];
	    while (! a.empty() && combine[index(a[a.size()-1], c)]) {
		c = combine[index(a[a.size()-1], c)];
		a.resize(a.size()-1);
	    }
	    a += c;
	    for (int p=0; p<a.size(); ++p)
		for (int q=p+1; q<a.size(); ++q)
		    if (binary_search(opposed.begin(), opposed.end(),
				      key(a[p], a[q]))) {
			a.clear();
			break;
		    }
	}
	printf("Case #%d: %s\n", t+1, decorate(a).c_str());
    }
}
