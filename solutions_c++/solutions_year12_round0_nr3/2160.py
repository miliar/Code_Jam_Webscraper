#include <stdio.h>
#include <set>
#include <string>
using namespace std;

int A,B;

struct bn
{
	char a[10];
    int len; 
}bigB;

bn decode(int n)
{
	bn ret;
	ret.len = 0;
	while(n)
	{
		ret.a[ret.len++] = n%10+'0';
		n /= 10;
	}
	ret.a[ret.len] = 0;
    return ret;
}

bn rey(bn cur)
{
    int i;
	char ch = cur.a[0];
	for(i=0;i<cur.len-1;i++)
		cur.a[i] = cur.a[i+1];
	cur.a[i] = ch;
	return cur;
}

int cmp(const bn&a,const bn&b)
{

	if(a.len!=b.len)
		return a.len-b.len;
	else
	{
         int i;
		 for(i=a.len-1;i>=0;i--)
			 if(a.a[i]!=b.a[i])
				 return a.a[i] - b.a[i];
	}
	return 0;
}

int calc(bn now)
{
	set<string> hash;
	bn t = rey(now);
	int ret = 0;
    for(int i=0;i<now.len-1;i++)
	{
	if( cmp(t,bigB)<=0 && cmp(now,t)<0)
	{
		if(hash.find(t.a)==hash.end())
		{
			ret++;
			hash.insert(t.a);
		}
	}
	t = rey(t);
	}
	return ret;
}

int solve()
{
    int i;
	int cnt = 0;
	bigB = decode(B);
	for(i=A;i<=B;i++)
	{
		bn now = decode(i);
		if(now.len==1)
			continue;
		cnt += calc(now);
	}
		return cnt;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.txt","w",stdout);
	int ct,caset = 1;
	scanf("%d",&ct);

	while(ct--)
	{
		printf("Case #%d: ",caset++);         
	    scanf("%d%d",&A,&B);
		printf("%d\n",solve());
	}
	return 0;
}