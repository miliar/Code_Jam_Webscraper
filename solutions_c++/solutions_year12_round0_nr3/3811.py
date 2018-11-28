#include <iostream>
#include <cstdio>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <memory.h>
#include <algorithm>
#include <cstdlib>
#include <cassert>
#include <sstream>
#include <fstream>
using namespace std;
void solve();

#define pb push_back
#define mp make_pair

typedef long long li;
typedef vector<li> vi;
typedef pair<int, int> pi;

int main() {
	freopen("input", "r", stdin);
	freopen("output","w", stdout);
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	string s;
	getline(cin,s);
	for(int i=1;i<=t;++i){
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<"\n";
	}
	return 0;
}

void solve(){
	int a,b;
	cin>>a>>b;
	int power[]={0,1,10,100,1000,10000,100000,1000000,10000000};
	int len = 1;
	while(a>=power[len+1])
		++len;
	int ans = 0;
	for(int i=a;i<=b;++i){
		set<int> s;
		int next = i;
		for(int j=1;j<len;++j){
			next = (next%10)*power[len] + (next/10);
			//cout<<i<<' '<<next<<endl;
			if(next > i && next <= b && s.find(next)==s.end()){
				++ans;
				s.insert(next);
			}
		}
	}
	cout<<ans;
}