#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

vector<pair<int,int> > a,b;

bool pcmp(pair<int,int> a,pair<int,int> b)
{
	if (a.first!=b.first) return a.first<b.first;
	else return a.second>b.second;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i,j,l,t,tmp,ans1,ans2,na,nb,ta,x;
	char s[1000];
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		scanf("%d",&ta);
		scanf("%d%d",&na,&nb);
		a.clear();b.clear();
		for (i=0;i<na;i++)
		{
			scanf("%s",s);
			x=((s[0]-'0')*10+s[1]-'0')*60+(s[3]-'0')*10+s[4]-'0';
			a.push_back(make_pair(x,-1));
			scanf("%s",s);
			x=((s[0]-'0')*10+s[1]-'0')*60+(s[3]-'0')*10+s[4]-'0';
			b.push_back(make_pair(x+ta,1));
		}
		for (i=0;i<nb;i++)
		{
			scanf("%s",s);
			x=((s[0]-'0')*10+s[1]-'0')*60+(s[3]-'0')*10+s[4]-'0';
			b.push_back(make_pair(x,-1));
			scanf("%s",s);
			x=((s[0]-'0')*10+s[1]-'0')*60+(s[3]-'0')*10+s[4]-'0';
			a.push_back(make_pair(x+ta,1));
		}
		sort(a.begin(),a.end(),pcmp);
		sort(b.begin(),b.end(),pcmp);
		ans1=0;ans2=0;
		tmp=0;
		for (i=0;i<a.size();i++)
		{
			tmp+=a[i].second;
			if (tmp<ans1) ans1=tmp;
		}
		tmp=0;
		for (i=0;i<b.size();i++)
		{
			tmp+=b[i].second;
			if (tmp<ans2) ans2=tmp;
		}
		ans1=-ans1;
		ans2=-ans2;
		printf("Case #%d: %d %d\n",l+1,ans1,ans2);
	}
	return 0;
}

