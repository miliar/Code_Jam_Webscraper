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

FILE *fin=fopen("A-large.in","r");
FILE *fout=fopen("A-large.out","w");

#define MAXN 1000001
#define MOD 1000000000
int nn;
int64 a,b,c,d,m,x[MAXN],y[MAXN];

void init()
{
	int i;
	fscanf(fin,"%d %I64d %I64d %I64d %I64d %I64d %I64d %I64d",&nn,&a,&b,&c,&d,&x[0],&y[0],&m);
	x[0]%=m;
	y[0]%=m;
	for (i=1; i<nn; i++)
	{
		x[i]=(x[i-1]*a+b)%m;
		y[i]=(y[i-1]*c+d)%m;
	}
}

void search()
{
	int64 n[3][3];
	int64 ret=0;
	int i,j,i1,j1,i2,j2,i3,j3;

	for (i=0; i<3; i++)
		for (j=0; j<3; j++)
			n[i][j]=0;

	for (i=0; i<nn; i++)
		n[x[i]%3][y[i]%3]++;

	for (i1=0; i1<3; i1++)
		for (i2=0; i2<3; i2++)
			for (i3=0; i3<3; i3++)
				for (j1=0; j1<3; j1++)
					for (j2=0; j2<3; j2++)
						for (j3=0; j3<3; j3++)
							if ((i1+i2+i3)%3==0&&(j1+j2+j3)%3==0)
							{
								if (i1==i2&&i2==i3&&j1==j2&&j2==j3)
								{
									if (n[i2][j2]-1>=0&&n[i3][j3]-2>=0)
										ret+=n[i1][j1]*(n[i2][j2]-1)*(n[i3][j3]-2);
								}
								else if (i1==i2&&j1==j2)
								{
									if (n[i2][j2]-1>=0)
										ret+=n[i1][j1]*(n[i2][j2]-1)*n[i3][j3];
								}
								else if (i1==i3&&j1==j3)
								{
									if (n[i1][j1]-1>=0)
										ret+=n[i1][j1]*n[i2][j2]*(n[i3][j3]-1);
								}
								else if (i2==i3&&j2==j3)
								{
									if (n[i3][j3]-1>=0)
										ret+=n[i1][j1]*n[i2][j2]*(n[i3][j3]-1);
								}
								else
									ret+=n[i1][j1]*n[i2][j2]*n[i3][j3];
							}
	ret/=6;
	fprintf(fout,"%I64d\n",ret);
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
