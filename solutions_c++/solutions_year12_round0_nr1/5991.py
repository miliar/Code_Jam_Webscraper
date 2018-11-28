#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <string.h>
#include <time.h>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

using namespace std;

#define rep(i,a,b) for(int i=(int)a; i<(int)b; ++i)
#define irep(i,a,b) for(int i=(int)a; i>=(int)b; --i)
#define pb push_back
#define mp make_pair
#define inf (1 << 30)
#define infH 0x7F7F7F7F
#define all(v) v.begin(),v.end()
#define clr(v) v.clear()
#define setV(Vect,Tam,Val) Vect.assign(Tam,Val)
#define setA(Arr,Tam,Val) memset(Arr,Val,Arr+Tam)
#define MAX 25

typedef long long i64;
typedef pair < int, int > pii;
typedef vector < int > vi;
typedef vector < vi > vvi;
typedef vector < pii > vpii;
typedef vector < i64 > vi64;

struct point2d{int x,y;};

//char M[30];
char M[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main(){
/*	vector < string > v;
	string str;
	rep(i,0,3){
		getline(cin, str);
		v.pb(str);
	}
	rep(i,0,3){
		getline(cin, str);
		rep(j,0,str.size()) if(str[j]!=' '){
//			printf("%c : %c\n", v[i][j], str[j]);
			M[v[i][j]-'a'] = str[j];
		}
	}
	rep(i,0,26){
		//printf("%c = %c\n", M[i], i+'a');
		if(i+'a'=='q') M[i]='z', M['z'-'a']='q';
		cout << "'" << M[i] << "',";
	}
	cout << endl;
	*/
	string str;
	int n;
	cin >> n;
	getline(cin, str);
	rep(i,0,n){
		getline(cin, str);
		cout << "Case #" << (i+1) << ": ";
		rep(i,0,str.size()) if(str[i]==' ') cout << " ";
		else cout << M[str[i]-'a'];
		cout << endl;
	}
   return 0;
}
