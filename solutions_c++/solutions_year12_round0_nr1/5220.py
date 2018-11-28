#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

#define floop(i,n) for(int i = 0; i < (int)(n); i++)
#define floopi(i,m,n) for(int i = m; i < (int)(n); i++)
#define floopd(i,m,n) for(int i = m; i > (int)(n); i--)

typedef long long l2;
typedef vector<string> vstr;

int compare(int,int,int);

//#define TEST
#define SMALL
//#define LARGE

void main()
{

#ifdef TEST
	freopen("a.txt", "rt", stdin);
	freopen("b.txt", "wt", stdout);
#endif
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif

   int T;
   char G[200] = {0};
   char S[200],os[200] = {0};

   G['a']='y';G['b']='h';G['c']='e';G['d']='s';G['e']='o';G['f']='c';G['g']='v';G['h']='x';
   G['i']='d';G['j']='u';G['k']='i';G['l']='g';G['m']='l';G['n']='b';G['o']='k';G['p']='r';
   G['q']='z';G['r']='t';G['s']='n';G['t']='w';G['u']='j';G['v']='p';G['w']='f';G['x']='m';
   G['y']='a';G['z']='q';

   scanf("%d\n", &T);
   floop(i,T)
   {
        fgets(S,200,stdin);
		floop(i,strlen(S))
		{
			if(S[i] != ' ')
				os[i] = G[S[i]];
			else
				os[i] = ' ';
		}
		printf("Case #%d: %s\n",i+1,os);
   }
}