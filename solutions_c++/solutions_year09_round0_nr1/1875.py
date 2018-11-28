#include <iostream>
#include <string>
#include <cstdlib>
#include <set>
#include <vector>
using namespace std;

set<string> words;
vector< set<string> > prefix_words;

int match(string beg, string s)
{
    if(s.empty())
	return words.count(beg);

    // s begin with a letter
    if(s[0] != '(') {
	int i(1);
	while(i<s.size() && s[i]!='(')
	    ++i;
	if(i >= s.size())
	    return match(beg + s, "");
	else {
	    beg += s.substr(0, i);
	    if(prefix_words[beg.size()-1].count(beg) == 0)
		return 0;
	    return match(beg, s.substr(i));
	}
    }

    // s begins with (
    int i(2);		
    while(s[i] != ')')
	++i;
    string left("");
    if((i+1) < s.size())
	left = s.substr(i+1);
    int idx = beg.size();
    int count(0);
    for(int j = 1; j < i; ++j) {
	if(prefix_words[idx].count(beg+s[j]))  // maybe a word
	    count += match(beg+s[j], left);
    }
    return count;
}

int main()
{
    int l, d, n;
    cin>>l>>d>>n;

    int i, j, k;
    for(i = 0; i < l; ++i) {
	set<string> ss;
	prefix_words.push_back(ss);
    }
    string s;
    for(i = 0; i < d; ++i) {
	cin>>s;
	words.insert(s);
	for(j = 0; j < l; ++j)
	    for(k = 1; k <= l; ++k)
		prefix_words[j].insert(s.substr(0, k));
    }
    for(i = 1; i <= n; ++i) {
	cin>>s;
	cout<<"Case #"<<i<<": "<<match("", s)<<endl;
    }
    return 0;
}
