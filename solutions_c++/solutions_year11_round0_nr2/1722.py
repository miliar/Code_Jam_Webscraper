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
#define vc vector<char>
#define pb push_back
#define all(x) x.begin(),x.end()
using namespace std;
int C[256][256];
bool O[256][256];
char inp[250];
vc outa;
int main()
{
	int tc;
	scanf("%d",&tc);
	int caseno=1;
	while(tc--){
		memset(O,0,sizeof(O));
		memset(C,-1,sizeof(C));
		outa.clear();
		int c;
		scanf("%d",&c);
		for(int i=0;i<c;i++){
			scanf("%s",inp);
			C[inp[0]][inp[1]]=inp[2];
			C[inp[1]][inp[0]]=inp[2];
		}
		scanf("%d",&c);
		for(int i=0;i<c;i++){
			scanf("%s",inp);
			O[inp[0]][inp[1]]=true;
			O[inp[1]][inp[0]]=true;
		}
		scanf("%d",&c);
		scanf("%s",inp);
		for(int i=0;i<c;i++){
			bool perf = false;
			if(outa.sz>0 && C[outa[outa.sz-1]][inp[i]]!=-1){
				char take = C[outa[outa.sz-1]][inp[i]];
				outa.pop_back();
				outa.push_back(take);
				perf=true;
			}
			else if(outa.sz>0){
				//see if opposed to ? 
				int t=0;
				for(;t<outa.sz;t++){
					if(O[outa[t]][inp[i]]) break;
				}
				if(t<outa.sz){
					outa.clear();
					perf=true;
				}
			}
			if(!perf){
				outa.pb(inp[i]);
			}
		}
		printf("Case #%d: [",caseno++);
		for(int t=0;t<outa.sz;t++){
			if(t==outa.sz-1) printf("%c",outa[t]);
			else printf("%c, ",outa[t]);
		}
		puts("]");
	}
	return 0;
}