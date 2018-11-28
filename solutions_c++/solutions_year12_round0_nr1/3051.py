#include <iostream>
#include <fstream>
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define EPS 1e-9
#define INF MOD
#define MOD 1000000007LL
#define fir first
#define iss istringstream
#define sst stringstream
#define ite iterator
#define ll long long
#define mp make_pair
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<n;i++)
#define pi pair<int,int>
#define pb push_back
#define sec second
#define sh(i) (1LL<<i)
#define sz size()
#define vi vector<int>
#define vc vector
#define vl vector<ll>
#define vs vector<string>

string s=
"ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
string t=
"our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

char c[128];

int main(){
	rep(i,s.sz)if(s[i]!=' '){
		c[s[i]]=t[i];
	}
	//rep2(i,'a','z'+1)cout<<(char)i<<" -> "<<c[i]<<endl;
	c['q']='z';
	c['z']='q';
	int T;
	cin>>T;
	string S;
	getline(cin,S);
	rep(tc,T){
		cout<<"Case #"<<tc+1<<": ";
		getline(cin,S);
		rep(i,S.sz){
			if(S[i]==' ')cout<<' ';
			else cout<<c[S[i]];
		}
		cout<<endl;
	}
}
