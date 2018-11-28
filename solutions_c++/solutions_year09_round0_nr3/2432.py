#include <cstdio>
#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;
string strIn = "" ;
const string strFormat = "welcome to code jam";
int nCount;
void dfs(int nFormatPos, int nstrInPos)
{
	if (nFormatPos == strFormat.size())
	{
		nCount ++;
		return;
	}
	if (nstrInPos == strIn.size())
	{
		return;
	}
	if (strFormat[nFormatPos] == strIn[nstrInPos])
	{
		dfs(nFormatPos +1, nstrInPos + 1);
	}
	dfs(nFormatPos , nstrInPos + 1);
}
int main(int argc , char ** argv)
{	
 	//freopen("in.txt","r",stdin);
 	//freopen("out.txt","w",stdout);
	int N;
	scanf("%d\n",&N);
	unsigned int i;
	
	for ( i = 1; i <= N; ++i)
	{
		strIn = "";
		nCount = 0;
		getline(cin,strIn);
		dfs(0,0);
		printf("Case #%d: %04d\n",i,nCount);
	}
	return 0;
}