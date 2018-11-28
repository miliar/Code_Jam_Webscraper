#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <queue>
using namespace std;
#define   max(a,b)    ((a)>(b)?(a):(b))
#define   min(a,b)    ((a)<(b)?(a):(b))
#define   sqr(a)         ((a)*(a))
#define   rep(i,a,b)  for(i=(a);i<(b);i++)
#define   REP(i,n)     rep(i,0,n)
#define   clr(a)      memset((a),0,sizeof (a));
#define   mabs(a)     ((a)>0?(a):(-(a))) 
#define   inf         1000000000
#define  MAXL     20
#define  MAXD     5010
#define  eps      1e-6
#define  MAXN      10000
typedef __int64 int64;
FILE *fin;
FILE *fout;
int L,D,N;
int n;
char dic[MAXD][MAXL];
char cs[MAXN];
bool isok(char s[])
{
	int i,j,k;
	j=0;
    REP(i,L)
	{
		if(j>=n) return false;
		if(s[i]==cs[j]) 
		{
			j++;
			continue;
		}
		else if(cs[j]=='(')
		{
			j++;
			bool f=false;
		    while (true)
		    {
                if(cs[j]==s[i])
				{
					f=true;
					j++;
				}
				else if(cs[j]==')')
				{
					j++;
					break;
				}
				else j++;
		    }
			if(!f) return false;
		}
		else 
		{
			return false;
		}
	}
	if(i==L&&j==n) return true;
	return false;
}
int doit()
{
	int i,j;
	int ret=0;
	REP(i,D)  ret+=isok(dic[i]);
	return ret;
}
int main()
{
   	fin=fopen("A-large.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
	fscanf(fin,"%d%d%d",&L,&D,&N);
	REP(i,D) fscanf(fin,"%s",dic[i]);
    int rounds;
	for (rounds=1;rounds<=N;rounds++)
	{
		  fscanf(fin,"%s",cs);
		  n=strlen(cs);
		  int ret=doit();
		  printf("Case #%d: %d\n",rounds,ret);
          fprintf(fout,"Case #%d: %d\n",rounds,ret);
	}
}
