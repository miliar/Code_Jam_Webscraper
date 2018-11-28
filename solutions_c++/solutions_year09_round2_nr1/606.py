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
int N;
char cs[3000];
typedef struct node 
{
	double p;
	string shu;
	bool isleaf;
}node;
node tree[1000000];
void gettree(int idx)
{
	while (true)
	{
		char ct;
		fscanf(fin,"%c",&ct);
		if(ct=='(') break;
	}
	double tp;
	fscanf(fin,"%lf",&tp);
	tree[idx].p=tp;
	int top=0;
	while (true)
	{
		char ct;
		fscanf(fin,"%c",&ct);
		if(ct==' '||ct=='\n') continue;
		cs[top++]=ct;
		break;
	}
	if(cs[0]==')')
	{
		tree[idx].isleaf=true;
		return ;
	}
	while (true)
	{
		char ct;
		fscanf(fin,"%c",&ct);
		if(ct==' '||ct=='\n')break;
		cs[top++]=ct;
	}
	cs[top]='\0';
	tree[idx].isleaf=false;
	tree[idx].shu=string(cs);
	gettree(idx<<1);
	gettree((idx<<1)+1);
	while (true)
	{
		char ct;
		fscanf(fin,"%c",&ct);
		if(ct==')') break;
	}
	return ;
}
set<string> mset;
double res;
void doit(int idx)
{
	res*=tree[idx].p;
	if (tree[idx].isleaf)	return ;
    if(mset.find(tree[idx].shu)!=mset.end())
	{
		doit(idx<<1);
	}
	else 
	{
		doit((idx<<1)+1);
	}
}
void solve()
{
	int m;
	fscanf(fin,"%s",cs);
	fscanf(fin,"%d",&m);
	int i,j;
	mset.clear();
	REP(i,m) 
	{
		fscanf(fin,"%s",cs);
		mset.insert(string(cs));
	}
	res=1;
	doit(1);
    printf("%lf\n",res);
    fprintf(fout,"%lf\n",res);
}
int main()
{
   	fin=fopen("A-small-attempt1.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
	int T;
	fscanf(fin,"%d",&T);
    int rounds;
	for (rounds=1;rounds<=T;rounds++)
	{
		  int n;
		  fscanf(fin,"%d",&n);
		  gettree(1);
		  printf("Case #%d: \n",rounds);
          fprintf(fout,"Case #%d: \n",rounds);
		  int m;
		  fscanf(fin,"%d",&m);
		  REP(i,m) solve();
	}
}
