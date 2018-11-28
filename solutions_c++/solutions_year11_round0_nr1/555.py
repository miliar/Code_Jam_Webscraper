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
char S[128];
int pos[128];

void sol()
{	
	int O_target, B_target;
	S[n+1]='O'; S[n+2]='B';
	pos[n+1]=1; pos[n+2]=1;
	FOR(a,1,n+2) if (S[a]=='O') { O_target = pos[a]; break; }
	FOR(a,1,n+2) if (S[a]=='B') { B_target = pos[a]; break; }

	int ans=0;
	int O_pos=1, B_pos=1, p=1;
	while(1)
	{
		if (p>n) break;
		ans++;

		bool press=false;

		if (O_pos==pos[p] && S[p]=='O')
		{
			p++;
			FOR(a,p,n+2) if (S[a]=='O') { O_target = pos[a]; break; }
			press=true;
		}
		else if (O_pos > O_target) O_pos--;
		else if (O_pos < O_target) O_pos++;

		if (B_pos==pos[p] && S[p]=='B' && !press)
		{
			p++;
			FOR(a,p,n+2) if (S[a]=='B') { B_target = pos[a]; break; }
		}
		else if (B_pos > B_target) B_pos--;
		else if (B_pos < B_target) B_pos++;
	}

	cout << ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	FOR(a,1,T)
	{
		RE("%d", &n);
		FOR(b,1,n)
		{
			char ch[5];
			RE("%s%d", ch, &pos[b]);
			S[b]=ch[0];
		}
		cout << "Case #" << a << ": ";
		sol();
		cout << "\n";
	}
	return 0;
}