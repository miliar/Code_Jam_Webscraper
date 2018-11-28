#define _HAS_CPP0X 0
#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:16777216")
#include <queue>
#include <cassert>
#include <sstream>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <iostream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
#define FOR(i, n) for(int i = 0; i < (int)(n); ++i)

void pb(){
	const string A = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
	const string B = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
	map<char, char> tr;
	for (int i = 'a'; i <= 'z'; i++)
		tr[i] = ' ';
	FOR(i, A.size())
		tr[B[i]] = A[i];
	string a, b;
	for(map<char, char>::iterator it = tr.begin(); it != tr.end(); ++it){
		a += it->first;
		b += it->second;
	}
	cout << a << endl << b << endl;
}
void Go(){
	static const string A = "abcdefghijklmnopqrstuvwxyz";							  
	static const string B = "ynficwlbkuomxsevzpdrjgthaq";
							 
	string s;
	getline(cin, s);
	FOR(i, s.size()){
		FOR(j, B.size()){
			if (B[j] == s[i]){
				s[i] = A[j];
				break;
			}
		}
	}
	cout << s;
}

int main(){
	const string task = "A";
	const int attempt = 0;
	const bool dbg = false;


	if (dbg){
		freopen("inp.txt", "r", stdin);
	}
	else{
		stringstream ss;
		ss << "gcj/2012/qual/";
		if (attempt < 0)
			ss << task << "-large";
		else
			ss << task << "-small-attempt" << attempt;
		freopen((ss.str() + ".in").c_str(), "r", stdin);
		freopen((ss.str() + ".out").c_str(), "w", stdout);
	}
	//pb();

	int t;
	scanf("%d", &t);
	string ss;
	getline(cin, ss);
	FOR(i, t){
		printf("Case #%d: ", i + 1);
		Go();
		printf("\n");
	}
	return 0;
}