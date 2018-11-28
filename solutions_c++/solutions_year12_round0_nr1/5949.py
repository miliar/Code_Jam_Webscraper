#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <fstream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <iterator>
#include <cassert>
#include <stack>
#include <queue>
#include <ctime>
#include <vector>
#include <map>
#include <set>
#include <utility>

using namespace std;

#define FORALL(i,a,b) for (int i = (a); i <= (b); i++)
#define FOR(i,n) for (int i=0;i<n;i++)
#define FORB(i,a,b) for (int i = (a); i >= (b); i--)
#define FORIN(it,type,b) for(type::iterator it = (b).begin(); it != (b).end(); it++)
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long double ld;

#define in cin
#define out cout
#define dout if(true) cout

#define ASCII 300
char toeng[ASCII];
char togog[ASCII];

void remember(string gog, string eng){
	int N = gog.length();
	int M = eng.length();
	
	assert(N==M);
	
	FOR(i,N){
		toeng[tolower(gog[i])] = tolower(eng[i]);
		togog[tolower(eng[i])] = tolower(gog[i]);
		toeng[toupper(gog[i])] = toupper(eng[i]);
		togog[toupper(eng[i])] = toupper(gog[i]);
	}
}
string translate(string gog){
	int N = gog.length();
	string ans;
	FOR(i,N){
		ans += toeng[gog[i]];
	}
	return ans;
}

int main()
{
	remember("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	remember("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	remember("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
	remember("y","a");
	remember("e","o");
	remember("q","z");
	remember("z","q");
	for(char c = 'a'; c <= 'z'; c++) if(toeng[c] == 0) cout << c;
	for(char c = 'A'; c <= 'Z'; c++) if(toeng[c] == 0) cout << c;
	for(char c = 'a'; c <= 'z'; c++) if(togog[c] == 0) cout << c;
	for(char c = 'A'; c <= 'Z'; c++) if(togog[c] == 0) cout << c;
	for(char c = 'a'; c <= 'z'; c++) assert(togog[toeng[c]] == c);
	for(char c = 'A'; c <= 'Z'; c++) assert(togog[toeng[c]] == c);
	
	toeng[' '] = togog[' '] = ' ';
	
	int T;
	in >> T;
	in.ignore();
	FORALL(test,1,T){
		string line;
		getline(in,line);
		cout << "Case #" << test << ": " << translate(line) << endl;
	}
};