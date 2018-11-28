#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;
#define INF 2000000000
#define INFLL (1LL<<62)
#define SS getint()
#define SSL getlint()
#define rep(i,n) for(int i=0;i<(n);i++)
#define rept(i,m,n) for(int i=(m);i<(n);i++)
#define ull unsigned long long
#define lint long long
#define MX 10000001
/********************* FAST IO *********************************/

#define NEGATIVE
#define BUFSIZE (10000)
char inputbuffer[BUFSIZE];
char *ioptr=inputbuffer+BUFSIZE,*ioend=inputbuffer+BUFSIZE;
int input_eof=0;
#define getchar() ({if (ioptr >= ioend) init_input(); *ioptr++;})
#define eof() (ioptr>=ioend && input_eof)
#define eoln() ({if(ioptr >= ioend) init_input(); *ioptr == '\n';})
void init_input()
{
	if (input_eof) return;
	int existing = BUFSIZE - (ioend - inputbuffer);
	memcpy(inputbuffer, ioend, existing);
	int wanted = ioend - inputbuffer;
	int count=fread(inputbuffer + existing, 1, wanted, stdin);
	if (count < wanted)
		input_eof = 1;
	ioend = inputbuffer + BUFSIZE - (wanted - count);
	while (*--ioend > ' ');
	ioend++;
	ioptr=inputbuffer;
}
inline void non_whitespace()
{
	for(;;){
		if(ioptr>=ioend)	init_input();
		if(*ioptr>' ')    return;
		ioptr++;
	}
}
inline int getint()
{
	non_whitespace();
	#ifdef NEGATIVE
	int neg=0;
	if(*ioptr=='-'){
		ioptr++;
		neg=1;
	}
	#endif
	int n=0;
	while(*ioptr>' ')
		n=(n<<3)+(n<<1)+*ioptr++-'0';
	ioptr++;
	#ifdef NEGATIVE
	if(neg) n=-n;
	#endif	
	return n;
}
inline lint getlint()
{
	non_whitespace();
	#ifdef NEGATIVE
	int neg=0;
	if(*ioptr=='-'){
		ioptr++;
		neg=1;
	}
	#endif
	lint n=0;
	while(*ioptr>' ')
		n=(n<<3)+(n<<1)+*ioptr++-'0';
	ioptr++;
	#ifdef NEGATIVE
	if(neg) n=-n;
	#endif	
	return n;
}

/*----------------------------- 	Actual code follows 	-------------------------*/


int main()
{
	int i,j,k,l,n,m,t,s,p;
	t=SS;
	for(k=1;k<=t;++k)
	{
		n=SS;
		s=SS;
		p=SS;
		
		int a[n];
		
		rep(i,n)
			a[i]=SS;
		
		int cnt=0;
		
		if(p==0)
			cnt=n;			
		else
		{
			sort(a,a+n);
			int ind=n-1;
		
			//find the ones with score >=3*p-2, as we won't need surprising triplets for them (p>=1)
			while(ind>=0&&a[ind]>=3*p-2)
			{
					ind--;
					cnt++;
			}		
			
			if(p>=2)
			{
				while(ind>=0&&s>0&&a[ind]>=3*p-4)
				{
						ind--;
						s--;
						cnt++;
				}
			}
		}
		
		printf("Case #%d: %d\n",k,cnt);
	}	
	return 0;
}










