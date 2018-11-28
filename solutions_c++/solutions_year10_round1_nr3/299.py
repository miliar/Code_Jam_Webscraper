#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>
#include <sstream>
using namespace std;
int T, TT;
int ans, a1, a2, b1, b2;

bool get(int x, int y){
//	cout<<x<<"  "<<y<<endl;
	int a, b;
	if (x<y) {x=x+y; y=x-y; x=x-y;}
	a=x%y; b=x/y;
	if (a==0) return true;
	bool aa=get(y, a);
	if (!aa) return true;
	if (b>=2) return true;
	return false;
}

int main(){
	freopen("c.in","r",stdin);
	freopen("c.txt","w",stdout);
	cin>>T;
	
	for(int TT=1; TT<=T; ++TT){
		ans=0;
		cin>>a1>>a2>>b1>>b2;
		for(int i=a1; i<=a2; ++i){
			for(int j=b1; j<=b2; ++j){
				if (i==j) continue;
				if (get(i, j)) {//cout<<i<<" "<<j<<endl;
				++ans;}	
			}	
		}
		cout<<"Case #"<<TT<<": "<<ans<<endl;	
	}	
	//cin>>T;
}
