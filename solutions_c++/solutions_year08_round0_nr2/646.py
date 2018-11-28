#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<algorithm>
#define MinNum(a,b) ((a)>(b)?(b):(a))
#define MaxNum(a,b) ((a)<(b)?(b):(a))
#define INF INF32
#define NA (-1)

#define uint64 unsigned long long
#define _1 ((uint64)1)
#define int64 long long
/*
#define uint64 unsigned __int64
#define _1 ((uint64)1)
#define int64 __int64
*/

const int64 INF64=(_1<<63)-1;
const int INF32=(_1<<31)-1;

using namespace std;

/*
class Temp{
public:
	void Ret()
	{
	}
};
*/

#define MAXN 201

FILE *fin=fopen("B-large.in","r");
FILE *fout=fopen("B-large.out","w");

class Train{
public:
	int dt,at,typ,vis;
};

bool operator<(Train x,Train y)
{
	return x.at<y.at;
}

int n,na,nb,tt;
Train t[MAXN];
int p[MAXN][MAXN],cx[MAXN],yx[MAXN],fx[MAXN];

int numtime(char s[101])
{
	int h=(s[0]-'0')*10+(s[1]-'0');
	int m=(s[3]-'0')*10+(s[4]-'0');
	return h*60+m;
}

void init()
{
	int i;
	char temp[101];

	fscanf(fin,"%d",&tt);
	fscanf(fin,"%d %d",&na,&nb);
	for (i=0; i<na; i++)
	{
		fscanf(fin,"%s",temp);
		t[i].dt=numtime(temp);
		fscanf(fin,"%s",temp);
		t[i].at=numtime(temp);
		t[i].typ=0;
		t[i].vis=0;
	}
	for (i=na; i<na+nb; i++)
	{
		fscanf(fin,"%s",temp);
		t[i].dt=numtime(temp);
		fscanf(fin,"%s",temp);
		t[i].at=numtime(temp);
		t[i].typ=1;
		t[i].vis=0;
	}
	n=na+nb;
}

int path(int pp)
{
	int i;
	
	if (fx[pp]==1)
		return 0;
	fx[pp]=1;
	for (i=0; i<n; i++)
		if (p[pp][i])
			if (yx[i]==-1||path(yx[i]))
			{
				yx[i]=pp;
				cx[pp]=1;
				return 1;
			}
	return 0;
}

void search()
{
	int i,j,r[2];

	for (i=0; i<n; i++)
		for (j=0; j<n; j++)
			if (t[i].typ!=t[j].typ&&t[i].at+tt<=t[j].dt)
				p[i][j]=1;
			else
				p[i][j]=0;
	memset(cx,0,sizeof(cx));
	memset(yx,-1,sizeof(yx));
	for (i=0; i<n; i++)
		if (cx[i]==0)
		{
			memset(fx,0,sizeof(fx));
			path(i);
		}
	r[0]=0;
	r[1]=0;
	for (i=0; i<n; i++)
		if (yx[i]==-1)
			r[t[i].typ]++;
	fprintf(fout,"%d %d\n",r[0],r[1]);
}

int main()
{
	int testdata,i;

	fscanf(fin,"%d",&testdata);
	for (i=0; i<testdata; i++)
	{
		fprintf(fout,"Case #%d: ",i+1);
		init();
		search();
	}
	return 0;
}
