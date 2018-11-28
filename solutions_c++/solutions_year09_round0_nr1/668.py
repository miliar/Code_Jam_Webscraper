#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <string>
#include <map>

using namespace std;

const int LSZ=17;
const int SZ=LSZ*26;
int L, D, N;
int r;

struct link
{
	int v;
	link* next;
	link()
	{
		next=NULL;
	}
	link(int vv)
	{
		v=vv;
		next=NULL;
	}
};
link* c[LSZ];

struct node
{
	node* t[26];
	node()
	{
		memset(t, 0, sizeof(t));
	}
};
node* rt;

void in(char* s)
{
	node* p=rt;
	for(int i=0; s[i]!='\0'; i++)
	{
		int k=s[i]-'a';
		if(p->t[k]==NULL)
		{
			p->t[k]=new node;
		}
		p=p->t[k];
	}
}

void dfs(node* p, int i)
{
	if(i==L) 
	{
		r++; 
		return;
	}
	for(link* q=c[i]->next; q!=NULL; q=q->next)
	{
		if(p->t[q->v]!=NULL)
		{
			dfs(p->t[q->v], i+1);
		}
	}
}

void deal(char *s)
{
	for(int i=0; i<L; i++)
	{
		c[i]=new link;
	}
	bool same=0;
	int cnt=0;
	for(int i=0; s[i]!='\0'; i++)
	{
		if(s[i]=='(')
		{
			same=1;
		}
		else if(s[i]==')')
		{
			same=0;
			cnt++;
		}
		else
		{
			link* tmp=new link(s[i]-'a');
			tmp->next=c[cnt]->next;
			c[cnt]->next=tmp;
			if(!same) cnt++;
		}
	}
}

void remove()
{
	for(int i=0; i<L; i++)
	{
		for(link* p=c[i]; p!=NULL; )
		{
			link* q=p;
			p=p->next;
			delete q;
		}
	}
}
		
void init()
{
	rt=new node;
}


int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
	scanf("%d%d%d", &L, &D, &N);
	init();
	for(int i=0; i<D; i++)
	{
		char s[LSZ];
		scanf("%s", s);
		in(s);
	}
	for(int i=1; i<=N; i++)
	{
		char s[SZ];
		scanf("%s", s);
		deal(s);
		r=0;
		dfs(rt, 0);
		printf("Case #%d: %d\n", i, r);
		remove();
	}
    return 0;
}

