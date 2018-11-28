#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define lim 101

int cs,c,l,i,j,k,s,n,m;
double p;
int S[lim],E[lim];
bool L[lim];
double P[lim];
char N[lim][lim],str[lim],A[lim][lim],M[lim][lim];

int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%d ",&l);
	s=0;
	for(i=0;i<l;i++)
	{
	  gets(A[i]);
      j=0;
	  while(A[i][j]==' ')
		j++;
	  if(A[i][strlen(A[i])-1]==')' && A[i][j]=='(')
	  {
	    L[i]=1;
		sscanf(A[i]+j+1,"%lf",&P[i]);
		E[i]=i;
      }
	  else if(A[i][j]==')')
	  {
	    E[S[--s]]=i;
	  }
	  else
	  {
	    L[i]=0;
		sscanf(A[i]+j+1,"%lf%s",&P[i],N[i]);
		S[s++]=i;
	  }
	}
	scanf("%d",&n);
	printf("Case #%d:\n",c);
	for(i=0;i<n;i++)
	{
	  scanf("%s%d",str,&m);
	  for(j=0;j<m;j++)
	    scanf("%s",M[j]);
	  j=0;
	  p=1;
	  while(1)
	  {
	    p*=P[j];
		if(L[j])
		  break;
        for(k=0;k<m;k++)
		  if(!strcmp(M[k],N[j]))
		    break;
		if(k<m)
		  j++;
		else
		  j=E[j+1]+1;
	  }
	  printf("%.10lf\n",p);
	}
  }
  return 0;
}
