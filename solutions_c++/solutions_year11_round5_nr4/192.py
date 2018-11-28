#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <iterator>
#include <bitset>
#include <sstream>
#include <cmath>
#include <cstring>

using namespace std;

#define LL long long

LL ans=0;

bool is_square(LL cur){
	LL tmp=(LL)(sqrt((cur))+1e-5);
	if (cur==tmp*tmp) return true;
	return false;
}

int main(){
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int t;cin >> t;
	for (int i=1;i<=t;i++){
		
		cout << "Case #"<< i << ":" <<" ";
		string s;cin >> s;
		vector<LL> v;v.clear();
		LL cur=0;
		for (LL j=0;j<s.size();j++)
			if (s[s.size()-j-1]=='?'){
				v.push_back((1ll<<j));
			}else if (s[s.size()-j-1]=='1') cur+=(1ll<<j);
		
		for (LL j=0;j<((1ll<<(LL)(v.size())));j++){
			LL tmp=0;
			for (LL k=0;k<v.size();k++)
				if ((j&(1ll<<k))) tmp+=v[k];
			if (is_square(tmp+cur)) {
				ans=tmp+cur;
			}
		}
		for (LL j=0;j<s.size();j++)
			if ((ans&(1ll<<(s.size()-j-1)))) putchar('1');
			else putchar('0');
		puts("");
	}
	return 0;
}
