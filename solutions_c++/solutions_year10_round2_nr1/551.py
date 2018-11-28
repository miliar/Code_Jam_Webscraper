#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <fstream>
#include <string>
//#include <windows.h>

using namespace std;

#define rep(i,n) for(int i = 0; i < n; i++)
#define rep1(i,n) for(int i = 1; i <= n; i++)
#define repk(i,k,n) for(int i = k; i < n; i++)
#define clr(a,x) memset(a,x,sizeof(a))
#define clearqueue(x) while(!x.empty()) x.pop();
#define clearvector(arr,n) rep(i,n)arr[i].clear();

string getTill(stringstream& ss, char c){
	char x;
	string s = "";
		ss.get(x);
	while(!ss.eof()){
		if(x == c) break;
		s+=x;
		ss.get(x);
	}
	return s;
}

int main()
{
	ifstream cin("A-large.in");
	ofstream cout("1.txt");
//	ios_base::sync_with_stdio(0);
//	long long begin = GetTickCount();
//	long long end = GetTickCount();
//	include <window.h>
	int t, n, m, cnt = 0, casenum = 1;
	stringstream ss;
	string s, tt;
	set<string> game;
	cin >> t;
	while(t--){
		cin >> n >> m;
		getline(cin, s);
		rep(i,n){
			getline(cin, s);
			ss << s;
			s = getTill(ss, '/');

			s = getTill(ss, '/');
			game.insert(s);
			while(!ss.eof()){
				tt = getTill(ss, '/');
				s+='/'+tt;
				game.insert(s);
			}
			ss.clear();
		}
		cnt = 0;
		rep(i,m){
			getline(cin, s);
			ss << s;
			s = getTill(ss, '/');
			s = getTill(ss, '/');
			if(game.find(s) == game.end()){
				game.insert(s);
				cnt++;
			}
			while(!ss.eof()){
				tt = getTill(ss, '/');
				s+='/'+tt;
				if(game.find(s) == game.end()){
					game.insert(s);
					cnt++;
				}
			}
			ss.clear();
		}

		cout << "Case #" << casenum++ << ": " << cnt << endl;
		game.clear();
	}

	return 0;
}