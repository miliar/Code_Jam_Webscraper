#define _CRT_SECURE_NO_DEPRECATE
#include <iostream> 
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;

template<class T >
string to_s(const vector<T>& a,const string& delim)
{
	ostringstream out;
	for(int i=0;i<(int)a.size();i++)
	{
		out<<a[i];
		if(i!= (int)a.size()-1)
			out<<delim;
	}
	return out.str();
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int nt;
	cin>>nt;
	string temp;
	for(int it=1;it<=nt;it++)
	{
		map<char, string> o;
		map<char, vector<pair<char,char> > > c;
		int a;
		cin >> a;
		for (int i=0;i<a;++i){
			cin >> temp;
			if (c.find(temp[0]) == c.end()) {
				c.insert(mpair(temp[0], vector<pair<char,char> > ()));
			}
			if (c.find(temp[1]) == c.end()) {
				c.insert(mpair(temp[1], vector<pair<char,char> > ()));
			}
			c[temp[0]].push_back(mpair(temp[1], temp[2]));
			c[temp[1]].push_back(mpair(temp[0], temp[2]));
		}
		cin >> a;
		for (int i=0;i<a;++i){
			cin >> temp;
			if (o.find(temp[0]) == o.end()){
				o.insert(mpair(temp[0], "" ));
			}
			if (o.find(temp[1]) == o.end()){
				o.insert(mpair(temp[1], "" ));
			}
			o[temp[0]].push_back(temp[1]);
			o[temp[1]].push_back(temp[0]);
		}
		string s;
		int n;
		cin >> n;
		cin >> s;
		n = s.size();
		vector<char> res;
		for (int i=0;i<n;++i){
			res.push_back(s[i]);
			if (res.size() <= 1){
				continue;
			}
			char prev = res[(int)res.size() - 2];
			map<char, vector<pair<char,char> > >::iterator it = c.find(s[i]);
			if (it != c.end()) {
				bool found = false;
				const vector<pair<char, char> >& v = it->second;
				for (int j =0; j< (int)v.size();++j) {
					if (v[j].first == prev) {
						res.pop_back();
						res.pop_back();
						res.push_back(v[j].second);
						found = true;
						break;
					}
				}
				if (found) {
					continue;
				}
			}
			map<char, string>::iterator iter = o.find(res.back());
			if (iter == o.end()) {
				continue;
			}
			const string& str = iter->second;
			for (int j=0;j+1<(int)res.size();++j) {
				for (int k=0;k<(int)str.size();++k){
					if (str[k] == res[j]){
						res = vector<char>();
						break;
					}
				}
			}
		}
		cout<<"Case #"<<it<<": "<< "[" << to_s(res,", ") << "]"<<endl;
	}
	return 0;
}
