#include <iostream>
#include <string>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <cctype>
#include <sstream>
#include <cstring>
#include <list>
using namespace std;
#define oo (1<<31-1)
#define INFI (1e31)
#define ll long long
#define ull unsigned long long
#define PB(x) push_back(x)
#define ALL(x) (x).begin(),(x).end()
#define REP(i,l) for(int i=0;i<l;i++)
#define FOR(i,a,b) for(int i=a;i<b;i++)
int solve();


int main(){
	int T;
	cin>>T;
	REP(i,T){
	printf("Case #%d: %d\n",i+1,solve());
	}
return 0;}
int solve(){
	int N,S,q;
	cin>>N>>S>>q;	
	vector<int> m0,m2,m1;
	vector<int> ans;
	for(int i=0,j;i<N;i++){
		cin>>j;
		if(j<=1||j>=29){
			if(j==0||j==30) ans.PB(j/3);
			else ans.PB(j/3+1);
		}else{
			if(j%3==0) m0.PB(j);
			else if(j%3==1) m1.PB(j);
				else m2.PB(j);
		}
	}

	for(int i=0;i<m2.size();i++){
		if(m2[i]/3+1<q){
			if(m2[i]/3+2>=q&&S){
				S--;
				ans.PB(m2[i]/3+2);
			}
		}else{
			ans.PB(m2[i]/3+1);
		}
	}
	for(int i=0;i<m0.size();i++){
		if(m0[i]/3<q){
			if(m0[i]/3+1>=q&&S){
				S--;
				ans.PB(m0[i]/3+1);
			}
		}else{
			ans.PB(m0[i]/3);
		}
	}
	for(int i=0;i<m1.size();i++){
		ans.PB(m1[i]/3+1);
	}
	int cont=0;
	for(int i=0;i<ans.size();i++){
		if(ans[i]>=q)
			cont++;
	}
	return cont;
}
