# include <cstdio>
# include <iostream>
# include <fstream>
# include <algorithm>
# include <vector>
# include <string>
# include <set>
# include <utility>
# include <map>
# include <queue>
# include <stack>
# include <list>
# include <bitset>
# include <deque>
# include <cassert>
# include <iomanip>
# include <cmath>
# define pb push_back
# define forn(i,n) for (int i=0; i<(int)n; ++i)
# define ford(i,n) for (int i=n-1; i>=0; --i)
# define get(a,b); a b; cin >> b;
# define ull unsigned long long
# define ll long long
# define ld long double
# define mp make_pair
# define matrix vector < vector <int> > 
# define all(a) a.begin(), a.end()
# define INF 1e9
# define eps 1e-9
using namespace std;

int main(){
	ifstream cin ("B-small-attempt0.in");
	ofstream cout ("B-small-attempt0.out");
	int t;
	cin >> t;
	forn(test,t){
		int n;
		cin >> n;
		map <string,char> comb;
		forn(i,26)
			forn(j,26){
				string tt = "" + char('A'+i) + char('A'+j);
				comb[tt] = '#';
			}

		map <char,char> bad;
		string s;
		forn(i,n){
			cin >> s;
			string tt = s.substr(0,2);
			comb[tt] = s[2];
			reverse(all(tt));
			comb[tt] = s[2];
		}
		int m;
		cin >> m;
		forn(i,m){
			cin >> s;
			bad[s[0]] = s[1];
			bad[s[1]] = s[0];
		}
		string seq;
		cin >> m;
		cin >> seq;
		string cur = "";
		forn(j,seq.size()){
			cur += seq[j];
			char c = ' ';
			while (cur.size()>=2 && c!='#'){
				s = cur.substr(cur.size()-2,2);
				c = comb[s];
				if (c<'A' || c>'Z') c = '#';
				if (c!='#')
					cur = cur.substr(0,cur.size()-2) + c;
			}
			forn(i,cur.size())
				if (cur[cur.size()-1] == bad[+cur[i]])
					cur.clear();
		}
		string ans;
		ans = "[";
		forn(i,cur.size()){
			s = "";
			s += cur[i];
			s += ", ";
			ans += s;
		}
		while (ans.size()>0 && (ans[ans.size()-1]<'A' || ans[ans.size()-1]>'Z'))
			ans.erase(ans.size()-1,1);
		if (ans.size() == 0)
			ans = "[";
		ans += ']';
		cout << "Case #" << test+1 << ": " << ans << endl;
	}
    return 0;
}
