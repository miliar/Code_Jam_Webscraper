#include <stdio.h>
#include <stdlib.h>

int bbb = 31250;

class node
{
public:
	node *next;
	int val,count;
};

class list
{
public:
	node *first;
	void initialize()
	{
		first = NULL;
	}
	void add(int x,int y)
	{
		node *c = (node *)malloc(sizeof(node));
		c->next= first;
		first=c;
		c->val = x;
		c->count = y;
	}
	void del_all()
	{
		node *tmp2;
		node * tmp=first;
		while(tmp!=NULL)
		{
			tmp2 = tmp;
			tmp = tmp->next;
			free(tmp2);
		}
		first= NULL;
	}
};

class bucket
{
public:
	list l;
	int total_num;
	void initialize()
	{
		l.initialize();
		total_num=0;
	}

	void del_all()
	{
		l.del_all();
		total_num=0;
	}
};

bucket ttt[32000];
int A[500002];
int seq[500002];
int ans[500002];

int main()
{
	int i,j;
	node *tmp;
	__int64 X,Y,Z;
	int cas,asd;
	__int64 n,m;
	__int64 sum;
	
	int x,y;

	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		scanf("%I64d %I64d %I64d %I64d %I64d",&n,&m,&X,&Y,&Z);
		for(i=0;i<m;i++)
			scanf("%d",&A[i]);
		for(i=0;i<n;i++)
		{
			seq[i] = A[i % m];
			A[i%m] = (X * A[i % m] + Y * (i + 1) ) % Z;
		}
		for(i=0;i<32000;i++)
			ttt[i].initialize();
		for(i=0;i<n;i++)
		{
			ans[i]=1;
			x = seq[i] / bbb;
			for(j=0;j<x;j++)
				ans[i] = (ans[i] + ttt[j].total_num) % 1000000007;
			tmp = ttt[x].l.first;
			while(tmp!=NULL)
			{
				if(tmp->val < seq[i])
					ans[i] = (ans[i] + tmp->count) % 1000000007;
				tmp=tmp->next;
			}
			
			tmp = ttt[x].l.first;
			while(tmp!=NULL)
			{
				if(tmp->val == seq[i])
				{
					tmp->count = (tmp->count + ans[i]) % 1000000007;
					break;
				}
				tmp = tmp->next;
			}
			if(tmp==NULL)
				ttt[x].l.add(seq[i],ans[i]);
			ttt[x].total_num = (ttt[x].total_num + ans[i]) % 1000000007;
		}
		sum=0;
		for(i=0;i<n;i++)
			sum = (sum + ans[i]) % 1000000007;
		printf("Case #%d: %I64d\n",asd+1,sum);
	}
	return 0;
}
