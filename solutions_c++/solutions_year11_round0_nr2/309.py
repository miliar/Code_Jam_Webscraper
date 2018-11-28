#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <string.h>
#include <bitset>
#include <math.h>
#include <time.h>
#include <list>
#include <stack>

using namespace std;

//typedef long long LL;
typedef __int64 LL;
#define move(i) (1<<i)
#define take(a,b) (((a)>>(b))&1)
#define mp make_pair
#define pb push_back
#define VI vector<int>
#define MX vector<vector<int> >
#define PII pair<int,int>
#define SZ(X) ((int)(X.size()))
#define LEN(X) ((int)(X.length()))
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
//template<class T> inline T max(T a,T b){return a > b ? a : b;}
//template<class T> inline T min(T a,T b){return a < b ? a : b;}

// template by tracyzhu
int comb[30][30];
int opps[30][30];
int main(){
	int t,cas = 0,i,j,k;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		int c;
		memset(comb,0,sizeof(comb));
		memset(opps,0,sizeof(opps));
		scanf("%d",&c);
		for(i = 1;i <= c;i++){
			string str;
			cin>>str;
			comb[str[0] - 'A'][str[1] - 'A'] = str[2];
			comb[str[1] - 'A'][str[0] - 'A'] = str[2];
		}
		scanf("%d",&c);
		for(i = 1;i <= c;i++){
			string str;
			cin>>str;
			opps[str[0] - 'A'][str[1] - 'A'] = 1;
			opps[str[1] - 'A'][str[0] - 'A'] = 1;
		}
		int L;
		vector<char>beg;
		vector<char>temp;
		cin>>L;
		for(i = 1;i <= L;i++){
			char ch;
			cin>>ch;
			if(SZ(beg) > 0){
				if(comb[beg[SZ(beg) - 1] - 'A'][ch - 'A'] > 0)
					beg[SZ(beg) - 1] = comb[beg[SZ(beg) - 1] - 'A'][ch - 'A'];
				else{
					int f = 0;
					for(j = 0;j < SZ(beg);j++){
						if(opps[beg[j] - 'A'][ch - 'A'] == 1){f = 1;break;}
					}
					if(f == 1){
						beg.clear();
					}else beg.pb(ch);
				}
			}else{
				beg.pb(ch);
			}
		}
		printf("Case #%d: ",++cas);
		printf("[");
		for(i = 0;i < SZ(beg);i++){
			if(i != 0) printf(", ");
			printf("%c",beg[i]);
		}
		printf("]\n");
	}
	return 0;
}
