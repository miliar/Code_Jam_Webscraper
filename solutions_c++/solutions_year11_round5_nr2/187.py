#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
bool check(vector<int> &cards,int c)
{
	vector<bool> used(cards.size());
	vector<int> tail;
	int n=cards.size();
	for(int i=0;i<n;i++)
	{
		if(used[i]) continue;
		vector<int> found;
		for(int j=i,k=cards[i];j<n&&k<cards[i]+c;k++)
		{
			bool flag=false;
			for(;j<n;j++)
			{
				if(used[j]) continue;
				if(cards[j]>k)
				{
					break;
				}
				if(cards[j]==k)
				{
					found.push_back(j);
					flag=true;
					break;
				}
			}
			if(!flag) break;
		}
		if((int)found.size()==c)
		{
			for(int j=0;j<c;j++) used[found[j]]=true;
			tail.push_back(cards[i]+c-1);
		}
	}
	for(int i=0;i<n;i++)
	{
		if(used[i]) continue;
		bool flag=true;
		for(int j=0;j<(int)tail.size();j++)
		{
			if(cards[i]==tail[j]+1)
			{
				tail[j]++;
				used[i]=true;
				flag=false;
				break;
			}
		}
		if(flag) return false;
	}
	return true;
}
int solve()
{
	int n;
	scanf("%d",&n);
	if(n==0) return 0;
	vector<int> cards(n);
	for(int i=0;i<n;i++)
	{
		scanf("%d",&cards[i]);
	}
	sort(cards.begin(),cards.end());
	int a=1,b=n;
	while(a<=b)
	{
		int c=(a+b)/2;
		if(check(cards,c)) a=c+1; else b=c-1;
	}
	return b;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int cs=1;cs<=t;cs++)
	{
		printf("Case #%d: %d\n",cs,solve());
	}
	return 0;
}
