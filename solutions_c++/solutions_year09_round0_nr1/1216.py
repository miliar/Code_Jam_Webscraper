#include <iostream>
using namespace std;

int L,D,N;
struct node
{
	node * jh[26];
};

node * root;

void insert(node * head,char * c)
{
	if (c[0]==0) return;
	int i=c[0]-'a';
	if (head->jh[i]==NULL)
	{
		head->jh[i]=new node;
		memset(head->jh[i]->jh,0,sizeof(head->jh[i]->jh));
	}
	insert(head->jh[i],c+1);
}

void init()
{
	freopen("A_large.in","r",stdin);
	freopen("ans2.txt","w",stdout);
	cin>>L>>D>>N;
	root=new node;
	memset(root->jh,0,sizeof(root->jh));
	int i;
	char a[10000];
	for (i=1;i<=D;i++)
	{
		cin>>a;
		insert(root,a);
	}
}

int tongj(node * head,char * a)
{
	if (a[0]==0) return 1;
	int i,j,t;
	t=0;
	if (a[0]=='(')
	{
		i=0;
		while (a[i]!=')') i++;
		for (j=1;j<i;j++)
		{
			if (head->jh[a[j]-'a']!=NULL)
				t+=tongj(head->jh[a[j]-'a'],a+i+1);
		}
		return t;
	}
	else if (head->jh[a[0]-'a']!=NULL) 
		return tongj(head->jh[a[0]-'a'],a+1);
	return 0;
}

void make()
{
	int i;
	char a[10000];
	for (i=1;i<=N;i++)
	{
		cin>>a;
		cout<<"Case #"<<i<<": "<<tongj(root,a)<<endl; 
	}
}

void del(node * head)
{
	int i;
	for (i=0;i<26;i++)
	{
		if (head->jh[i]!=NULL)
		{
			del(head->jh[i]);
		}
	}
	delete head;
}

int main()
{

	init();
	make();
	del(root);
	return 0;
}