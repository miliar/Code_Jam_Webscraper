#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL unsigned long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 100000000

#define GI(x) scanf("%d", &x)

using namespace std;

char s[111];
bool gt(vector<int> v1, vector<int> v2) // v1 > v2 ?
{
	int i, j, k;
	for(i = 0; i < v1.size(); i++)
	{
		if(v1[i] > v2[i])
			return true;
		if(v1[i] < v2[i])
			return false;
	}
	return false;
}
void disp(VI v)
{
	int i, j, k;
	for(i = 0; i < SZ(v); i++)
	{
		cout<<v[i];
	}
}
void solve()
{
	vector<int> v;
	int i, j, k;
	int n = strlen(s);
	int mini = 100;
	for(i = 0; i < n; i++)
	{
		v.PB(s[i] - '0');
		if(s[i] == '0')
			continue;
		mini = min(mini, s[i] - '0');
	}
	VI t = v;
	next_permutation(ALL(t));
	if(gt(t, v))
	{
		disp(t);
		return;
	}
	sort(ALL(t));
	int pos = 0;
	while(pos < t.size() && t[pos] == 0)
	{
		pos++;
		continue;
	}
	if(pos < t.size())
	swap(t[pos], t[0]);
	t.insert(t.begin()+1, 0);
	disp(t);
}
int main()
{
	int tes;
	scanf("%d", &tes);
	getchar();
	int i, j, k;
	for(int t = 1; t <= tes; t++)
	{
		gets(s);
		printf("Case #%d: ", t);
		solve();
		cout<<endl;
	}
	return 0;
}
