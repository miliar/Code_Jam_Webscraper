#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;
typedef long long ll;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int tc=1; tc<=t; tc++){
		ll c=1;
		ll ans=0;
		map<char,int> d;
		char s[100];
		int p;
		scanf("%s\n",s);
		ll cnt = 0;
		p=1;
		int len = strlen(s);
		for(int i=0; i<len; i++){
			if(d.count(s[i])==0){
				if(p==1){
					d[s[i]]=p;
					p=0;
				}
				else if(p==0){
					d[s[i]]=p;
					p=2;
				}
				else{
					d[s[i]]=p;
					p++;
				}
				cnt++;
			}
		}
		cnt = max(cnt,2ll);
		strrev(s);
		for(int i=0; i<len; i++){
			ans += c*(ll)d[s[i]];
			c *= (ll)cnt;
		}
		printf("Case #%d: %lld\n",tc,ans);
	}
	return 0;
}