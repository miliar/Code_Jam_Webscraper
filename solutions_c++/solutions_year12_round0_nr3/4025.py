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
ll n,a,b,res;
string str,str1,str2;
int main( ) {
freopen("a.in","r",stdin);
freopen("a.txt","w",stdout);
cin>>n;
rep(i,n){
	res=0;
	cin>>a>>b;
	cout<<"Case #"<<i+1<<": ";
	FOR(j,a,b){
		stringstream ss;
		ss<<j;
		str=ss.str();		
		for(int k=2;k<=sz(str);k++){
			str1=str.substr(k-1,sz(str)-k+1)+str.substr(0,k-1);
			if(str1==str)break;
		int c=1,h=0;
		for(int l=sz(str1)-1;l>=0;l--){
			h+=(str1[l]-'0')*c;
			c*=10;
		}
		if(h<=b&&h>j)res++;
	}
	}
	cout<<res<<endl;
}
return 0;
}

