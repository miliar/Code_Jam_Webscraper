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

int check(int v)
{
	return (v%1000+1000)%1000;
}
void mul(int C[2][2],int _A[2][2],int _B[2][2])
{
	int A[2][2],B[2][2];
	for (int i=0;i<2;i++) for (int j=0;j<2;j++) A[i][j]=_A[i][j];
	for (int i=0;i<2;i++) for (int j=0;j<2;j++) B[i][j]=_B[i][j];
	for (int i=0;i<2;i++) for (int j=0;j<2;j++) C[i][j]=0;
	for (int i=0;i<2;i++) for (int j=0;j<2;j++) 
		for (int k=0;k<2;k++) C[i][j]=check(C[i][j]+A[i][k]*B[k][j]);
}
void solve(int depth,int C[2][2])
{
	if (depth==0)
	{
		C[0][0]=C[1][1]=1;
		C[0][1]=C[1][0]=0;
		return;
	}
	if (depth%2==0)
	{
		solve(depth/2,C);
		mul(C,C,C);
	}
	else
	{
		solve(depth-1,C);
		int A[2][2];
		A[0][0]=0;
		A[0][1]=1;
		A[1][0]=check(-4);
		A[1][1]=6;
		mul(C,C,A);
	}
}

int G[]={
2,27,
3,143,
4,751,
5,935,
6,607,
7,903,
8,991,
9,335,
10,47,
11,943,
12,471,
13,55,
14,447,
15,463,
16,991,
17,95,
18,607,
19,263,
20,151,
21,855,
22,527,
23,743,
24,351,
25,135,
26,407,
27,903,
28,791,
29,135,
30,647};


int main()
{
//	freopen("..\\input.txt","r",stdin);
//	freopen("..\\C-small-attempt0.in","r",stdin);
//	freopen("..\\tmp.txt","w",stdout);
//	freopen("..\\C-small-attempt0.out","w",stdout);
	freopen("..\\C-large.in","r",stdin);
	freopen("..\\C-large.out","w",stdout);
	int A[2][2];

	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		int n;
		scanf("%d",&n);
		int result;
		if (n<100)
			n=n;
		if (n==2)
			result=27;
		else if (n==3)
			result=143;
		else if (n==4)
			result=751;
		else
		{
			int C[2][2];
			solve(n-1,C);
			result=check(2*C[1][0]+6*C[1][1])-1;
		}
		printf("Case #%d: %03d\n",caseId,result);
	}
	return 0;
}

//ENDSOURCECODE_BY_ACRUSH_TOPCODER
