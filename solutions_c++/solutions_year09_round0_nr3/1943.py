#include <iostream>
#include <sstream>
#include <string>
#include <map>
using namespace std;

map<string, int> ptn_times;

int foo(string s, string m)
{
    if(s.size() < m.size())
	return 0;
    if(m.empty())
	return 1;

    string ptn(s+"#"+m);
    map<string, int>::iterator it = ptn_times.find(ptn);
    if(it != ptn_times.end())
	return it->second;

    int times(0);
    for(int i = 0; i < s.size(); ++i) {
	if(s[i] == m[0]) {
	    times += foo(s.substr(i+1), m.substr(1));
	}
    }
    ptn_times.insert(make_pair(ptn, times));
    return times;
}

string setFormat(int t)
{
    string s;
    stringstream ss(stringstream::in | stringstream::out);
    ss<<t;
    ss>>s;
    if(s.size() > 4)
	return s.substr(s.size()-4);
    int j(4-s.size());
    for(int i = 0; i < j; ++i)
	s = '0' + s;
    return s;
}

int main()
{
    const string match_str("welcome to code jam");
    int n, c(0), times;
    cin>>n;
    cin.get();
    string line;
    while(n--) {
	getline(cin, line);
	cout<<"Case #"<<++c<<": ";
	times = foo(line, match_str);
	cout<<setFormat(times)<<endl;
	ptn_times.clear();
    }
}
