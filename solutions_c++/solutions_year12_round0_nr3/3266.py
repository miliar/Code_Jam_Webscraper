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
//int sumi1[2500][2500],sumi2[2500][2500];
bool can(string a,string b){
	int i,n=a.size(),m=b.size();
	if(n!=m) return false;
	rep(i,n){
		if(a==b.substr(i)+b.substr(0,i)) return true;
	}
	return false;
}
int de(string a){
	int ret=0,i,n=a.size();rep(i,n) ret=ret*10+(a[i]-'0');return ret;
}
string moji(int a){
	string ret="";string r="";int amari;
	if(a==0) return "0";if(a<0) return "-"+moji(-a);
	while(a>0){
		amari=a%10;r+=(amari+'0');a/=10;
	}
	for(int i=0;i<r.size();i++) ret+=r[r.size()-(i+1)];
	return ret;
}
int cal(int a,int ma){
	string b=moji(a);
	int n=b.size(),i,ret=0;
	vector <int> t;
	rep(i,n) t.pb(de(b.substr(i)+b.substr(0,i)));
	sort(All(t));
	t.erase(unique(All(t)),t.end());
	rep(i,t.size()){
		if(t[i]<=ma && t[i]>a){
//			if(!can(moji(a),moji(t[i]))) cout<<a<<' '<<t[i]<<endl;
			ret++;//sumi1[a][t[i]]++;
		}
	}
	return ret;
}
int main()
{
//	memset(sumi1,0,sizeof(sumi1));
//	memset(sumi2,0,sizeof(sumi2));
	int i,j,k,a,b,t;
	cin>>t;
	rep(i,t){
		cin>>a>>b;int ret=0,ret2=0;
		REP(j,a,b+1) ret+=cal(j,b);
//		REP(j,a,b) REP(k,j+1,b+1){
//			if(can(moji(j),moji(k))){sumi2[j][k]++;ret2++;}
//		}
		cout<<"Case #"<<i+1<<": "<<ret<<endl;
//		cout<<"Case #"<<i+1<<": "<<ret<<' '<<ret2<<endl;
	}
//	rep(i,2500) rep(j,2500){
//		if(sumi1[i][j] && !sumi2[i][j]) cout<<i<<' '<<j<<'a'<<endl;
//		if(!sumi1[i][j] && sumi2[i][j]) cout<<i<<' '<<j<<'b'<<endl;
//		if(sumi1[i][j]!=sumi2[i][j]) cout<<i<<' '<<j<<' '<<sumi1[i][j]<<' '<<sumi2[i][j];
//	}
	return 0;
}
