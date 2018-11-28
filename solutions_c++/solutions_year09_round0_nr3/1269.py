#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define FOR(i,n) for( i = 0 ; i<n ; i++)
#define RFOR(i,a,b)  for( i = a ; i<b ; i++)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))
#define i64 __int64
int sto[503][25];
string a,b;
int cal(int i , int j)
{
	if(sto[i][j]!=-1)	return sto[i][j];
	if(j >= 19)	return sto[i][j] = 1;
	if(i>=a.size())	return sto[i][j] = 0;
	int k,res = 0;
	for(k = i;k<a.size();k++)
		if(a[k] == b[j])
			res = (res+cal(k+1,j+1))%10000;
	return sto[i][j] = res;
}
int main()
{
	//freopen("C.in","r",stdin);
	//freopen("C.out","w",stdout);
	b = "welcome to code jam";
	char p[10001];
	int N, fg = 1;
	cin>>N;
	getchar();
	while(N--)
	{
		MCLR(sto);
		gets(p);
		a = p;
		int res = cal(0,0);
		printf("Case #%d: %04d\n",fg++,res);
	}
	return 0;
}