#include <iostream>
#include <vector>
#include <deque>
#include <map>
#include <cstdio>
using namespace std;
const int MC=20;

void patricSum(const deque<int>& lhs, deque<int>& out);
void getBinary(int n, deque<int>& out);
int getDec(deque<int>& in);

int main()
{
	deque<int> pnum[1001];
	int T; scanf("%d", &T);
	for(int tcase=1; tcase<=T; ++tcase)
	{
		int n; scanf("%d", &n);
		vector<int> num(n,0);
		for(int i=0; i < n; ++i)
			scanf("%d", &num[i]);
		for(int i=0; i < n; ++i)
			getBinary(num[i], pnum[i]);
		
		int sol=-1;
		for(int i=0; i <= (1<<n)-1; ++i)
		{
			vector<int> patric, sean;
			for(int j=0; j < n; ++j){
				if(i&(1<<j)) patric.push_back(j);
				else sean.push_back(j);
			}
			if(sean.empty()||patric.empty())
				continue;
			/*for(int i=0; i < (int)sean.size(); ++i)
				printf("%d ", sean[i]);
			printf("\n");
			for(int i=0; i < (int)patric.size(); ++i)
				printf("%d ", patric[i]);
			printf("\n");*/

			deque<int> add1=pnum[sean[0]];
			deque<int> add2=pnum[patric[0]];
			for(int i=1; i < (int)sean.size(); ++i)
				patricSum(pnum[sean[i]], add1);
			for(int i=1; i < (int)patric.size(); ++i)
				patricSum(pnum[patric[i]], add2);
			int num1 = getDec(add1);
			int num2 = getDec(add2);
			if( num1==num2 )
			{
				int sum=0;
				for(int i=0; i < (int)sean.size(); ++i)
					sum += num[ sean[i] ];
				sol = max(sum,sol);
			}
		}
		if(sol==-1)
			printf("Case #%d: NO\n", tcase);
		else
			printf("Case #%d: %d\n", tcase, sol);
	}
	return 0;	
}

void patricSum(const deque<int>& lhs, deque<int>& out)
{
	for(int i=0; i < MC; ++i)
	{
		if(out[i] && lhs[i])
			out[i]=0;
		else if(out[i] || lhs[i])
			out[i]=1;
	}
}

void getBinary(int n, deque<int>& out)
{
	out.clear();
	int ret = 0;
	for(int i=0; i < MC; ++i)
	{
		if( n&(1<<i) )
			out.push_front(1);
		else
			out.push_front(0);
	}
}

int getDec(deque<int>& in)
{
	int s=0;
	int ret=0;
	for(int i=MC-1; i > -1; --i, ++s)
	{
		if( in[i] )
			ret += (1<<s);
	}
	return ret;
}

