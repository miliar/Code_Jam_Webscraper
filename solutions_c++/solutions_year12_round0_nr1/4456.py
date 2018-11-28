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
#include <list>
#include <cassert>
#include <conio.h>
using namespace std; 

#define PB push_back 
#define MP make_pair 
#define SZ(v) ((int)(v).size()) 
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n) 
#define FORE(i,a,b) for(int i=(a);i<=(b);++i) 
#define REPE(i,n) FORE(i,0,n) 
#define FORSZ(i,a,v) FOR(i,a,SZ(v)) 
#define REPSZ(i,v) REP(i,SZ(v)) 
typedef long long ll; 


int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);


	string	s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv",
			s2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	
	map<char, char> dic;
	REP(i, s1.length()) dic[s1[i]] = s2[i];
	dic['q'] = 'z';
	dic['z'] = 'q';

	/*
	for( map<char,char>::iterator ii = dic.begin(); ii!=dic.end(); ++ii)
   {
       cout << (*ii).first << ": " << (*ii).second << endl;
   }
	*/

	int T;	
	cin >> T;
	cin.get();
	REP(i, T)
	{
		char str[101];
		cin.getline(str, 101);
		REP(k, 101) if ((str[k] >= 'a')&(str[k] <= 'z')) str[k] = dic[str[k]];
		cout << "Case #" << i+1 << ": " << str << endl;
	}

	//getch();
	return 0;
}