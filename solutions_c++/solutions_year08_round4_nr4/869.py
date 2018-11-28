#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

#define dbg(x) cout << #x << " -> " << x << "\t" << flush;
#define dbge(x) cout << #x << " -> " << x << "\t" << endl;
#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define EACH(i,v) FOR(i,(v).begin(),(v).end())
#define cs c_str()
#define pb push_back
#define sz size()
#define INF (int)1e9+1

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;

int fn(int k,string s){
	int ret=INF;
	VI a(k,0);
	int bl=1;
	REP(i,k)	a[i]=i;
	do{
		string dum="";
		
		REP(i,s.sz)	dum+='z';
		REP(i,s.sz){
			bl= (i/k)+1;
			int pos= (bl-1)*k+a[i%k];
			dum[pos]=s[i];
			
			
		}
		
		int cnt=0;
		REP(i,dum.sz){
			int j;
			for(j=i+1;j<dum.sz && dum[j]==dum[i];j++);
			cnt++;
			i=j-1;
		}
		ret<?=cnt;
	}while(next_permutation(a.begin(),a.end()));
	
	return ret;
}

int main(){
	
	int Kase;
	scanf("%d",&Kase);
	FOR(kase,1,Kase+1){
		int k;
		string s="";
		char z[100005];
		cin>>k;cin.get();
		cin>>z;
		for(int i=0;z[i];i++)	s+=z[i];
		
		int ans= fn(k,s);
		printf("Case #%d: %d",kase,ans);
		printf("\n");
	}
	return 0;
}
