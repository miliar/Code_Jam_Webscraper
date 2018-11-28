#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <sstream>
#include <queue>

#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>

#define forn(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(__typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define ALL(x)   (x).begin(),(x).end()
#define SIZE(x)   (int)(x).size()
#define SORT(x) sort(ALL(x))
using namespace std;
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
typedef long long ll;

int contar(string &s){
	s += ".";
	int last = 0;
	int ind = last;
	int res = 0;
// 	cout << s << endl;
	for(int i = 0 ;i < (int)s.size()-1;i++){
		last = i;
		while(s[i] == s[last]){
			i++;
		}
		res++;
		i--;
	}
	return res;
}

int main(){
	int i,j ,k;
	int casos;cin >> casos;
	for(int h = 0 ; h < casos; h ++ ){
		string s;int res = 1090000;
		cin >> k >> s;
		int arr[5];
		for(i=0;i<k;i++) arr[i] = i;
// 		cout << s << endl;
		do{
			string t="";
			for(i=0;i<(int)s.size()/k;i++){
				for(j=0;j<k;j++){
					t += s[i*k+arr[j]];
// 					printf("%i\n", i*k+arr[j]);
				}
			}
// 			cout << t << endl;
			res = min ( res, contar(t) );
		}while(next_permutation(arr, arr+k));
		printf("Case #%i: %i\n", h+1, res);
	}


	return 0;
}


























