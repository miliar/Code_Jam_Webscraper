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

string query[1001],searcheng[101];

int S,Q;

int mem[1001][101];
int cal(int qindex,int curs)
{
	if(mem[qindex][curs]!=-1) return mem[qindex][curs];
	if(qindex==Q) return 0;
	int ret=1000000;
	if(query[qindex]!=searcheng[curs])
		ret=min(ret,cal(qindex+1,curs));
	else
	{
		for(int i=0;i<S;i++)
		{
			if(i!=curs)
			{
				ret=min(ret,cal(qindex,i)+1);
			}
		}
	}
	 return mem[qindex][curs]=ret;
}

int main()
{
	FILE *fp,*fw;
	fp=fopen("A-large.in","r");
	fw=fopen("output.txt","w");
	int count,N,i;
	fscanf(fp,"%d\n",&N);
	for(count=1;count<=N;count++)
	{
		memset(mem,-1,sizeof(mem));
		char ch[101];
		fscanf(fp,"%d\n",&S);
		for(i=0;i<S;i++)
		{
			fscanf(fp," %[^\n]",ch);
			int x=strlen(ch);
			string s(ch,ch+x);
			searcheng[i]=s;
		}
		fscanf(fp,"%d\n",&Q);
		for(i=0;i<Q;i++)
		{
			fscanf(fp," %[^\n]",ch);
			int x=strlen(ch);
			string s(ch,ch+x);
			query[i]=s;
		}
		int ans=1000000;
		for(i=0;i<S;i++)
			ans=min(ans,cal(0,i));
		fprintf(fw,"Case #%d: %d\n",count,ans);
	}
	return 0;

}




 