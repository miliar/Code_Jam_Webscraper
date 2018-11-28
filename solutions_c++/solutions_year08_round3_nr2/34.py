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
int d[] = {2,3,5,7};
bool isugly(ll a)
{
	FOR(i,0,4)
		if (a%d[i] == 0) return true;
	return false;
}

int D=2*3*5*7;
int L;
char s[50];
ll mem[50][250];
ll rec(int p, int v)
{
	ll &r = mem[p][v];
	if (r!=-1) return r;
	r = 0;
	if (p == 0)
	{
		r = rec(1, (s[0]-'0')%D);
		int num=(s[0]-'0')%D;
		FOR(i,1,L)
		{
			num = (num*10 + s[i]-'0')%D;
			r += rec(i+1, num);
		}
		return r;
	}
	else if (p == L)
	{
		//printf("%lld\n", v);
		return r = (isugly(v)?1:0);
	}
	else
	{
		r += rec(p+1, (v+s[p]-'0')%D);
		r += rec(p+1, (-v+s[p]-'0'+D)%D);
		int num = (s[p]-'0')%D;
		FOR(i,p+1,L)
		{
			num = (num*10 + s[i]-'0')%D;
			r += rec(i+1, (v+num)%D);
			r += rec(i+1, (-v+num+D)%D);
		}
		return r;	
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int Tasks;
	scanf("%d\n", &Tasks);
	FOR(task,0,Tasks)
	{
		scanf("%s\n", s);
		L=strlen(s);
		fill(mem,-1);
		ll res=rec(0, 0);
		printf("Case #%d: %lld\n", task+1, res);
	}
	return 0;
} 
