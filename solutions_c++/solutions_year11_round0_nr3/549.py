#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <algorithm>
#include <memory.h>

using namespace std;

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,k,n) for(int i=(k); i<=(n); i++)
#define DFOR(i,k,n) for(int i=(k); i>=(n); i--)
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a, 0, sizeof(a))

#define LL long long
#define VI  vector<int>
#define PAR pair<int ,int>
#define o_O 1000000000 
void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}

int n;
int nums[1024];

void sol()
{	
	FOR(a,0,25)
	{
		int ones=0;
		FOR(b,1,n) ones += ((nums[b]>>a)&1);
		if (ones&1)
		{
			cout << "NO";
			return;
		}
	}

	sort(nums+1, nums+n+1);
	int sum=0;
	FOR(a,2,n) sum+=nums[a];
	cout << sum;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	FOR(t,1,T)
	{
		cin >> n;
		FOR(a,1,n) RE("%d", &nums[a]);
	
		cout << "Case #" << t << ": ";
		sol();
		cout << "\n";
	}
	return 0;
}