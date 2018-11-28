#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>

#define MAX_N 1005
#define MAX_VAL 10005
#define MAX_N2 10
#define INF 1000000000

using namespace std;

FILE *fin=fopen("B-large.in","r");
FILE *fout=fopen("B-large.out","w");

int mic[(1<<MAX_N2)];
int t,iii;
int n,i,j;
int k;
int val[MAX_N];
int cnt[MAX_VAL];
int cnttmp[MAX_VAL];
int le,ri,mi,v;
int tmp1,tmp2;
multiset<pair<int,int> > S;
multiset<pair<int,int> >::iterator it;
bool chk1;

int findans()
{
	int answer=INF;
	S.clear();
	for(i=0;i<MAX_VAL;i++)
	{
		while(cnt[i]>0)
		{
			it=S.lower_bound(pair<int,int>(i,0));
			if(it!=S.begin())
			it--;
			if(it==S.end()||it->first!=i-1)
			{
				S.insert(pair<int,int>(i,i));
			}
			else
			{
				tmp1=it->first;
				tmp2=it->second;
				S.erase(it);
				S.insert(pair<int,int>(i,tmp2));
			}
			cnt[i]--;
		}
	}
	//fprintf(fout,"KUY %d\n",S.size());
	for(it=S.begin();it!=S.end();it++)
	{
		answer=min(answer,(it->first)-(it->second)+1);
	}
	return answer;
}

int main()
{
	fscanf(fin,"%d",&t);
	for(iii=0;iii<t;iii++)
	{
		fscanf(fin,"%d",&n);
		for(i=0;i<MAX_VAL;i++)
		{
			cnt[i]=0;
		}
		for(i=0;i<n;i++)
		{
			fscanf(fin,"%d",&val[i]);
			cnt[val[i]]++;
		}
		fprintf(fout,"Case #%d: ",iii+1);
		if(n!=0)
		{
			fprintf(fout,"%d\n",findans());
		}
		else
		{
			fprintf(fout,"0\n");
		}
	}
	return 0;
}