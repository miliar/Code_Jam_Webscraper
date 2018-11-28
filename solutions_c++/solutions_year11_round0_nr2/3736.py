#define _USE_MATH_DEFINES
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
/*maded by demidoff*/
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <utility>


using namespace std;
#pragma comment(linker, "/STACK:64000000")


#define p(x) cout<<#x<<":"<<x<<"\n"
#define INF (int)(1e10)
#define INFL (int)(1e18)
#define PB push_back
#define MP make_pair
#define PRIME 31


typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pii64;
typedef vector<int> vi;
typedef vector<ll> vi64;
typedef vector< vi > vii;
typedef vector< vi64 > vii64;
typedef vector< pii > vpii;
typedef vector < pii64 > vpii64;

bool cmpInt(int a, int b)
{
	return a < b;
}

bool cmpPair(pair<string,char> a, pair<string,char> b)
{
	return a.first < b.first;
}

int gcd(int a, int b)
{
	if(b == 0)
		return a;
	else 
		gcd(b,a%b);
}

ll getHash(string &str) {
	//cout << str << endl;
	ll sum = 0;
	ll p_pow = 1;
	for(int i = 0; i < str.size(); ++i) {
		sum += (str[i] - 'a' + 1) * p_pow;
		p_pow *= PRIME;
	}
	return sum;
}

void updateTree(vector<int> &mas, int i, int l, int r, int a, int b,int sum)
{
	if(a > b)
		return;
	if(l == a && b == r) {
		mas[i] += sum;
	} else {
		int m = (l + r) / 2;
		updateTree(mas, i * 2, l, m, a, min(b,m), sum);
		updateTree(mas, i * 2 + 1, m + 1, r, max(m + 1, a), b, sum);

	}
}


int getTree(vector<int> &mas, int i, int l, int r, int pos)
{
	//p(i);
	if(l == r) {
		//cout << mas[i] << endl;
		return mas[i];
	}
	int m = (l + r) / 2;
	if(pos <= m)
		return mas[i] + getTree(mas, i * 2, l, m,pos);
	else
		return mas[i] + getTree(mas, i * 2 + 1, m + 1, r,pos);
}

int bs(int l, int r, string x, vector< pair<string,char> > &combine) 
{
	if(r < l)
		return -1;
	int m;
	while(l < r) {
		m = (l + r) / 2;
		if(x < combine[m].first) {
			r = m;
		} else
			l = m + 1;
	}
	if(combine[r].first == x)
		return r;
	else 
		return -1;
}

#define INPUT_ON 1
#define INPUT_TXT 1
#define file_name "test"
int main()
{
	if(INPUT_ON) {
		if(INPUT_TXT) {
			freopen("input.txt","r",stdin);
			freopen("output.txt","w",stdout);
		} else {
			freopen(file_name".in","r",stdin);
			freopen(file_name".out","w",stdout);
		}
	}
	int t;
	scanf("%d",&t);
	string out;
	int c,d;
	string str;
	string tmp;

	for(int r = 0; r < t; ++r) {
		map<char,vector<char> > opposed;
		//map<pair<char,char> ,char> combine;
		vector<pair<string,char> > combine;
		scanf("%d",&c);
		for(int j = 0; j < c; ++j) {
			cin >> tmp;
			string s = "";
			s += tmp[0];
			s += tmp[1];
			combine.push_back(MP(s,tmp[2]));
			//swap(s[0],s[1]);
			reverse(s.begin(),s.end());
			combine.push_back(MP(s,tmp[2]));
		}
		sort(combine.begin(),combine.end(),cmpPair);
		scanf("%d",&d);
		for(int j = 0; j < d; ++j) {
			cin >> tmp;
			opposed[tmp[0]].push_back(tmp[1]);
			opposed[tmp[1]].push_back(tmp[0]);
		}
		cin >> c >> str;
		char ended = - 1;
		multiset<char> used;
		out.clear();
		for(int i = 0; i < str.size(); ++i) {
			string ss;
			ss += ended;
			ss += str[i];
			
			int tt = bs(0,(int)combine.size() - 1, ss,combine);
			if(tt != -1) {
				used.erase(used.find(ended));
				ended = combine[tt].second;//combine[MP(str[i],ended)];
				out.pop_back();
				out.push_back(ended);
				continue;
			}
			reverse(ss.begin(),ss.end());
			tt = bs(0,(int)combine.size() - 1, ss,combine);
			if(tt != -1) {
				used.erase(used.find(ended));
				ended = combine[tt].second;//combine[MP(str[i],ended)];
				out.pop_back();
				out.push_back(ended);
				continue;
			}
			bool f = false;
			for(vector<char>::iterator it = opposed[str[i]].begin(); it != opposed[ str[i]].end(); ++it) {
				if(used.find(*it) != used.end()) {
					used.clear();
					ended = -1;
					f = true;
					out.clear();
					break;
				}
			}
			if(f)
				continue;

			ended = str[i];
			used.insert(str[i]);
			out += str[i];
		}

		printf("Case #%d: [",r + 1);
		for(int j = 0; j < (int)out.size() - 1; ++j) {
			printf("%c, ",out[j]);
		}
		if(int(out.size()) > 0) {
			printf("%c",out[out.size() - 1]);
		}
		printf("]\n");
	}
	return 0;
}
