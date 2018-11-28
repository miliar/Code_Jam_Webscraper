#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <queue>
#include <iostream>
#include <string>
using namespace std;

#define YES 1
#define NO 0
#define NUM 26

/*字典树的数据结构*/

struct trie
{
   trie * next[NUM];
   int isword;
};

/*字典树的数据结构*/

/*字典树的相关操作*/

trie thead,*t,*s;

int exist(trie &head,char x[])
{
   int i;
   int len;
   len=strlen(x);
   if(len==0) return NO;
   s=&head;
   for(i=0;i<len;i++)
   {
       if(s->next[x[i]-'a']==NULL) break;
       else s=s->next[x[i]-'a'];
   }
   if(i==len && s->isword==YES) return YES;
   else return NO;
}

int insert(trie &head,char x[])
{
   int i,j;
   int len;
   len=strlen(x);
   s=&head;
   for(i=0;i<len;i++)
   {
       if(s->next[x[i]-'a']==NULL) break;
       else s=s->next[x[i]-'a'];
   }
   if(i==len)
   {
       s->isword=YES;
       return YES;
   }
   for(;i<len;i++)
   {
       t=(trie*)malloc(sizeof(trie));
       for(j=0;j<NUM;j++) t->next[j]=NULL;
       t->isword=YES;
       s->next[x[i]-'a']=t;
       s=t;
   }
   s->isword=YES;
   return NO;
}

void deltrie(trie *current)
{
   int i;
   for(i=1;i<NUM;i++)
   {
       if(current->next[i]==NULL) continue;
       deltrie(current->next[i]);
   }
   free(current);
   current=NULL;
}

void inittrie(trie &head)
{
   int i;
   for(i=0;i<NUM;i++)
       head.next[i]=NULL;
   head.isword=NO;
}
char* change(string s)
{
	int i;
	char *str;
	str = new char[1000];
	for (i=0;i<s.length();i++)
		str[i] = s[i];
	str[i] = '\0';
	return str;
}
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	trie head;
	int l,d,n,i,j,k;
	char str[30];
	char qq[1000];
	string s[1000];
	while (scanf("%d %d %d",&l,&d,&n)!=EOF)
	{
		inittrie(head);
		while (d--)
		{
			scanf("%s",&str);
			insert(head,str);
		}
//		cout << exist(head,"abcd");
		
		int p;
		for (p=1;p<=n;p++)
		{
			scanf("%s",&qq);
			k = 0;
			int len = strlen(qq);
			for (j=0;j<len;j++)
			{
				if (qq[j]=='(')
				{
					s[k] = "";
					j++;
					while (j<len&&qq[j]!=')')
						s[k] += qq[j++];
					k++;
				}
				else s[k++] = qq[j];
			}
			if (k!=l) printf("Case #%d: 0\n",p);
			else
			{
				queue <string> que;
				for (i=0;i<s[0].length();i++)
				{
					string s1 = "";
					s1 += s[0][i];
					if (exist(head,change(s1)))
						que.push(s1);
				}
				int result=0;
				while (!que.empty())
				{
					string s1 = que.front();
					que.pop();
					if (s1.length()==l) result++;
					else
					{
						j = s1.length();
						for (i=0;i<s[j].length();i++)
						{
							string temp = s1;
							temp += s[j][i];
							if (exist(head,change(temp)))
								que.push(temp);
						}
					}
				}
				printf("Case #%d: %d\n",p,result);
			}
		}
	}
}