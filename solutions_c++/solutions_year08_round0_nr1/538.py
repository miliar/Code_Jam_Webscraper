#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<iterator>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<deque>
#include<stack>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<string>
#include<cmath>
#include<ctime>
using namespace std;
typedef vector<int> VI; 
typedef vector<VI> VVI; 
typedef pair<int,int> II; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define debug 0
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,b) FOR(i,0,b)
#define pos(a) ((int)(a)>=0?(a):-(a))
#define INF 10000000
typedef long long LL;
/* Greedy .... Farthest is best */
int cnt;
map<string,int> m;
char search_engine[101][101],temp[1001];
int main()
{
	int t,cas=0;
	cin>>t;
	while(t--){
		cnt=0;m.clear();
		int N;scanf("%d\n",&N);
		int visitedCnt=0,ans=0;
		REP(i,N){
			gets(search_engine[i]);
			string s(search_engine[i]);
			m[s]=cnt++;
		}
		bool visited[N+1];
		memset(visited,0,sizeof(visited));
		int q;scanf("%d\n",&q);
		REP(i,q){
			gets(temp);
			string s(temp);
			if(m.find(temp)!=m.end()){
				int ind=m[temp];
				if(visitedCnt==N-1 && !visited[ind]){
					ans++;
					memset(visited,0,sizeof(visited));
					visited[ind]=1;
					visitedCnt=1;
				}
				else {
					if(!visited[ind])visitedCnt++;
					visited[ind]=1;
				}
			}
		}
		cas++;
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
	
