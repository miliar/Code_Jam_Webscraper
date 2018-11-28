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
#define MAXD 5001

using namespace std;
stringstream stream;
int sum=0;
string dic[MAXD];
string que;    
int L=0,D=0,N=0;
                                              
void dfs(string cur,int curIndex)
{
	int i=0;
	int length=cur.size();
	for(i=0;i<D;i++)
	{
		if(dic[i].substr(0,length)==cur)
			break;
	}
	if(i>=D)return;
	if(length==L)
	{
		sum++;
		return ;
	}
	
	

	if(que[curIndex]!='(')
	{
		cur=cur+que.substr(curIndex,1);
		dfs(cur,curIndex+1);
	}
	else
	{
		curIndex++;
		int nextIndex=curIndex;
		while(que[nextIndex]!=')')
			nextIndex++;

		for(i=curIndex;i<nextIndex;i++)
		{
			dfs(cur+que.substr(i,1),nextIndex+1);
		}
	}
	return ;
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	int Case=0;
	int i=0,j=0;
	string s;


	getline(cin,s);
	stream<<s;
	stream>>L>>D>>N;

	for(i=0;i<D;i++)
	{
		getline(cin,dic[i]);
	}

	while(Case<N)
	{

		sum=0;

		getline(cin,que);

		dfs("",0);

		Case++;
		cout<<"Case #"<<Case<<": "<<sum<<endl;
	}
	return 0;
}