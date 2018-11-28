#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

struct Node
{
  Node (){memset(p,0,sizeof(p));}
  Node *p[26];
};
Node *head=new Node;

void insert(char *str)
{ 
  Node *tmp=head;
  
  while(*str)
  { 
    if(tmp->p[*str-97]==NULL)
       tmp->p[*str-97]=new Node;
    tmp=tmp->p[*str-97];
    str++;
  }
}

int ans;
char pattern[500000002];
int L,D,N,len;

void dfs(int i,int l,Node *tmp)
{ 
  if(l==L)  {ans++;return;}
  if(pattern[i]=='(')
  {
  	int j,k;
    for(j=i+1;j<len;j++)
     if(pattern[j]==')')
      break;
    for(k=i+1;k<j;k++)
      if(tmp->p[pattern[k]-97])
      dfs(j+1,l+1,tmp->p[pattern[k]-97]);  
  }
  else
  {
    if(tmp->p[pattern[i]-97])
     dfs(i+1,l+1,tmp->p[pattern[i]-97]);  
  }
}
char str[16];

int main()
{ 
   freopen("A-large.in","r",stdin);
  freopen("A-small-attempt.out","w",stdout);
  
  int i;
  
  scanf("%d%d%d",&L,&D,&N);
  for(i=0;i<D;i++)  
  {
    scanf("%s",str);
    insert(str);
  } 
  
  for(i=0;i<N;i++)
  {
    scanf("%s",pattern);
    len=strlen(pattern);
    ans=0;
    dfs(0,0,head);
    printf("Case #%d: %d\n",i+1,ans);
  }
  return 0;
}
