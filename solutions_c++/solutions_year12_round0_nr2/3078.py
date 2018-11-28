#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
#include<utility>

#define mm(a,b) memset(a,b,sizeof(a))
#define rep(i,a,b) for(i=a;i<b;++i)
#define repr(i,a,b) for(i=a;i>b;--i)
#define maxn 256

using namespace std;

char t[256];

int n,s,p,total;


void process(void)
{
	cin>>n>>s>>p;
	int i,x,t,a,b,c;
	rep(i,0,n)
	{
		cin>>x;
		t=x%3;
		x/=3;
		if(x>=p)
		{
			++total;
			continue;
		}
		if(!t)
		{
			a=x-1;
			b=x;
			c=x+1;
			if(a<0 || !s)
				continue;
			if(c>=p)
					--s,++total;
			continue;
		}
		if(t==1)
		{
			a=b=x;
			c=x+1;
			if(c>=p)
				++total;
			continue;
		}
		if(t==2)
		{
			if(x+1>=p)
				{
					++total;
					continue;
				}
			if(!s)
				continue;
			if(x+2>=p)
				++total,--s;
			continue;
		}
		
	}
	cout<<total<<endl;
}

void clear(void)
{
	n=s=p=total=0;
}

int main(void)
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i,T;
	for(i=1,cin>>T;i<=T;++i)
	{
		printf("Case #%d: ",i);
		process();
		clear();
	}
	return 0;
}
