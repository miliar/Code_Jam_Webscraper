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
#define  MAXM     (1<<7)  
#define  MAXN     101
#define  eps      1e-6
#define  MOD      50261
typedef __int64 int64;
FILE *fin;
FILE *fout;
int T;
char cs[30];
vector<int> vi;
int main()
{
   	fin=fopen("B-large.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
	int N;
	fscanf(fin,"%d",&T);
    int rounds;
	for (rounds=1;rounds<=T;rounds++)
	{
		fscanf(fin,"%s",cs);
		vi.clear();
		REP(i,strlen(cs)) vi.push_back(cs[i]-'0');
		bool flag=false;
	    while (next_permutation(vi.begin(),vi.end()))
	    {
			if(vi[0]!=0)
			{
				flag=true;
				break;
			}
	    }
		if(!flag)
		{
			vector<int> vii;
			REP(i,strlen(cs)) if(cs[i]!='0')vii.push_back(cs[i]-'0');
			sort(vii.begin(),vii.end());
			vi.clear();
			int n=strlen(cs)+1;
			vi.push_back(vii[0]);
			REP(i,n-vii.size()) vi.push_back(0);
			for (i=1;i<vii.size();i++)
			{
				vi.push_back(vii[i]);
			}
		}
	    printf("Case #%d: ",rounds);
        fprintf(fout,"Case #%d: ",rounds);
		REP(i,vi.size()-1)
		{
			printf("%d",vi[i]);
			fprintf(fout,"%d",vi[i]);
		}
			printf("%d\n",vi[i]);
			fprintf(fout,"%d\n",vi[i]);

	}
}
