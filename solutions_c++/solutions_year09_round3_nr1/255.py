#include <iostream>
#include <string>
using namespace std;
#define tiao system("pause")

int t;
string s;
int base;
bool used[222];
unsigned long long ans(0);
int a[222];

int main(void)
{
	int i,j,k,ci,cici,cicici;
	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	cin >> t;
	for (cicici=1; cicici<=t; cicici++)
	{
		cin >> s;
		memset(used,0,sizeof(used));
		
		if (s.size() == 1)
		{
			cout << "Case #" << cicici << ": 1" << endl;
			continue;
		}
		
		int cnt = 0;
		for (i=0; i<s.size(); i++)
		{
			if (!used[s[i]])
			{
				cnt++;
				used[s[i]] = true;
			}
		}
		
		base = cnt;
		if (base == 1) base++;
		memset(a,-1,sizeof(a));
		a[s[0]] = 1;

		int now = 0;		
		for (i=1; i<=s.size(); i++)
		{
			if (a[s[i]] != -1) continue;
			if (now == 1) now++;
			a[s[i]] = now;
			now++;
		}
		
		
		ans = 0;
		for (i=0; i<s.size(); i++)
		{
			ans = ans * base + a[s[i]];
		}		
		
		cout << "Case #" << cicici << ": " << ans << endl;
	}
//	tiao;
	return 0;
}
