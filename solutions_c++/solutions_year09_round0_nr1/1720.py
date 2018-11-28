// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
/*
#include <iostream>
#include <string>
using namespace std;

int L,N,D,cnt;
string a[30];
string str;
int hash[30],hh[30]; 

int find(string str)
{
	for (int i = 0; i < D; ++ i)
		if(str == a[i])
			return 1;
	return 0;
}

int main()
{
	freopen("A.in","r",stdin);
	//freopen("A-largeh.in","r",stdin);
	//freopen("A.out","w",stdout);
	int i;
	scanf("%d %d %d",&L,&D,&N);
	{
		for (i = 0; i < D; ++ i)
			cin >> a[i];
		for (i = 1; i <= N; ++ i)
		{
			cin >> str;
			cnt = 0;
			memset(hash,0,sizeof(hash));
			string b[30];
			//for (int l = 0; l < 30; ++ l)
			//	b[i].clear();
			int mark = 0;
			for (int j = 0; j < str.length(); ++ j)
			{
				int k;
				if(str[j] == '(')
				{
					for (k = j + 1; str[k] != ')'; ++ k)
						b[mark] += str[k];
					hash[mark] = k - j - 1;
					j = k;
				}
				else 
				{
					b[mark] = str[j];
					hash[mark] = 1;
				}
				mark ++;
			}
			memset(hh,0,sizeof(hh));
			string ch;
			while ((hh[0] + 1) <= hash[0])
			{	
				int l;
				ch = "";
				for (l = 0; l < L; ++ l)
				{
					ch += b[l][hh[l]];
				}			
				if(find(ch))
					cnt ++;
				hh[l - 1] ++;
				for (int ll = L - 1; ll >= 0; ll --)
				{
					if((hh[ll] + 1) > hash[ll])
					{
						if (ll > 0)
							hh[ll] = 0;
						if (ll > 0)
							hh[ll - 1] ++;
					}
				}
			}
			printf ("Case #%d: %d\n",i,cnt);
		}
	}
	return 0;
}



*/

#include<iostream>
using namespace std;

typedef struct node
{
	int flag;
	node *next[27];
	void init(){memset(next,0,sizeof(next));flag=0;}
}node;

char ch[5010];
char hash[15000];
char mapx[501][27];
int L,D,K;
int total=0;

int del(node *T)
{
	int i;
	if(T==NULL)
		return 0;
	for(i=0;i<27;i++)
	{
		if(T->next[i]!=NULL)
		{
			del(T->next[i]);
		}
	}
	delete T;
	return 0;
}

int predeal(int len)
{
	int i,xk=0;
	for(i=0;i<len;i++)
	{
		if(hash[i]=='(')
		{
			int xxk=0;
			for(i=i+1;i<len;i++)
			{
				if(hash[i]==')')
				{
					mapx[xk][xxk]='\0';
					xk++;
					break;
				}
				mapx[xk][xxk++]=hash[i];
			}
		}
		else
		{
			mapx[xk][0]=hash[i];
			mapx[xk][1]='\0';
			xk++;
		}
	}
	return xk;
}


int deal(int now,node *T)
{
	int i;
	if(now==L)
	{
		total++;
		return 1;
	}
	for(i=0;mapx[now][i]!='\0';i++)
	{
		if(T->next[mapx[now][i]-'a'+1]==NULL)
			continue;
		deal(now+1,T->next[mapx[now][i]-'a'+1]);
	}
	return 0;
}

int main()
{
	int i,j;
	node *T,*p,*q;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	while(scanf("%d %d %d",&L,&D,&K)!=EOF)
	{
		getchar();
		//T=(node*)malloc(sizeof(node));
		T = new node();
		T->init();
		for(i=0;i<D;i++)
		{
			gets(ch);
			p=T;
			for(j=0;j<L;j++)
			{
				if(p->next[ch[j]-'a'+1]==NULL)
				{
					//q=(node*)malloc(sizeof(node));
					q = new node();
					q->init();
					p->next[ch[j]-'a'+1]=q;
					p=q;
				}
				else
					p=p->next[ch[j]-'a'+1];
			}
		}
		int len,pre;
		for(i=1;i<=K;i++)
		{
			gets(hash);
			len=strlen(hash);
			pre=predeal(len);
			if(pre!=L)
			{
				printf("Case #%d: 0\n",i);
				continue;
			}
			total=0;
			deal(0,T);
			printf("Case #%d: %d\n",i,total);
		}
		del(T);
	}
	fclose(stdout);
	fclose(stdin);
	return 0;
}

