#include<fstream>
#include<iostream>
using namespace std;
const int M=4000;
struct node
{
	int l,r;
	long long sum;
	node():l(0),r(0),sum(0){}
};
node tree[M];
long long data[M];
int ncase,R,K,N;
int ind=0;
ifstream fin("C-large.in");
ofstream fout("C-large.out");
struct nod
{
	int time;
	long long s;
};
nod recode[M];
//*****************************************************
void Build(int root,int start,int end)
{
	tree[root].l=start;
	tree[root].r=end;
	if(start==end) tree[root].sum=data[start];
	else if(start<end)
	{
		int mid=(start+end)/2;
		Build(2*root+1,start,mid);
		Build(2*root+2,mid+1,end);
		tree[root].sum=tree[2*root+1].sum+tree[2*root+2].sum;
	}
}
//**********************************************************
void ask(int root,int start,int end,long long &sum,int &re)
{
	if(tree[root].l>=start && tree[root].r<=end)
	{
		if(sum>=tree[root].sum)
		{
			sum-=tree[root].sum;
			if(tree[root].r>re)
				re=tree[root].r;
			return;
		}
		if(tree[root].l==tree[root].r)  return;
		long long t=tree[2*root+1].sum;
		if(sum>=t)
		{
			sum-=t;
			re=tree[2*root+1].r;
			ask(2*root+2,start,end,sum,re);
		}
		else ask(2*root+1,start,end,sum,re);
	}
	else
	{
		if(tree[root].l==tree[root].r) return;
		int mid=(tree[root].l+tree[root].r)/2;
		if(end<=mid)
		{
			ask(2*root+1,start,end,sum,re);
		}
		else if(start>mid)
		{
			ask(2*root+2,start,end,sum,re);
		}
		else if(start<=mid && end>mid)
		{
			ask(2*root+1,start,end,sum,re);
			if(re==tree[2*root+1].r)
				ask(2*root+2,start,end,sum,re);
		}
	}
}
//****************************************************
int main()
{
	fin>>ncase;
	int count=0;
	while(ncase--)
	{
		fin>>R>>K>>N;
		memset(tree,0,sizeof(tree));
		for(int i=0;i<M;++i)
		{
			recode[i].time=-1;
			recode[i].s=0;
		}
		for(int i=0;i<N;++i)
			fin>>data[i];
		Build(0,0,N-1);
		long long sum=0;
		int re=-1;
		long long ans=0;
		int start=0,end=N-1;
		int flag=-1,log=-1;
		long long recly=0;
		for(int i=0;i<R;++i)
		{
			sum=K;
			if(sum>tree[0].sum) 
			{
				ans+=tree[0].sum;
				continue;
			}
			if(re==N-1)
			{
				re=-1;
			}
			int lre=re;
			start=re;
			ask(0,start+1,N-1,sum,re);
			if(sum>0 && re==N-1 && sum>=data[0])
			{
				re=-1;
				ask(0,0,lre,sum,re);
			}
			ans+=(K-sum);
			if(recode[re].time!=-1)
			{
				flag=i;
				log=re;
				recly=ans-recode[re].s;
				break;
			}
			else 
			{
				recode[re].time=i;
				recode[re].s=ans;
			}
		}
		if(flag!=-1)
		{
			int t=flag-recode[log].time;
			int x=R-recode[log].time-1;
			int y=x%t;
			//y=(y+t-1)%t;
			int z=x/t;
			ans+=recly*(z-1);
			for(int i=0;i<N;++i)
			{
				if(recode[i].time==y+recode[log].time)
				{
					ans+=recode[i].s-recode[log].s;
					break;
				}
			}
		}
		fout<<"Case #"<<++count<<": "<<ans<<endl;
	}
	return 0;
}