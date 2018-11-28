#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cassert>
#include <climits>
#define REP(i,n) for(int (i)=0, _n=(n); (i) < (_n); i++)
#define REPD(i,n) for(int (i)=(n-1); i >= 0; i--)
#define FOR(i,a,n) for(int (i)=(a),_n=(n); (i) <= (_n); (i)++)
#define FORD(i,a,n) for(int (i)=(a),_n=(n); (i) >= (_n); (i)--)
#define INF 1000000000
#define MAXN 120
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(cs,1,test){
		int arr[MAXN];
		vector<int> v[2];
		int idx[2]={};
		int dist[2];
		
		int n;
		scanf("%d",&n);
		REP(i,n){
			int a; char c[3];
			scanf("%s %d",c,&a);
			int id = c[0]=='O';
			arr[i]=id;
			v[id].push_back(a);	
		}	
		
		int ans=0;
		
		dist[0] = (v[0].size())?v[0][0]:INF;
		dist[1] = (v[1].size())?v[1][0]:INF;
		
		REP(i,n){
			int id = arr[i];
			int next = (id+1)%2;
			
			ans += dist[id];
			dist[next] = max(1,dist[next]-dist[id]);
			dist[id] = (v[id].size() == idx[id])?INF:v[id][idx[id]+1]-v[id][idx[id]];
			if(dist[id]<0)dist[id]=-dist[id];
			dist[id]++;
			idx[id]++;
		}
		printf("Case #%d: %d\n",cs,ans);
	}
	//system("pause");
    return 0;
}
