#include <stdio.h>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <string.h>
#include <queue>
#include <algorithm>
#include <math.h>
#include <sstream>
using namespace std;
typedef pair<int, int> pi;
typedef long long int li;
typedef vector<int> vi;
void solve();
#define mp make_pair
#define pb push_back

int main(){
#ifdef DEBUG
    freopen("input", "r", stdin);
    freopen("output","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;++i){
		printf("Case #%d: [",i);
		solve();
	}
    return 0;
}

void solve(){
	char base[]={'Q','W','E','R','A','S','D','F'};
	int cnt[30];
	bool is_opposite[30][30];
	vector<char> res;
	char sum[30][30];
	memset(cnt,0,sizeof(cnt));
	memset(is_opposite,0,sizeof(is_opposite));
	memset(sum,0,sizeof(sum));
	
	int c;
	scanf("%d",&c);
	for(int i=0;i<c;++i){
		char x,y,z;
		scanf(" %c%c%c",&x,&y,&z);
		sum[x-'A'][y-'A']=z;
		sum[y-'A'][x-'A']=z;
	}
	int d;
	scanf("%d",&d);
	for(int i=0;i<d;++i){
		char x,y;
		scanf(" %c%c",&x,&y);
		is_opposite[x-'A'][y-'A']=true;
		is_opposite[y-'A'][x-'A']=true;
	}
	
	int n;
	char s[111];
	scanf("%d%s",&n,s);
	for(int i=0;i<n;++i){
		if(res.empty()){
			res.pb(s[i]);
			cnt[s[i]-'A']=1;
		}
		else if(sum[res.back()-'A'][s[i]-'A']){
			--cnt[res.back()-'A'];
			char q=sum[res.back()-'A'][s[i]-'A'];
			res.pop_back();
			res.pb(q);
		}
		else{
			bool f=true;
			for(int j=0;j<8;++j){
				if(cnt[base[j]-'A'] && is_opposite[base[j]-'A'][s[i]-'A']){
					res.clear();
					for(int k=0;k<8;++k){
						cnt[base[k]-'A']=0;
					}
					f=false;
					break;
				}
			}
			if(f){
				res.pb(s[i]);
				++cnt[s[i]-'A'];
			}
		}
	}
	for(int i=0;i<res.size();++i){
		if(i)
			printf(", ");
		printf("%c",res[i]);
	}
	printf("]\n");
}