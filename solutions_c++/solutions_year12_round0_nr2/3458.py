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
int N,S,P;
int t[100];
int ts[100];
int tps[100];
int tpns[100];
int tnpns[100];
int an(int tr,int inx)
{
	int pjs = tr/3-2;
	if (pjs< 0)pjs = 0;
	for (;pjs<=(tr/3+1) && pjs<=10;pjs++)
	{
		for (int j = pjs;j<=(tr/3+3) && j<= 10;j++)
		{
			for (int k=j;k<=(tr/3+3) && k<=10;k++)
			{
				if ((pjs+j+k) == tr)
				{
					if (k>= P)
					{
						if ((k-pjs) == 2)
						{
							tps[inx] = 1;
						}
						else if ((k-pjs) <= 1)
						{
							tpns[inx] = 1;
						}
					}
					else if (k < P)
					{
						if ((k-pjs) == 2)
						{
							ts[inx] = 1;
						}
						else if ((k-pjs) <= 1)
						{
							tnpns[inx] = 1;
						}
						
					}
				}
			}
		}
	}
	return 0;
}

int solve()
{
	int ret = 0;
	int rets = 0;
	int i;
	for (i=0;i<N;i++)
	{
		if (tpns[i] == 1)
		{
			ret++;t[i] = 1;
		}
	}
	if (rets == S)
	{
		return ret;
	}
	for (i=0;i<N;i++)
	{
		if (t[i]==0 && tps[i] == 1)
		{
			ret++;
			rets++;
			t[i] = 2;
		}
		if (rets==S)
		{
			break;
		}
	}
	if (rets == S)
	{
		return ret;
	}
	for (i=0;i<N;i++)
	{
		if (t[i] == 0&& ts[i] == 1)
		{
			rets++;
		}
		if (rets == S)
		{
			break;
		}
	}
	if (rets == S)
	{
		return ret;
	}
	for (i=0;i<N;i++)
	{
		if (t[i] == 1&& tps[i] == 1)
		{
			t[i] = 2;
			rets++;
		}
		if (rets == S)
		{
			break;
		}
	}
	if (rets == S)
	{
		return ret;
	}
	for (i=0;i<N;i++)
	{
		if (t[i] == 1&& ts[i] == 1)
		{
			t[i] = 0;
			ret--;
			rets++;
		}
		if (rets == S)
		{
			break;
		}
	}
	return ret;
	
}

int main()
{
	FILE *fp = NULL;
//	fp = freopen("B-test.in","r",stdin);
	fp = freopen("B-large (1).in","r",stdin);
//	fp = freopen("B-large.in","r",stdin);
	fp = freopen("B.out","w",stdout);

	int T;
	cin>>T;
	for (int caseId=1;caseId<=T;caseId++)
	{

		cin>>N;
		cin>>S;
		cin>>P;
		memset(t,0,sizeof t);
		memset(ts,0,sizeof ts);
		memset(tps,0,sizeof tps);
		memset(tpns,0,sizeof tpns);
		memset(tnpns,0,sizeof tnpns);
		int ts;
		for (int i=0;i<N;i++)
		{
			cin>>ts;
			an(ts,i);

		}
		
		cout<<"Case #"<<caseId<<": "<<solve()<<endl;
	}


	return 0;
}

