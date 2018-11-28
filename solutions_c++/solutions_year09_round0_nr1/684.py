
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<cstdio>

#define F(i,n) for(i = 0; i < (int)n;i++)
#define FE(i,v) for( typeof((v).begin()) i = (v).begin(); i!= (v).end();i++)

using namespace std;

int m, n;
int trie[100000][30];
int inuse[10000], last;
int end[10000];
void maketrie(int p,char *s)
{
   if(*s==0) {return;}
   if(trie[p][(*s)-'a'] == -1)
   {
      trie[p][(*s)-'a'] = ++last;
      maketrie(last,s+1);
   }
   else
       maketrie( trie[p][(*s)-'a'] , s+1);
}
int answer ;
void solve(int p,char *s)
{
   if(p==-1) return;
   if(*s==0) { answer++;return;}
   char *t = s;
   if(*s=='(')
   {
      while(*++t != ')') ;
      while( ++s != t)
      solve(trie[p][(*s)-'a'],t+1);
   }
   else
      solve(trie[p][(*s)-'a'],s+1);
}
char s[10000];
int main()
{
   int i, j, k, t;
   int L,D,N;
   scanf("%d %d %d\n",&L,&D,&N);
   memset(trie,-1,sizeof(trie));
   F(i,D)
   {
      gets(s);
      maketrie(0,s);
   }
   F(i,N)
   {
      answer = 0;
      gets(s);
      solve(0,s);
      printf("Case #%d: %d\n",i+1,answer);
   }
   
   return 0;
}
