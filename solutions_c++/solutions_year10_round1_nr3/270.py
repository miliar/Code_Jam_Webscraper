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
#define  MAXN      33
typedef __int64 int64;
FILE *fin;
FILE *fout;
int A1,A2,B1,B2;
int M;
int N,K;
map<pair<int,int>,bool> mp;
vector<pair<int,int> > vp;
bool isok(int a,int b)
{
	if(a<b) swap(a,b);
	int A=a,B=b;
	vp.clear();
	while (true)
	{
		if(a%b==0) break;
		vp.push_back(make_pair(a,b));
		int t=a%b;
		a=b;
		b=t;
	}
    mp.clear();
	if(a==b)
	mp[make_pair(a,b)]=false;
	else mp[make_pair(a,b)]=true;
	int i,n;
	n=vp.size()-1;
	for (i=n;i>=0;i--)
	{
		a=vp[i].first;
		b=vp[i].second;
		if(a/b>1) mp[make_pair(a,b)]=true;
		else mp[make_pair(a,b)]=!mp[make_pair(b,a%b)];
	}
	return mp[make_pair(A,B)];
}
int main()
{
   	fin=fopen("C-small-attempt0.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
	fscanf(fin,"%d",&M);
    int rounds;
	for (rounds=1;rounds<=M;rounds++)
	{
		  fscanf(fin,"%d%d%d%d",&A1,&A2,&B1,&B2);
		  int cnt=0;
		  rep(i,A1,A2+1) rep(j,B1,B2+1) if(isok(i,j)) cnt++;
                printf("Case #%d: %d\n",rounds,cnt);
                fprintf(fout,"Case #%d: %d\n",rounds,cnt);
	}
}
