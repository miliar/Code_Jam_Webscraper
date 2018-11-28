#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<deque>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
string c="yhesocvxduiglbkrztnwjpfmaq";
int main(){
	int i,t,j;string s;cin>>t;getline(cin,s);
	rep(i,t){
		getline(cin,s);
		rep(j,s.size()){
			if(s[j]!=' ') s[j]=c[(s[j]-'a')];
		}
		cout<<"Case #"<<i+1<<": "<<s<<endl;
	}
	return 0;
}
