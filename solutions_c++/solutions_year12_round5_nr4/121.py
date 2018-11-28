#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<map>
#include<cstdlib>
#include<queue>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl
#define sqr(x) ((x)*(x))


map<char,int> a;
map<char,char> b;
char s[10010];
int tests,K,ans;
vector<string> v;

int main()
{
	freopen("d0.in","r",stdin);
	freopen("d0.out","w",stdout);
	b.clear();
	b['o'] = '0';
	b['i'] = '1';
	b['e'] = '3';
	b['a'] = '4';
	b['s'] = '5';
	b['t'] = '7';
	b['b'] = '8';
	b['g'] = '9';
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++)
	{
		scanf("%d %s",&K,s);
		a.clear();
		v.clear();
		ans = 0;
		for (int i=0;s[i]&&s[i+1];i++)
		{
			char p = s[i], q = s[i+1];
			v.push_back(string("")+p+q);
			if (b.find(p) != b.end())
			{
				v.push_back(string("")+b[p]+q);
			}
			if (b.find(q) != b.end())
			{
				v.push_back(string("")+p+b[q]);
			}
			if (b.find(p) != b.end() && b.find(q) != b.end())
			{
				v.push_back(string("")+b[p]+b[q]);
			}
		}
		sort(v.begin(),v.end());
		ans = 0;
		for (int i=0;i<v.size();i++)
		{
			//cout << "# " << v[i] << endl;
			if (i==0 || v[i]!=v[i-1])
			{
				ans++;
				a[v[i][0]]--;
				a[v[i][1]]++;
			}
		}
		
		int cnt = 0;
		for (char ch='a'; ch<='z'; ch++)
		{
			cnt += abs(a[ch]);
			if (b.find(ch) != b.end())
				cnt += abs(a[b[ch]]);
		}
		cnt/=2;
		//debug(ans);
		//debug(cnt);
		if (cnt>1)
			ans += cnt-1;
		printf("Case #%d: %d\n",test,ans+1);
	}
	
	return 0;
}
