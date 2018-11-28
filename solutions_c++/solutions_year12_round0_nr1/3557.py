/// In The Name Of God

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstring>


using namespace std;

#define REP(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

string s;
char mp[100]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q' };

int main(){
	//ios::sync_with_stdio(false);
	int n,t,i,tsc;
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	cin>>tsc;
	getline(cin,s);
	REP(t,tsc){
		printf("Case #%d: ",t+1);
		getline(cin,s);
		REP(i,s.size())
			if(s[i]!=' ')
			cout<<mp[s[i]-'a'];
			else cout<<" ";
		cout<<endl;
	}
	return 0;
}