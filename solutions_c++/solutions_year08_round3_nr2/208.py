#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>

using namespace std;

#define min(a,b) ((a) < (b) ? (a) : (b))
#define max(a,b) ((a) > (b) ? (a) : (b))

#define CLR(a) memset(a,0,sizeof(a))

#define i64 __int64

i64 cases,caseno,len,res;
char a[100],b[100];

void call(int i,int blen)
{
	if(i==0)
	{
		b[blen]=a[0];
		call(i+1,blen+1);
		return;
	}
	if(i==len)
	{
		b[blen]=0;
		i64 k=1,sum=0,sum1;
		
		for(i=0;i<blen;i++)
		{
			if(isdigit(b[i]))
			{
				sum1=0;
				while(isdigit(b[i])) sum1=sum1*10+b[i++]-48;
				sum+=sum1*k;
				i--;
				continue;
			}
			if(b[i]=='+') k=1;
			if(b[i]=='-') k=-1;
		}
		if(!(sum%2) || !(sum%3) || !(sum%5) || !(sum%7)) res++;
		return;
	}
	b[blen]=a[i];
	call(i+1,blen+1);

	b[blen]='+';
	b[blen+1]=a[i];
	
	call(i+1,blen+2);
	
	b[blen]='-';
	b[blen+1]=a[i];
	
	call(i+1,blen+2);
}

void process()
{
	res=0;
	len=strlen(a);
	call(0,0);
	printf("Case #%I64d: %I64d\n",++caseno,res);
}

int main()
{
	freopen("Inputs\\fk.txt","r",stdin);
	freopen("Inputs\\B1.txt","w",stdout);

	scanf("%I64d",&cases);
	while(cases--)
	{
		scanf("%s",a);
		process();
	}
	return 0;
}
