#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
#include <memory.h>
#include <assert.h>
using namespace std;

vector<int>	intVec;


char tmpbuf[20];

int RightShift( int a, int len)
{
	int res;
	int base=1;
	for (unsigned int i=0;i < (len-1);i++)
	{
		base*=10;
	}
	res = a/10 + (a%10)*base;
	return res;
}

bool CheckExist(int a)
{
	for (unsigned int i=0;i < intVec.size();i++)
	{
		if (a == intVec[i])
		{
			return true;
		}
	}
	return false;
}



int main(void)
{
	freopen("C-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int nTest;
	int small, big;
	int res;
	intVec.reserve  (20);
	scanf("%d", &nTest);

	for (int i = 0; i < nTest ; i++)
	{
		res = 0;
		scanf("%d %d", &small, &big);
		if (big >=10)
		{
			for ( int j=small;j <=big ;j++)
			{
				itoa(j, tmpbuf, 10);
				string tmpstr(tmpbuf);
				int len = tmpstr.length  ();
				int tmpInt = j;
				intVec.clear  ();
				for ( int k=0;k < (len-1);k++)
				{
					tmpInt = RightShift  (tmpInt, len);
					
					if (tmpInt>small && tmpInt <=big && tmpInt>j)
					{
						
						if (!CheckExist  (tmpInt))
						{						
							intVec.push_back(tmpInt);
							res++;
						//printf("pair  %d  %d\n", tmpInt, j);
						}

					}
				}
			}
		}
		printf("Case #%d: %d\n", i+1, res);

	}



	return 1;
}