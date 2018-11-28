#include<iostream>
#include<fstream>
#include<string.h>
#include<vector>
#include<queue>
using namespace std;
const int L=20;
const int M=1000;
struct node
{
	node* child[26];
	bool isend;
	node()
	{
		for(int i=0;i<26;++i)
		{
			child[i]=NULL;
		}
		isend=false;
	}
};
node *TRoot;
char str[L];
char in[M];
int ncase,nask,len;
struct nod
{
	int s,e;
};
nod leng[L];
char searc[M];
int match;
//*****************************************************
inline void build(char * str)
{
	node* p=TRoot;
	int index=0;
	int m=0;
	while(str[index]!='\0')
	{
		m=str[index]-'a';
		if(p->child[m]==NULL)
			p->child[m]=new node;
		p=p->child[m];
		++index;
	}
	p->isend=true;
}
//*****************************************************
inline int search(char *str)
{
	node *p=TRoot;
	int index=0;
	int m=0;
	while(str[index]!='\0')
	{
		m=str[index]-'a';
		if(p->child[m]==NULL)
		{
			return index;
		}
		p=p->child[m];
		++index;
	}
	if(p->isend) return -1;
	else return index;
}
//*****************************************************
inline void solve()
{
	int l=strlen(in);
	int index=0;
	
	for(int i=0;i<l;++i)
	{
		if(in[i]=='(')
		{
			leng[index].s=i+1;
			continue;
		}
		else if(in[i]==')')
		{
			leng[index].e=i-1;
			++index;
			while(in[i+1]!='(')
			{
				leng[index].s=i+1;
				leng[index].e=i+1;
				++index;
				++i;
				if(i>=l)
					break;
			}
		}
		else if(i==0)
		{
			leng[index].s=i;
			leng[index++].e=i;
			while(in[i+1]!='(')
			{
				leng[index].s=i+1;
				leng[index].e=i+1;
				++index;
				++i;
				if(i>=l)
					break;
			}
		}
	}

}
//*****************************************************
void DFS(int deep)
{
	if(deep>=len)
	{
		searc[deep]='\0';
        if(search(searc)==-1)
			++match;
		return ;
	}
	bool flag=false;
	for(int i=leng[deep].s;i<=leng[deep].e;++i)
	{
		searc[deep]=in[i];
		if(i==leng[deep].s)
		{
			searc[deep+1]='\0';
			int c=search(searc);
			if(c>=(deep-1) || c==-1)
			{
				flag=true;
				DFS(deep+1);
			}
		}
		else if(flag)
		{
			DFS(deep+1);
		}
		else break;
	}
}
//*****************************************************
int main()
{
	ifstream fin("A-small-attempt8.in");
	ofstream fout("A-small-attempt8.out");
	//scanf("%d%d%d",&len,&ncase,&nask);
	fin>>len>>ncase>>nask;
	TRoot=new node();
	for(int i=0;i<ncase;++i)
	{
	//	scanf("%s",str);
		fin>>str;
		build(str);
	}
	for(int i=1;i<=nask;++i)
	{
	//	scanf("%s",in);
		fin>>in;
		match=0;
		solve();
		DFS(0);
		fout<<"Case #"<<i<<": "<<match<<endl;
	}
	return 0;
} 
