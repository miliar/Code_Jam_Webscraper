/*
Author : OmarEl-Mohandes
PROG   : A
LANG   : C++
*/
#include <map>
#include <string>
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
#include <memory.h>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define REP(i,k,m) for(int i=k;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define oo ((int)1e9)
int main()
{
	freopen("test.in" , "rt" , stdin);
	freopen("A.out" , "wt" , stdout);
	string arr[]={"ejp mysljylc kd kxveddknmc re jsicpdrysi" ,
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" ,
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string to[]={"our language is impossible to understand",
	"there are twenty six factorial possibilities" ,
	"so it is okay if you want to just give up"};
	map<char , char>m;
	m['q'] = 'z';
	m['z'] = 'q';
	m[' '] = ' ';
	for(int i = 0 ; i < 3 ; i ++)
		for(int j = 0 ; j < arr[i].size() ; j ++)
			m[arr[i][j]] = to[i][j];
	int n ;
	cin >> n;
	string input;
	getline(cin , input);
	for(int i = 0 ; i < n ; i ++){
		getline(cin , input);
		printf("Case #%d: " , i+1);
		for(int j = 0 ; j < input.size() ; j ++)
			cout << m[input[j]] ;
		cout << endl;
	}
	return 0;
}

