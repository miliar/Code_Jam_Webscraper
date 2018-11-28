#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
using namespace std;

void init();
void solve();
void print();
inline int getInt(char);
int n;
string st,ans;
bool opt[27][27];
int comb[27][27];

int main()
{
	freopen("Magicka.in","r",stdin);
	freopen("Magicka.out","w",stdout);
	
	int tt;
	scanf("%d", &tt);
	for(int i=0; i<tt; i++)
	{
		init();
		solve();
		printf("Case #%d: ", i+1);
		print();
	}
	
	return 0;	
}

int getInt(char ch)
{
	return ch-'A'+1;
}

void init()
{
	memset(comb,0,sizeof(comb));
	memset(opt,0,sizeof(opt));
	cin >>n;
	for(int i=0; i<n; i++)
	{
		string ss;
		cin >>ss;
		comb[getInt(ss[0])][getInt(ss[1])]=getInt(ss[2]);
		comb[getInt(ss[1])][getInt(ss[0])]=getInt(ss[2]);
	}
	cin >>n;
	for(int i=0; i<n; i++)
	{
		string ss;
		cin >>ss;
		opt[getInt(ss[0])][getInt(ss[1])]=1;
		opt[getInt(ss[1])][getInt(ss[0])]=1;
	}
	cin >>n;
	cin >>st;
}

bool check(int x)
{
	for(int i=0; i<ans.length(); i++)
		if(ans[i]==(char)(x+'A'-1)) return 1;
	return 0;
}

void solve()
{
	ans="";
	for(int i=0;i<n;i++)
	{
		if(ans.length()>0 && comb[getInt(ans[ans.length()-1])][getInt(st[i])]!=0)
		{
			char ch=ans[ans.length()-1];
			ans.erase(ans.length()-1,1);
			ans=ans+(char)(comb[getInt(ch)][getInt(st[i])]+'A'-1);
			continue;
		}
		bool flag=0;
		for(int j=1; j<=26; j++)
			if(check(j) && opt[j][getInt(st[i])])
			{
				flag=1; ans="";
			}
		if(flag) continue;
		ans=ans+st[i];
	}
}

void print()
{
	if(ans.length()==0)
	{
		printf("[]\n");
		return;
	}
	printf("[%c", ans[0]);
	for(int i=1; i<ans.length(); i++)
		printf(", %c",ans[i]);
	printf("]\n");
}
