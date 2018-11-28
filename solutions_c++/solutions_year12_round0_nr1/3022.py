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

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;
typedef vector<VII> VVII;
typedef vector<VI> VVI;

#define INF 2000000000
#define INFLL (1LL<<62)
#define FI first
#define SE second
#define PB push_back
#define SS ({int x;scanf("%d", &x);x;})
#define SSL ({LL x;scanf("%lld", &x);x;})
#define SSF getint()
#define SSLF getlint()
#define _mp make_pair

template<class T>
inline void _min(T &a,T b)
{
	if(a>b)
		a=b;
}

template<class T>
inline void _max(T &a,T b)
{
	if(a<b)
		a=b;
}

/********************* FAST IO *********************************/

// comment this line for only +ve numbers input in int and lints [slightly more efficient :P]
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
	if (input_eof)
		return;
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
	for(;;)
	{
		if(ioptr>=ioend)
			init_input();
		if(*ioptr>' ')
			return;
		ioptr++;
	}
}
inline int getint()
{
	non_whitespace();
	
	#ifdef NEGATIVE
	int neg=0;
	if(*ioptr=='-')
	{
		ioptr++;
		neg=1;
	}
	#endif
	
	int n=0;
	while(*ioptr>' ')
		n=(n<<3)+(n<<1)+*ioptr++-'0';
	ioptr++;
	
	#ifdef NEGATIVE
	if(neg)
		n=-n;
	#endif	
	return n;
}
inline LL getlint()
{
	non_whitespace();
	
	#ifdef NEGATIVE
	int neg=0;
	if(*ioptr=='-')
	{
		ioptr++;
		neg=1;
	}
	#endif
	
	LL n=0;
	while(*ioptr>' ')
		n=(n<<3)+(n<<1)+*ioptr++-'0';
	ioptr++;

	#ifdef NEGATIVE
	if(neg)
		n=-n;
	#endif	

	return n;
}

//******************************** programme code starts here*************************//

char A[]="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
char B[]="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
char C[]="yhesocvxduiglbkrztnwjpfmaq";
char s[200];
int main()
{
	int i,j,n,t;
	
	scanf("%d\n",&t);
	for(j=1;j<=t;j++)
	{
		gets(s);
		for(i=0;s[i]!='\0';i++)
			if(s[i]!=' ')
				s[i]=C[s[i]-'a'];
		printf("Case #%d: %s\n",j,s);
	}
	return 0;
}
