#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<sstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;

#define LET(x,a) 	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	IFOR(it,v.begin(),v.end())
#define FOR(i,a,b)  	for(int i=(int)(a) ; i < (int)(b);++i)
#define REP(i,n) 	FOR(i,0,n)
#define PB		push_back
#define MP 		make_pair
#define EPS		1e-9
#define INF 2000000000

typedef vector<int>	VI;
typedef long long	LL;
typedef pair<int,int>	PI;

string s[10000];
int present[20][50];

int main(){
	int l,d,n;
	cin>>l>>d>>n;
	REP(i,d)cin>>s[i];
	REP(times,n){
		memset(present,0,sizeof(present));
		string s1;
		cin>>s1;
		bool st=1;
		int index=0;
		REP(i,s1.length()){
			if(s1[i]=='('){
				st=0;
			}
			else if(s1[i]==')'){
				st=1;
				index++;
			}
			else if(st){
				present[index][s1[i]-'a']=1;
				index++;
			}
			else {
				present[index][s1[i]-'a']=1;
			}
		}
		int cnt=0;
		REP(i,d){
			bool poss=1;
			REP(j,l)if(!present[j][s[i][j]-'a'])poss=0;
			cnt+=poss;
		}
		cout<<"Case #"<<times+1<<": "<<cnt<<endl;
	}
	return 0;
}
