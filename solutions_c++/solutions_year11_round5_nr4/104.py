#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <queue>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <set>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


typedef long long int64;
bool is(int64 a){
	int64 s=sqrt((double)a);
	if( s*s == a ) return true;
	if( (s+1)*(s+1) == a) return true;
	if( (s-1)*(s-1) == a) return true;
	return false;
}

int main(){
	freopen("D-small-attempt0(1).in","r",stdin);
	freopen("D-small-attempt0(1).out","w",stdout);

	int cas,Te=1;
	cin>>cas;
	while( cas-- ){
		string ans;
		string s; cin>>s;
		int num=0;
		reverse(s.begin(),s.end());
		for(int i=0;i<s.length();i++){
			if( s[i]=='?' ) num++;
		}
		for(int state=0;state<(1<<num);state++){
			int j=0;
			int64 one=1,tmp=0;
			for(int i=0;i<s.length();i++){
				if( s[i]=='0' ) continue;
				if( s[i]=='1' ){
					tmp+=one<<i;
				}else{
					if( state&(1<<j) ){
						tmp+=one<<i;
					}
					j++;
				}
			}
			if( is(tmp) ){
				ans=s;
				for(int j=0,i=0;i<ans.length();i++){
					if( ans[i]=='?' ){
						if( state&(1<<j) ){
							ans[i]='1';
						}else{
							ans[i]='0';
						}
						j++;
					}
				}
				break;
			}
		}
		reverse(ans.begin(),ans.end());
		printf("Case #%d: ",Te++);
		cout<<ans<<endl;
		//for(int i=1;i<G;i++) printf("%.8lf\n",ans[i]);
	}
}