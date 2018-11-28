//Флойд-Уоршелл
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <map>
#include <set>
#include <stack>
using namespace std;
 
#define sz(x) int((x).size())
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define repa(i,n) for (int (i) = 1; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define inf 1000000000
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define pi 2*acos(0.0)
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second
 
typedef vector<int> vint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
ll n,m,k,res,b;
string str;
int main( ) {
freopen("a.in","r",stdin);
freopen("a.txt","w",stdout);
cin>>n;
getline(cin,str);
rep(i,n){
	getline(cin,str);
	cout<<"Case #"<<i+1<<": ";
	rep(j,sz(str)){
		char ch;
		switch(str[j]){
			case 'a':ch='y';break;
			case 'b':ch='h';break;
			case 'c':ch='e';break;
			case 'd':ch='s';break;
			case 'e':ch='o';break;
			case 'f':ch='c';break;
			case 'g':ch='v';break;
			case 'h':ch='x';break;
			case 'i':ch='d';break;
			case 'j':ch='u';break;
			case 'k':ch='i';break;
			case 'l':ch='g';break;
			case 'm':ch='l';break;
			case 'n':ch='b';break;
			case 'o':ch='k';break;
			case 'p':ch='r';break;
			case 'q':ch='z';break;
			case 'r':ch='t';break;
			case 's':ch='n';break;
			case 't':ch='w';break;
			case 'u':ch='j';break;
			case 'v':ch='p';break;
			case 'w':ch='f';break;
			case 'x':ch='m';break;
			case 'y':ch='a';break;
			case 'z':ch='q';break;
		}
		if(str[j]==' ')ch=' ';
		cout<<ch;
	}
	cout<<endl;
}
return 0;
}

