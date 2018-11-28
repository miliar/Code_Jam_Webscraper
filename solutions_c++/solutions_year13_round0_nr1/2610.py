//Template

// By Anudeep :)
//Includes
#include <vector> 
#include <queue>
#include <map> 
#include <set>
#include <utility> //Pair
#include <algorithm>
#include <sstream> // istringstream>> ostring stream<<
#include <iostream> 
#include <iomanip> 
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 << endl; prints xxx77
//setprecision - cout << setprecision (4) << f << endl; Prints x.xxxx
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

//M lazy ;)
typedef long long ll;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <string> vs;
typedef pair< int ,int > pii;
typedef vector <ll> vll;
typedef istringstream iss;
typedef ostringstream oss;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define ln length()
#define rep(i,n) for(int i=0;i<n;i++)
#define all(a)  a.begin(),a.end() 
#define ESP (1e-9)

char s[5][5];
int test=0;
void testcase() {
	test++;
	int x,o,ans=0,dot=0;
	rep(i,4) scanf("%s",s[i]);
	//Check vertical
	rep(j,4) {
		x=1; o=1;
		rep(i,4) {
			if(s[i][j]=='.') dot=1;
			if(s[i][j]=='.' || s[i][j]=='O') x=0;
			if(s[i][j]=='.' || s[i][j]=='X') o=0;
		}
		if(x) ans|=1;
		if(o) ans|=2;
	}
	
	//check horizontal
	rep(i,4) {
		x=1; o=1;
		rep(j,4) {
			if(s[i][j]=='.' || s[i][j]=='O') x=0;
			if(s[i][j]=='.' || s[i][j]=='X') o=0;
		}
		if(x) ans|=1;
		if(o) ans|=2;
	}
	//Diagonals
	x=1; o=1;
	rep(i,4) {
		if(s[i][i]=='.' || s[i][i]=='O') x=0;
		if(s[i][i]=='.' || s[i][i]=='X') o=0;
	}
	if(x) ans|=1;
	if(o) ans|=2;
	x=1; o=1;
	rep(i,4) {
		if(s[i][3-i]=='.' || s[i][3-i]=='O') x=0;
		if(s[i][3-i]=='.' || s[i][3-i]=='X') o=0;
	}
	if(x) ans|=1;
	if(o) ans|=2;
	
	printf("Case #%d: ",test);
	if(ans==0) {
		if(dot) printf("Game has not completed\n");
		else printf("Draw\n");
	}
	else if(ans==3) {
		printf("Draw\n");
	}
	else if(ans==1) {
		printf("X won\n");
	}
	else {
		printf("O won\n");
	}
}
	
int main() {
	int t;
	scanf("%d",&t);
	while(t--) testcase();
	return 0;
}