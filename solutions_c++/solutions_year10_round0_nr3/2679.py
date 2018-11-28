/*#include <stdio.h>
#include <iostream>
#include <memory.h>
#define N 1200

using namespace std;
int number;
int g[N];
int b1[N];
int b2[N];
int t1[N];
int t2[N];

void mycpy(int *a,int *b)
{
	int i;
	for(i=0;i<number;i++)
	{
		a[i]=b[i];
	}
}

bool mycmp(int *a,int *b)
{
	int i;
	for(i=0;i<number;i++)
	{
		if(a[i]!=b[i])
		{
			return 0;
		}
	}
	return 1;
}

void input()
{
	int i;
	memset(g,0,sizeof(g));
	memset(b1,0,sizeof(b1));
	memset(b2,0,sizeof(b2));
	memset(t1,0,sizeof(t1));
	memset(t2,0,sizeof(t2));
	for(i=0;i<number;i++)
	{
		scanf("%d",&g[i]);
		b1[i]=g[i];
	}
}

long long calc(int r,int k)
{
	long long money=0;
	int *p=g;
	int i;
	int tk,tk_pre;
	for(i=0;i<r;i++)
	{
		tk=k;
		int *bp=p;
		while(tk>0)
		{
			tk-=*p;
			p++;
			if(*p==0)
			{
				p=g;
			}
			if(bp==p)
			{
				break;
			}
		}
		if(tk)
		{				
			p--;
			tk+=*p;
		}
		money+=k-tk;
		int it=0;
		while(*p)
		{
			t2[it++]=*(p++);
		}
		p=g;
		while(it<number)
		{
			t2[it++]=*(p++);
		}
		if(*p==0)
		{
			p=g;
		}
		if(i==0)
		{
			mycpy(b2,t2);
		}
		if(mycmp(t1,b1)&&mycmp(t2,b2))
		{
		//	clog<<"----- Here is a loop -----"<<endl;
		//	clog<<"The T is "<<i<<endl;
			money-=k-tk;
		//	clog<<"Money in a loop : "<<money<<endl;
		//	clog<<"There are "<<r/i<<" loops."<<endl;
			money*=r/i;
			i=r-r%i-1;
			p=g;
		}
		mycpy(t1,t2);
		tk_pre=tk;
	}
	return money;
}

int main(int argc, char **argv)
{
	int t,index=1;;
	scanf("%d",&t);
	while(t--)
	{
		int r,k;
		scanf("%d%d%d",&r,&k,&number);
		input();
		printf("Case #%d: %lld\n",index++,calc(r,k));
	}
	return 0;
}
*/

#include <iostream>
#include <stdio.h>

using namespace std;

class RING
{
private:
	struct NODE
	{
		NODE()
		{
			num=0;
			next=NULL;
		}
		int num;
		NODE *next;
	};
	NODE head;
	NODE *tail;
	long long money;
public:
	RING()
	{
		tail=&head;
		money=0;
	}
	void Insert(int g)
	{
		NODE *p=new NODE;
		p->num=g;
		tail->next=p;
		tail=tail->next;
	}
	void Finish()
	{
		tail->next=head.next;
	}
	NODE *Run(int k,NODE *p)
	{
		NODE *now=p;
		bool first=1;
		int test=0;
		while(1)
		{
			test+=p->num;
			if((test>k)||(first==0&&now==p))
			{
				test-=p->num;
				money+=test;
				break;
			}
			else
			{
				p=p->next;
			}
			first=0;
		}
		return p;
	}
	long long GetMoney(int r,int k)
	{
		NODE *p=head.next;
		while(r--)
		{
			p=Run(k,p);
		}
		return money;
	}
};

int main()
{
	int t,index=1;
	scanf("%d",&t);
	while(t--)
	{
		RING rg;
		int i,r,k,n;
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)
		{
			int g;
			scanf("%d",&g);
			rg.Insert(g);
		}
		rg.Finish();
		printf("Case #%d: %lld\n",index++,rg.GetMoney(r,k));
	}
	return 0;
}