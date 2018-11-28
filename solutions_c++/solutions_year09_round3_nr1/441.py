#include<iostream>
using namespace std;

long long hap(long long n, long long b)
{ 
  long long s = 0,t;
  while(n >= b)
  {
	for(t=b;(n/t) >=b;t = b*t);
	s += (n/t)*(n/t);
	n = n-t*(n/t);
  }
  return (s + n*n);
}

int main()
{
    freopen("A1.in","r",stdin);
    freopen("A1.out","w",stdout);
  int kase, T,i,j,k,c,I,b,l;
  long long sum;
  char str[62];
  int F[36], arr[36];
  scanf("%d\n",&T);
  for(i=1;i<=T;i++)
  {
	gets(str);
	l =strlen(str);
	memset(arr,255,sizeof(arr));
	memset(F,0,sizeof(F));
	for(k=0;k<l;k++)
    {
	  if (str[k] >= 'a')
         F[10+str[k]-'a']=1;
	  else
		  F[str[k]-'0']=1;
	}
	for(k=0,b=0;k<36;k++)
	  b += F[k];
	if (b==1)
	   b=2;
	
	if (str[0] >= 'a')
	   arr[10+str[0] - 'a'] = 1;
	else
        arr[str[0] - '0'] =1;
        
	for(k=1;k<l && str[k]==str[0];k++);
	
	if(k!=l)
    {
	  if (str[k] >= 'a')
		 arr[10+str[k]-'a'] = 0;
	  else
		  arr[str[k] - '0'] =0;
	}
	  
	for(j=k+1,c=2;j<l;j++)
    {
	  if (str[j] >= 'a')
		 I = 10+str[j] - 'a';
	  else
		  I = str[j] - '0';
	  if (arr[I] == (-1))
		 arr[I] = c++;
	}
	for (k=0,sum=0;k<l;k++)
	    if (str[k] >='a')
		   sum = sum*b + arr[10 + str[k]-'a'];
	  else
		  sum = sum*b + arr[str[k] - '0'];
	printf("Case #%d: %d\n",i,sum);
  }
}
