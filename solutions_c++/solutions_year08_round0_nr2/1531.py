#include <cstdio>
#include <queue>

using namespace std;

struct train
{
	int begin,end,pb,pe;
};

struct waiting
{
	int begin;
};

bool operator<(const train &x,const train &y)
{
	if(x.begin>y.begin) return 1;
	return 0;
}

bool operator<(const waiting &x,const waiting &y)
{
	if(x.begin>y.begin) return 1;
	return 0;
}

int testnum;
int ld,rd;
int tw;

priority_queue <train> q;
priority_queue <waiting> w[3];

void solve(int numcase)
{
	int nt[3]={0};
	train t;
	while(q.empty()==0)
	{
		t=q.top(); 
		if(w[t.pb].empty())
		{
			nt[t.pb]++;
			waiting newwait;
			newwait.begin=t.end+tw;
			w[t.pe].push(newwait);
			q.pop();
			continue;
		}
		if(w[t.pb].top().begin<=t.begin)
		{
			nt[t.pb]--;
			w[t.pb].pop();
		}
		nt[t.pb]++;
		waiting newwait;
		newwait.begin=t.end+tw;
		w[t.pe].push(newwait);
		q.pop();
	}
	printf("Case #%d: %d %d\n",numcase,nt[1],nt[2]);
}

void read(int numcase)
{
	scanf("%d",&tw);
	int xx,xy,xz,xt;
	while(w[1].empty()==0) w[1].pop();
	while(w[2].empty()==0) w[2].pop();
	while(q.empty()==0) q.pop();
	scanf("%d %d",&ld,&rd);
	for(int i=0;i<ld;i++)
	{
		scanf("%d:%d %d:%d",&xx,&xy,&xz,&xt);
		train newtrain;
		newtrain.begin=xx*60+xy;
		newtrain.end=xz*60+xt;
		newtrain.pb=1;
		newtrain.pe=2;
		q.push(newtrain);
	}
	for(int i=0;i<rd;i++)
	{
		scanf("%d:%d %d:%d",&xx,&xy,&xz,&xt);
		train newtrain;
		newtrain.begin=xx*60+xy;
		newtrain.end=xz*60+xt;
		newtrain.pb=2;
		newtrain.pe=1;
		q.push(newtrain);
	}
	solve(numcase);
}

int main()
{
	scanf("%d",&testnum);
	for(int i=1;i<=testnum;i++) read(i);
	return 0;
}
