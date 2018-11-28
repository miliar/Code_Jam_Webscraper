#include<iostream>
#include<algorithm>
#include<list>
#include<vector>
#include<map>
#include<set>
#include<string>
#include<stack>
#include<math.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<fstream>

#define MIN(X,Y) (X < Y ? X : Y)
#define MAX(X,Y) (X > Y ? X : Y)
#define LENGTH(X) ((int)(X.length()))
#define SIZE(X) ((int)(X.size()))
#define SET(x,t) memset(x, t, sizeof(x))
#define FOR(i,x,y) for(int i = x; i < y; i++)

using namespace std;
fstream fin("A-large.in", ios::in);
fstream fout("A-large.out", ios::out);

//bool mark[5000];
string words[5000];
int L, D, N;

int solve(string & s){
	int pos = 0;
	list <string> remain, temp;
	for (int i = 0; i < D; i ++)
		remain.push_back(words[i]);
	for (int i = 0; i < L; i ++){
		string ss;
		if ( s[pos] == '(' ){
			int len;
			int j;
			for (j = pos + 1; ; j ++)
				if (s[j] == ')'){
					len = j - pos - 1;
					break;
				}
			ss = s.substr(pos + 1, len);
			pos = j + 1;
		}
		else {
			ss = s[pos];
			pos ++;
		}
		for (list<string>::iterator it = remain.begin(); it != remain.end(); it ++){
			string & s3 = * it;
			char c3 = s3[i];
			for (int j = 0; j < ss.length(); j ++){
				if (c3 == ss[j]){
					temp.push_back(s3);
					break;
				}
			}
		}
		remain = temp;
		temp.clear();
	}
	return remain.size();
}

int main(){
	//memset(mark , false, 5000);
	fin >> L >> D >> N;
	for (int i = 0; i < D; i ++){
		fin >> words[i];
	}
	for (int i = 0; i < N; i ++){
		string s;
		fin >> s;
		fout << "Case #" << i + 1 << ": " << solve(s) << endl;
	}
	
	return 0;
}
