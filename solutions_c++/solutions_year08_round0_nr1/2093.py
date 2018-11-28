#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long ll;

#define sz size()
#define pb push_back
#define MAX 0x3FFFFFFF
#define all(x) (x).begin(),(x).end()
#define For(i,n) for(int i=0, _n=(n);i<_n;++i)
#define For2(i,a,b) for(int i=(a), _n=(b);i<_n;++i)
#define Forit(it,x) for(typeof((x).begin()) it=(x).begin(), ed=(x).end();it!=ed;++it)

int n, m;
string a[128];
string b[1024];

string compute(int x)
{
	int last = x;
	map<string,int> mm;
	For2(i,x,m) if(!mm[b[i]]) {last = i; mm[b[i]] = 1;}
	For(i,n) if(!mm[a[i]]) return a[i];
	return b[last];
}

int main()
{
	int tn, ti = 0;
	FILE *in = fopen("A-large.in","r");
	FILE *out = fopen("output.txt","w");
	fscanf(in, "%d", &tn);
	while(tn--)
	{
		char p[128];
		fscanf(in, "%d ",&n);
		For(i,n) 
		{
			fgets(p, 128, in);
			a[i] = string(p);
		}
		fscanf(in, "%d ",&m);
		For(i,m) 
		{
			fgets(p, 128, in);
			b[i] = string(p);
		}
		string cur = compute(0);
		int ans = 0;
		For(i,m) if(cur == b[i]) {cur = compute(i); ans++;}
		fprintf(out, "Case #%d: %d\n", ++ti, ans);
	}
}
