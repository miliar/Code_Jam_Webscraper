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
#include <cassert>
#include <cstring>
#include <queue>
#define vvi vector<vector<int> > 
#define pii pair<int,int>
#define vpii vector<vector<pair<int,int> > > 
#define mp(a,b) make_pair(a,b)
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define sz size()
#define pb push_back
#define all(x) x.begin(),x.end()
using namespace std;
vector<vector<string> > ar;
char inp[200];
void trans()
{
	int len=strlen(inp);
	for(int i=0;i<len;i++){
		if(inp[i]=='/')inp[i]=' ';
	}
}
int main()
{
	int tc;
	scanf("%d",&tc);
	int caseno=1;
	while(tc--){
		int n,m;
		scanf("%d%d",&n,&m);
		ar.clear();
		for(int i=0;i<n;i++){
			vector<string> tmp;
			scanf("%s",inp);
			trans();
			string ginp=string(inp);
			stringstream is;
			is.str(ginp);
			string get;
			while(is>>get){
				tmp.pb(get);
			}
			ar.pb(tmp);
		}
		int ret=0;
		for(int i=0;i<m;i++){
			//best match
			vector<string> tmp;
			scanf("%s",inp);
			trans();
			string ginp=string(inp);
			stringstream is;
			is.str(ginp);
			string get;
			while(is>>get){
				tmp.pb(get);
			}
			int add=tmp.sz;
			for(int j=0;j<ar.sz;j++){
				int k;
				for(k=0;k<tmp.sz&&k<ar[j].sz;k++){
					if(tmp[k]!=ar[j][k])break;
				}
				if(add>tmp.sz-k)add=tmp.sz-k;
			//	add=(int)min(add,tmp.sz-k);
			}
			ret+=add;
			ar.pb(tmp);
		}
		printf("Case #%d: %d\n",caseno++,ret);
	}
	return 0;
}
