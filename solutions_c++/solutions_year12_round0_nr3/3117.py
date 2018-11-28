#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
#include<utility>

#define mm(a,b) memset(a,b,sizeof(a))
#define rep(i,a,b) for(i=a;i<b;++i)
#define repr(i,a,b) for(i=a;i>b;--i)
#define maxn 2000050

using namespace std;

int l,r,total;

bool used[maxn];

void get(deque<int> &n,int num)
{
	n.clear();
	while(num)
		n.push_front(num%10),num/=10;
}

void change(deque<int>&a)
{
a.push_front(a.back());
a.pop_back();
}

int get(deque<int>&a)
{
	int i,t(0);
	rep(i,0,a.size())
	t=t*10+a[i];
	return t;
}

void process(void)
{
	int num,i,j,k,t;
	deque<int> n,tmp;
	rep(num,l,r)
	{
		get(n,num);
		tmp=n;
		do
		{
			change(tmp);
			if(!tmp[0])
				continue;
			if(tmp==n)
				break;
			t=get(tmp);
			if(t>num && t<=r)
				++total;
		}
		while(true);
	}
	cout<<total<<endl;
}

void clear(void)
{
	mm(used,0);
	total=0;
}

int main(void)
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int i,j,T;
	for(i=1,cin>>T;i<=T;++i)
	{
		cin>>l>>r;
		printf("Case #%d: ",i);
		process();
		clear();
	}
	return 0;
}
