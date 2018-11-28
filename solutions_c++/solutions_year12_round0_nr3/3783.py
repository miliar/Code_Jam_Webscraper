/*
 * B.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: B2lawa
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>

using namespace std;
bool vis [2000001];
int A,B,cnt=0,len;
set <int> S;
int arr[]={1,10,100,1000,10000,100000,1000000,10000000};
void make(int n)
{
	int div=10,mul=arr[len-1],nel;
	S.clear();
	S.insert(n);
	while(div!=arr[len])
	{
		nel=n%div;
		nel*=mul;
		nel+=(n/div);
		//cout<<nel<<endl;
		if(nel >=A && nel<=B)
		{
			S.insert(nel);
			vis[nel]=1;
		}
		div*=10;
		mul/=10;
	}
	//cout<<"E"<<endl;
	int sz=S.size();
	if(sz>1)
	{
		cnt+=((sz*(sz-1))/2);
	}
}
int main()
{
	freopen("in.in","rt",stdin);
	freopen("out.out","wt",stdout);
	int t,id=1,cp;
	scanf("%d",&t);
	while(t--)
	{
		memset(vis,0,sizeof(vis));
		cnt=0;
		len=0;
		scanf("%d%d",&A,&B);
		cp=A;
		while(cp)
			len++,cp/=10;
		for(int i=A;i<=B;++i)
		{
			if(!vis[i])
				make(i);
		}
		printf("Case #%d: %d\n",id++,cnt);

	}
}
