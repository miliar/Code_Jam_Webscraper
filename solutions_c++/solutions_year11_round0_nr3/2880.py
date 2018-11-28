/*
ID: zhengmi1
PROG: Bot Trust
LANG: C++
*/

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
#include <fstream>
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
#include <string.h>

using namespace std;

#define max(a,b) (((a) > (b)) ? (a) : (b))
#define min(a,b) (((a) < (b)) ? (a) : (b))


inline int sum(int& a,int& b)
{
	return a^b;
}

int N;
int dat[1005];
int dp[1005][1005][2];

int main(int argc,char **args)
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	int cas;

	cin>>cas;
	int CAS;
	int i,j;
	int rlt=-1;

	for (CAS=1;CAS<=cas;CAS++)
	{
		cout<<"Case #"<<CAS<<":"<<" ";
		rlt=-1;

		cin>>N;
		for (i=0;i<N;i++)
			cin>>dat[i];

		int K=1<<N;

		for (i=1;i<K-1;i++)
		{
			int sum1=0,sum2=0;
			int realsum1=0,realsum2=0;
			

			for (j=0;j<N;j++)
			{
				if (((i>>j)&1)==1)
				{
					sum1=sum(sum1,dat[j]);
					realsum1+=dat[j];
				}
				else
				{
					sum2=sum(sum2,dat[j]);
					realsum2+=dat[j];
				}
			}

			if (sum1==sum2)
			{
				if (max(realsum1,realsum2)>rlt)
					rlt=max(realsum1,realsum2);
			}

		}

		if (rlt==-1)
			cout<<"NO"<<endl;
		else
			cout<<rlt<<endl;




	}

	return 0;
}



