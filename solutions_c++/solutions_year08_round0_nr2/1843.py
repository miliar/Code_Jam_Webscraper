#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;

int ATB[101][101],BTA[101][101];

typedef struct node
{
	int at,dh,dm,ah,am;
	
}NODE;
NODE A[101],B[101];
bool operator==(const NODE &A,const NODE &B)
	{
		return A.dh==B.dh &&A.dm==B.dm&&A.ah==B.ah&&A.am==B.am;
	}
bool operator<(const NODE &A,const NODE &B)
{
	if(A.dh*100+A.dm!=B.dh*100+B.dm) return A.dh*100+A.dm<B.dh*100+B.dm;
	return A.ah*100+A.am<B.ah*100+B.am;
}

bool cmp(const NODE &A,const NODE &B)
{
	return A.ah*100+A.am<B.ah*100+B.am;
}
int viz[101][2];
int NA,NB,T;
int na,nb;

void dfs(int cur,int f)
{
	int i,j;
	if(!viz[cur][f])
	{
		viz[cur][f]=1;
		if(f==0)
		{
			vector<NODE> temp;
			for(i=0;i<NB;i++)
				if(!viz[i][1]&& ATB[cur][i])
					temp.push_back(B[i]);
			if(temp.size()==0) return;
			sort(temp.begin(),temp.end(),cmp);
			for(i=0;i<NB;i++) if(ATB[cur][i] && B[i]==temp[0]) break;
			dfs(i,1);
			nb--;
		}
		else
		{
			vector<node> temp;
			for(i=0;i<NA;i++)
				if(!viz[i][0] && BTA[cur][i])
					temp.push_back(A[i]);
			if(temp.size()==0) return;
			sort(temp.begin(),temp.end(),cmp);
			for(i=0;i<NA;i++) if( BTA[cur][i] && A[i]==temp[0]) break;
			dfs(i,0);
			na--;
		}
	}
}













int main()
{
	FILE *fp,*fw;
	
		fp=fopen("B-small-attempt1.in","r");
	//fp=fopen("Bsmall.txt","r");
	fw=fopen("output.txt","w");
	int count,N,i,j;
	fscanf(fp,"%d\n",&N);
	for(count=1;count<=N;count++)
	{
		char ch[101];
		fscanf(fp,"%d\n",&T);
		fscanf(fp,"%d %d\n",&NA,&NB);
		memset(viz,0,sizeof(viz));
		memset(ATB,0,sizeof(ATB));
		memset(BTA,0,sizeof(BTA));
		for(i=0;i<NA;i++)
		{
			fscanf(fp,"%d:%d %d:%d\n",&A[i].dh ,&A[i].dm,&A[i].ah,&A[i].am);
			A[i].at=0;
		}
		for(i=0;i<NB;i++)
		{
			fscanf(fp,"%d:%d %d:%d\n",&B[i].dh ,&B[i].dm,&B[i].ah,&B[i].am);
			B[i].at=1;
		}

		sort(A,A+NA);
		sort(B,B+NB);
		for(i=0;i<NA;i++)
			for(j=0;j<NB;j++)
			{
				if(B[j].dh*100+B[j].dm>=A[i].ah*100+A[i].am+T)
					ATB[i][j]=1;
			}

		for(i=0;i<NB;i++)
			for(j=0;j<NA;j++)
			{
				if(A[j].dh*100+A[j].dm>=B[i].ah*100+B[i].am+T)
					BTA[i][j]=1;
			}
	
		vector<node> temp;
		for(i=0;i<NA;i++)
			temp.push_back(A[i]);
		for(i=0;i<NB;i++)
			temp.push_back (B[i]);
		sort(temp.begin(),temp.end());
		na=NA;
		nb=NB;
		for(i=0;i<temp.size();i++)
		{
			if(temp[i].at==0)
			{
				for(j=0;j<NA;j++)
					if(A[j]==temp[i]) break;
				if(!viz[j][0])
				{
					dfs(j,0);
				}
			}
			else
			{
				for(j=0;j<NB;j++)
					if(B[j]==temp[i]) break;
				if(!viz[j][1])
				{
					dfs(j,1);
				}
			}
		}

		
		fprintf(fw,"Case #%d: %d %d\n",count,na,nb);
	}
	return 0;
 
}

