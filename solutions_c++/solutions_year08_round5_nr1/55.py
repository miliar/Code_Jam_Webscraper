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


const int maxn=5000000;
const int maxsize=6000+5;
const int MX[]={-1,0,1,0};
const int MY[]={0,1,0,-1};

bool A[maxsize][maxsize],G[maxsize][maxsize];
int L[maxsize],R[maxsize],U[maxsize],D[maxsize];

void check(int &L,int &R,int P)
{
	if (L<0) L=R=P;
	else 
	{
		if (P<L) L=P;
		if (P>R) R=P;
	}
}
int main()
{
//	freopen("input.txt","r",stdin);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d:",caseId);
		int cnt;
		scanf("%d",&cnt);
		int dir=0;
		int X1=3002,Y1=3002;
		memset(A,false,sizeof(A));
		memset(G,false,sizeof(G));
		memset(L,255,sizeof(L));
		memset(U,255,sizeof(U));
		for (;cnt>0;cnt--)
		{
			char str[50];
			int times;
			scanf("%s%d",str,&times);
			bool findF=false;
			for (int i=0;str[i];i++) if (str[i]=='F') findF=true;
			if (!findF) times%=4;
			for (;times>0;times--)
				for (int i=0;str[i];i++)
					if (str[i]=='L') dir=(dir+3)%4;
					else if (str[i]=='R') dir=(dir+1)%4;
					else 
					{
						int X2=X1+MX[dir],Y2=Y1+MY[dir];
						if (X1==X2) A[X1][min(Y1,Y2)]=true;
						if (X1==X2) check(U[min(Y1,Y2)],D[min(Y1,Y2)],X1);
						if (Y1==Y2) check(L[min(X1,X2)],R[min(X1,X2)],Y1);
						X1=X2;
						Y1=Y2;
					}
		}
		for (int j=0;j<maxsize;j++)
			for (int i=1;i<maxsize;i++)
				A[i][j]=(A[i][j]!=A[i-1][j]);
		for (int i=0;i<maxsize;i++) if (L[i]>=0)
			for (int j=L[i];j<R[i];j++)
				G[i][j]=true;
		for (int i=0;i<maxsize;i++) if (U[i]>=0)
			for (int j=U[i];j<D[i];j++)
				G[j][i]=true;
		int result=0;
		for (int i=0;i<maxsize;i++) for (int j=0;j<maxsize;j++)
			if (G[i][j] && !A[i][j])
				result++;
		printf(" %d\n",result);
		fflush(stdout);
	}
	return 0;
}

