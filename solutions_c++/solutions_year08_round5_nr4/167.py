#include<stdio.h>
#include<algorithm>
#include<set>
#include<map>
#include<vector>

using namespace std;

typedef long long int64;

const int range = 100000000+10;

bool isprime[range];
int prime[range/5],cntprime;
int cnt[range/5];
pair<int,int> T[10];
map<pair<int,int>,int> Ans;
int U;

void getprime()
{
	cntprime=0;
	for(int i=2;i<range;i++)
	{
		if(!isprime[i])
		{
			prime[cntprime++]=i;
			if(i>30000) continue;
			for(int j=i*i;j<range;j+=i) isprime[j]=true;
		}
	}
}

void _add(int n)
{
	int t = 10007;
	while(t<=n)
	{
		U += n/t;
		if(n/t < 10007) break;
		t *= 10007;
	}
}

void _cut(int n)
{
	int t = 10007;
	while(t<=n)
	{
		U -= n/t;
		if(n/t < 10007) break;
		t *= 10007;
	}
}

void add(int n)
{
	for(int i=0;i<cntprime;i++)
	{
		int t = prime[i];
		while(t<=n)
		{
			cnt[i] += n/t;
			if(n/t<prime[i]) break;
			t *= prime[i];
		}
	}
}

void cut(int n)
{
	for(int i=0;i<cntprime;i++)
	{
		int t = prime[i];
		while(t<=n)
		{
			cnt[i] -= n/t;
			if(n/t<prime[i]) break;
			t *= prime[i];
		}
	}
}

int C(int m,int n)
{
	memset(cnt,0,sizeof(cnt)); U=0;
	_add(m); _cut(n); _cut(m-n);
	//if(U!=0) return 0;
	add(m); cut(n); cut(m-n);

	int ans = 1;
	for(int i=0;i<cntprime;i++)
	{
		for(int j=0;j<cnt[i];j++)
			ans = (ans * (prime[i] % 10007)) % 10007;
	}
	return ans;
}

int calc(int x,int y)
{
	if(Ans.find(make_pair(x,y))!=Ans.end()) return Ans[make_pair(x,y)];
	if((x+y)%3!=2) return 0;
	if(x<(x+y+1)/3 || y<(x+y+1)/3) return 0;
	return Ans[make_pair(x,y)]=C((x+y)/3,x-(x+y+1)/3);
}

vector<pair<int,int> > Path;
int W,H,R;

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	getprime();
	int ntest;
	scanf("%d",&ntest);
	for(int test=1;test<=ntest;test++)
	{
		//if(test>=20) break;
		fprintf(stderr,"%d\n",test);
		scanf("%d%d%d",&W,&H,&R);
		for(int i=0;i<R;i++) scanf("%d%d",&T[i].first,&T[i].second);
		sort(T,T+R);
		int ans = 0;
		for(int s=0;s<(1<<R);s++)
		{
			int value = 1;
			Path.clear();
			Path.push_back(make_pair(1,1));
			for(int i=0;i<R;i++)
				if(s&(1<<i)) 
					Path.push_back(T[i]);
			Path.push_back(make_pair(W,H));
			for(int i=0;i+1<Path.size();i++)
			{
				if(Path[i].second > Path[i+1].second) value = 0;
				else
				{
					value *= calc(Path[i+1].first-Path[i].first+1,Path[i+1].second-Path[i].second+1);
					value %= 10007;
				}
			}
			if(Path.size()%2==0)ans += value;
			else ans += (10007-value);
			ans %= 10007;
		}
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}
