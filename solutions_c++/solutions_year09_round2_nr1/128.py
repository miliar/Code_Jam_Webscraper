#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

#define SIZE(a) ((int)((a).size()))
#define ALL(a) (a).begin(),(a).end()
#define FILL(a) memset(&a,0,sizeof(a))
#define PB push_back
#define MP make_pair
#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i,a) for (int i = 0; i < (int)(a); ++i)
typedef long long LL;

using namespace std;

struct feat{
	double d;
	string name;
	vector<feat> list;
	feat(){
		d = 0;
		name = "";
	}
	feat(double d, string name):d(d),name(name){}
};

int pos = 0;
string s = "";

void white(){
	while (pos < s.length() && s[pos] == ' ')
		++pos;
}
void next(){
	white();
	++pos;
	white();
}

double getd(){
	double res = 0;
	while (s[pos] >= '0' && s[pos] <= '9'){
		res = res*10 + (s[pos] - '0');
		++pos;
	}
	if (s[pos] == '.'){
		double cur = 0.1;
		++pos;
		while (s[pos] >= '0' && s[pos] <= '9'){
			res += cur * (s[pos] - '0');
			cur /= 10.;
			++pos;
		}
	}
	return res;
}

feat proc(){
	next();
	double d = getd();
	white();
	feat res;
	if (s[pos] == ')'){
		res = feat(d, "");
		++pos;
		return res;
	}
	string name = "";
	while (s[pos] != ' ' && s[pos] != ')'){
		name += s[pos];
		++pos;
	}
	res = feat(d,name);
	white();
	while (s[pos] != ')'){
		res.list.PB(proc());
		white();
	}
	next();
	return res;
}

set<string> q;
feat root;

double get(feat cur){
	double res = cur.d;
	if (q.find(cur.name) != q.end()){
		if(SIZE(cur.list) > 0)
			res *= get(cur.list[0]);
	}
	else{
		if (SIZE(cur.list) > 1)
			res *= get(cur.list[1]);
	}
	return res;
}

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	REP(it,tc){
		printf("Case #%d:\n", it+1);
		int l;
		scanf("%d", &l);
		string cur;
		s = "";
		getline(cin, cur);
		REP(i,l){
			getline(cin, cur);
			s = s + " " + cur;
		}
		//cout << s << endl;
		pos = 0;
		root = proc();
		int a;
		scanf("%d", &a);
		REP(an,a){
			cin >> cur;
			int cnt;
			cin >> cnt;
			q.clear();
			REP(i,cnt){
				cin >> cur;
				q.insert(cur);
			}
			q.insert("");
			printf("%lf\n", get(root));
		}
	}
}
