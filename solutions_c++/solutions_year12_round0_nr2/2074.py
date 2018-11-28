#include <iostream>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>
#include <stack>
#include <map>
#pragma comment(linker, "/STACK:165777216")
using namespace std;
int n;
int a[113];
int p;
int s;
int solve(){
	int dva,mda;
	int ans=0;
	for(int i=0; i<n; i++){
		dva=a[i]/3;
		mda=a[i]%3;
		if(dva>=p) {
			ans++;
			continue;
		}
		if(mda!=0 && (dva+1)>=p) {
			ans++;
			continue;
		}
		if((dva+mda)>=p && s>0) {
			ans++;
			s--;
			continue;
		}
		if(dva!=0){
			if((dva+1)>=p && s>0) {
				ans++;
				s--;
				continue;
			}
		}
	}
	return ans;
}
int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int t;
	cin>>t;
	for(int i=0; i<t; i++){
		cin>>n>>s>>p;
		for(int j=0; j<n; j++){
			cin>>a[j];
		}
		cout<<"Case #"<<i+1<<": "<<solve()<<endl;
	}
	return 0;
}