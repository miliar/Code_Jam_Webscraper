/*
ID: imranka1
PROG: test
LANG: C++
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
#include <fstream>
using namespace std;
#define all(x) (x).begin(),(x).end()

#define vs vector <string>
#define vi vector <int>
#define p(X) push_back((X))

#define fir(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
#define fire(i,j,n) for(int (i)=(j);(i)<=(n);(i)++)
#define firr(i,j,n) for(int (i)=(j);(i)>(n);(i)--)
#define firre(i,j,n) for(int (i)=(j);(i)>=(n);(i)--)
#define tr(v,it) for(typeof(v.begin()) it=v.begin();it!=v.end();it++)

#define srt(v) sort((v).begin(),(v).end())
#define srtc(v) sort(v.begin(),v.end(),cmp)

#define _bc(i) __builtin_popcount(i)

string lower(string s) {for(int i=0;i<s.size();i++) s[i]=tolower(s[i]);return s;}
vector<string> sep(string s,char c) { string temp;vector<string> res;for(int i=0;i<s.size();i++) { if (s[i]==c) {if (temp!="") res.push_back(temp);temp="";continue;}temp=temp+s[i];}if (temp!="") res.push_back(temp);return res;}
template<class T> T toint(string s)
{
	stringstream ss(s);
	T ret;
	ss>>ret;
	return ret;
}
template<class T> string tostr(T inp)
{
	string ret;
	stringstream ss;ss<<inp;
	ss>>ret;
	return ret;
}
map<pair<char, char>, char> trans;
set<pair<char, char> > oppose;
vector<char> stak;
int main() {
	int T;
	cin>>T;
	int tc = 0;
	while(T--)
	{
		tc++;
		trans.clear();oppose.clear();stak.clear();
		printf("Case #%d: ", tc);
		int C;
		cin>>C;
		fir(i, 0, C)
		{
			string s;
			cin>>s;
			trans[make_pair(min(s[0], s[1]), max(s[0], s[1]))] = s[2];
		}
		int D;
		cin>>D;
		fir(i, 0, D)
		{
			string s;
			cin>>s;
			oppose.insert(make_pair(min(s[0], s[1]), max(s[0], s[1])));
		}
		int N;
		cin>>N;
		string s;
		cin>>s;
		stak.clear();
		fir(i, 0, N)
		{
			stak.p(s[i]);
			while(stak.size() > 1)
			{
				pair<char, char> tpr = make_pair(min(stak[stak.size() - 1], stak[stak.size() - 2]), max(stak[stak.size() - 1], stak[stak.size() - 2]));
				if (trans.find(tpr) != trans.end())
				{
					stak.pop_back();
					stak.pop_back();
					stak.p(trans[tpr]);
					continue;
				}
				bool ops = 0;
				fir(j, 0, stak.size() - 1)
				{
					tpr = make_pair(min(stak[stak.size() - 1], stak[j]), max(stak[stak.size() - 1], stak[j]));
					if (oppose.find(tpr) != oppose.end())
					{ ops = 1; break;}
				}
				if (ops) stak.clear();
				else break;
			}
		}
		bool fst = 1;
		printf("[");
		fir(i, 0, stak.size())
		{
			if (!fst) printf(", %c", stak[i]);
			else printf("%c", stak[i]);
			fst = 0;
		}
		printf("]\n");
	}
    return 0;
}