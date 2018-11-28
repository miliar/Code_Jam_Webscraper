#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
char combine[256][256];
bool opposed[256][256];
void init()
{
	memset(combine,0,sizeof(combine));
	memset(opposed,0,sizeof(opposed));
	int c,d;
	scanf("%d",&c);
	for(int i=0;i<c;i++)
	{
		char str[1024];
		scanf("%s",str);
		combine[str[0]][str[1]]=str[2];
		combine[str[1]][str[0]]=str[2];
	}
	scanf("%d",&d);
	for(int i=0;i<d;i++)
	{
		char str[1024];
		scanf("%s",str);
		opposed[str[0]][str[1]]=true;
		opposed[str[1]][str[0]]=true;
	}
}
void solve()
{
	int n;
	scanf("%d",&n);
	char str[1024];
	scanf("%s",str);
	vector<char> ans;
	for(int i=0;i<n;i++)
	{
		if(!ans.empty()&&combine[ans.back()][str[i]])
		{
			char temp=combine[ans.back()][str[i]];
			ans.pop_back();
			ans.push_back(temp);
		}
		else
		{
			bool flag=true;
			for(vector<char>::iterator it=ans.begin();it!=ans.end();it++)
			{
				if(opposed[*it][str[i]])
				{
					ans.clear();
					flag=false;
					break;
				}
			}
			if(flag) ans.push_back(str[i]);
		}
	}
	putchar('[');
	bool flag=true;
	for(vector<char>::iterator it=ans.begin();it!=ans.end();it++)
	{
		if(flag)
		{
			flag=false;
		}
		else
		{
			printf(", ");
		}
		putchar(*it);
	}
	puts("]");
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		init();
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
