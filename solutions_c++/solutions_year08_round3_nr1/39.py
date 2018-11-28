#define _CRT_SECURE_NO_DEPRECATE 
#include <string> 
#include <vector> 
#include <map> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <algorithm> 
using namespace std; 

typedef vector<int> vi; 
typedef vector<string> vs; 
typedef pair<int,int> pii; 
typedef long long ll; 
#define fill(w,v) memset(w,v,sizeof(w)) 
#define FOR(i,f,n) for(int i=f; i<n; ++i) 
#define pb push_back 
#define mp make_pair 
#define sz(a) ((int)a.size()) 
#define all(a) a.begin(),a.end()
#define inf 1000000000 


int freq[1001];
pii a[1001];
int b[1001];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int Tasks;
	scanf("%d", &Tasks);
	FOR(task,0,Tasks)
	{
		int P,K,L;
		scanf("%d%d%d", &P, &K, &L);
		FOR(i,0,L)
		{
			scanf("%d", &freq[i]);
			a[i].first = -freq[i];
			a[i].second = i;
		}
		sort(a,a+L);
		fill(b,0);
		FOR(i,0,L)
		{
			b[a[i].second] = i/K + 1;
		}
		ll res=0;
		FOR(i,0,L)
		{
			res += (ll)(b[i])*freq[i];
		}
		printf("Case #%d: %lld\n", task+1, res);
	}
	return 0;
} 
