#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define lim 26
#define lim2 75001
#define lim3 16

struct ST
{
  int V[lim];
};

int l,d,n,i,j,sz,x,c,a,t,res;
char str[1000000];
ST T[lim2];
int M[lim2][lim3];
bool B[lim3][lim];

int solve(int i,int j)
{
  int &res=M[i][j],k;
  
  if(res==-1)
    if(j==l)
	  res=1;
	else
	{
	  res=0;
	  for(k=0;k<lim;k++)
	    if(B[j][k] && T[i].V[k]!=-1)
		  res+=solve(T[i].V[k],j+1);
	}
  return res;
}
int main()
{
  scanf("%d%d%d",&l,&d,&n);
  memset(T,-1,sizeof T);
  for(i=0,t=1;i<d;i++)
  {
    scanf("%s",str);
	for(j=x=0,sz=strlen(str);j<sz;j++)
	{
	  if(T[x].V[str[j]-'a']==-1)
	    T[x].V[str[j]-'a']=t++;
      x=T[x].V[str[j]-'a'];
	}
  }
  for(c=1;c<=n;c++)
  {
    scanf("%s",str);
	memset(B,0,sizeof B);
	for(i=a=0,sz=strlen(str);i<sz;)
	{
	  if(str[i]=='(')
	  {
	    i++;
		while(str[i]!=')')
		  B[a][str[i++]-'a']=1;
		i++;
	  }
	  else
	    B[a][str[i++]-'a']=1;
	  a++;
	  if(a>l)
	    break;
	}
	if(a==l)
	{
	  memset(M,-1,sizeof M);
	  res=solve(0,0);
	}
	else
      res=0;
	printf("Case #%d: %d\n",c,res);
  }
  return 0;
}
