#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <cctype>
#include <assert.h>
#include <list>
#include <ext/hash_set>
#include <ext/hash_map>

using namespace __gnu_cxx;
using namespace std;

#define MP(a,b) make_pair(a,b)
#define i64 long long
#define pb push_back
#define For(i,a,b) for(typeof(a) i=(a);i<(b);i++)
#define Rev(i,a,b) for(typeof(a) i=(a);i>=(b);i--)
#define FOREACH(V,it) for(typeof(V.begin()) it=V.begin();it!=V.end();it++)
#define CLR(a,x) memset(a,x,sizeof(a))
#define ALL(x) x.begin(),x.end()

/**********************************************************************************/
const int maxn=50;
char buf[5000][maxn],s[maxn*26];
set<char> temp[5000];
int n,k,d;
int main(){
	scanf("%d%d%d",&n,&d,&k);
	For(i,0,d)
		scanf("%s",buf+i);
	For(i,0,k){
		scanf("%s",s);
		int cur=0;
		For(j,0,n){
			set<char> S;
			if (s[cur]=='('){
				++cur;
				while (s[cur]!=')') S.insert(s[cur++]);
			}
			else S.insert(s[cur]);
			temp[j]=S;
			cur++;
		}
		//FOREACH(temp[0],it) cout << *it << ' ' ; cout << endl;
		int ret=0;
		For(j,0,d){
			ret++;
			For(t,0,n){
				if (temp[t].find(buf[j][t])==temp[t].end()){
					ret--;
					break;
				}
			}
		}	
		printf("Case #%d: %d\n",i+1,ret);
	}
	return 0;
}
