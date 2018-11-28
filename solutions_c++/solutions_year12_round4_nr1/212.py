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


#define pb push_back
#define mp make_pair

typedef long long li;
typedef vector<li> vi;
typedef pair<int, int> pi;
string solve();
int main() {
	freopen("input", "r", stdin);
	freopen("output","w", stdout);
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	string s;
	getline(cin,s);
	cout<<fixed;
	cout.precision(30);
	for(int i=1;i<=t;++i){
		cout<<"Case #"<<i<<": ";
		cout<<solve();
		cout<<'\n';
	}
	return 0;
}
struct vine{
	int d, len;
};

vine v[10100];

string solve(){
	int n;
	cin>>n;
	for(int i=0;i<n;++i){
		cin>>v[i].d>>v[i].len;
		//v[i].len = min(v[i].len, v[i].d);
	}
	int d;
	cin>>d;
	int ok[10101];
	memset(ok, 0,sizeof(ok));
	ok[0] = v[0].d;
	for(int i=0;i<n;++i){
		if(!ok[i])
			continue;
		if(v[i].d + ok[i] >=d)
			return "YES";
		
		for(int j=i+1;j<n;++j){
			if(v[i].d + ok[i] >= v[j].d){
				ok[j] = max(ok[j], min(v[j].len, v[j].d - v[i].d));
			}
			else
				break;
		}
	}
	return "NO";
}

