#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
#define PB push_back
#define MP make_pair

typedef long long LL;

int T, tst;
int c, d;
int op[30][30];
string st;
string g[30][30];
int n;

void work()
{
	for(int i = 0; i < 26; ++i)
	for(int j = 0; j < 26; ++j) g[i][j] = "";
	memset(op, 0, sizeof(op));
	
	cin>> c;
	for(int i = 0; i < c; ++i) {
		string tmp;
		cin>> tmp;
		//cout<< << endl;fflush(stdout);
		g[tmp[0]-'A'][tmp[1]-'A'] = g[tmp[1]-'A'][tmp[0]-'A'] = tmp.substr(2,1);
		
	}
	cin>> d;
	for(int i = 0; i < d; ++i) {
		string tmp;
		cin>> tmp;
		op[tmp[0]-'A'][tmp[1]-'A'] = op[tmp[1]-'A'][tmp[0]-'A'] = 1;
	}
	
	cin>> n;
	st = "";
	for(int i = 0; i < n; ++i) {
		//cout<< st<< endl;fflush(stdout);
		char ch;
		cin>> ch;
		string aa = " "; aa[0] = ch;
		st.append(aa);
		int l = st.size();
		if(l > 1 && g[st[l-1]-'A'][st[l-2]-'A'] != "") {
			string t = (g[st[l-1]-'A'][st[l-2]-'A']);
			st.erase(l-2, 2);
			st.append(t);
		}
		l = st.size();
		for(int i = 0; i < l-1; ++i) if(op[st[l-1]-'A'][st[i]-'A']) {
			st = "";
			break;
		}
	}
	
	if(st.size()>1)
	for(int i = 0; i < st.size()-1; ++i)
		printf("%c, ", st[i]);
	if(st.size()>0)
		printf("%c", st[st.size()-1]);
	puts("]");
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	cin>> T;
	while(tst < T) {
		printf("Case #%d: [", ++tst);
		work();
	}
	
	return 0;
}
