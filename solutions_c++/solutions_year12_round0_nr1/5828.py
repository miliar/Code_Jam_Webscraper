#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<string>
#include<algorithm>
#include<functional>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<cassert>
using namespace std;
#define RLC(num,pos) ((num << pos)|(num >> (32 - pos)))
#define RRC(num,pos) ((num >> pos)|(num << (32 - pos)))

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UINT;
int gcd( int a, int b ) {  if( !b ) return a;  return gcd( b, a % b ); }

#define tr(container, it)for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 

#define getcx getchar_unlocked
inline void inp( int &n )//fast input function
{
        n=0;
        int ch=getcx();int sign=1;
        while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}

        while(  ch >= '0' && ch <= '9' )
                n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
		n=n*sign;
}
//}

/* Main code starts from here */
int main()
{

char   s[28];

char  ans[1002];
char   str[1002];
s[0]='y';s[1]='h';s[2]='e';s[3]='s';s[4]='o';s[5]='c';s[6]='v';s[7]='x';s[8]='d';s[9]='u';s[10]='i';s[11]='g';s[12]='l';s[13]='b';s[14]='k';s[15]='r';s[16]='z';s[17]='t';
s[18]='n';s[19]='w';s[20]='j';s[21]='p';s[22]='f';s[23]='m';s[24]='a';s[25]='q';

int tc,i;
 		scanf("%d",&tc);

 		char ch;
 		int c,p=0;
 		scanf("%c",&ch);
 		
 		while(tc--)
 		{

 			gets(str);
 			p++;

			int len=strlen(str);

			printf("Case #%d: ",p);
			for(i=0;i<len;i++)
			{
				if(str[i]!=' ')
				{ 
					c=str[i];
					c=c%97;
					printf("%c",s[c]);
				}
				else 
					printf("%c",' ');

			}
			printf("\n");

			 
		}
return 0;
}

