#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;


int t;
int N,M,ans;
set <string> sys;
int add(string);
int main() {
//	freopen("f://a-small.in","r",stdin);freopen("f://a-small.out","w",stdout);
	freopen("f://a-large.in","r",stdin);freopen("f://a-large.out","w",stdout);
	cin>>t;
	int len=0;
	string src;
	for(int i=1;i<=t;i++){
		
		cin>>N>>M;
		ans=0;
		sys.clear();
		sys.insert("/");
		for(int j=0;j<N;j++) {
			cin>>src;
			add(src);
		}
		for(int j=0;j<M;j++) {
			cin>>src;
			ans+=add(src);

		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	
}
int add(string s) {
	int res=0;

	for(int i=1;i<s.size();i++){
		if(s[i]=='/'){
			string tmp(s,0,i);
			if(sys.count(tmp)==0){
				res++;
				sys.insert(tmp);
	//			cout<<tmp<<endl;
			}
		}
	}
	if(sys.count(s)==0) {
		res++;
		sys.insert(s);
	}
	return res;
}