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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <sstream>
#include <queue>

using namespace std;

#define ALL(v) (v.begin(),v.end())
#define sz(x) ((int)(x).size())
#define pb push_back
typedef vector<int> vi;

const int INF (0x3f3f3f3f);

int dx[] = {1,0,-1,0}, dy[] = {0,1,0,-1};


typedef long long LL;

ifstream fin ("A-small-attempt0.in");
ifstream f ("f.txt");
ofstream fout ("A-small-attempt0.out");

map <char,char> mp;

int main (){
	string str1,str2;
	for (int i=0;i<3;i++){
		f >> str1; f >> str2;
		for (int j=0;j<str1.length();j++){
			mp[str1[j]]=str2[j];
		}
	}
	mp['q'] = 'z';
	mp['z'] = 'q';
	mp[' '] = ' ';
	f.close();
	int T;
	string str;
	fin >> T;
	getline(fin,str);
	string str3;
	for (int i=0;i<T;i++){
		str = "";
		str3 = "";
		getline(fin,str);
		for (int j=0;j<str.length();j++){
				str3 += mp[str[j]];
		}
		fout << "Case #" << i+1 << ": " << str3 << endl; 
	}

	return 0;
}