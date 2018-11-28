#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <queue>
#include<iostream>
#define FALSE 0
#define TRUE 1
using namespace std;
typedef long long ll;
typedef pair<int,int> ipair;
#define SIZEARRAY(x) (sizeof(x)/sizeof(x[0]))

template <typename T>
string ToString(T var)
{
	ostringstream os;
	os << var;
	return os.str();
}

int main()
{

	freopen("F:\\code\\topcoder\\compete\\compete\\A-large (1).in","r",stdin);
	freopen("F:\\code\\topcoder\\compete\\compete\\test2.out","w",stdout);
	int testCase;
	cin >> testCase;
	for (int caseNum = 1;caseNum<=testCase;caseNum++)
	{
		int res = 0;
		int squa;
		cin >> squa;
		int square[50];
		int rowNum[50];
		memset(rowNum,0,sizeof(rowNum));
		for (int i = 0;i<squa;i++)
		{
			getchar();
			for (int j = 0;j<squa;j++)
			{
				char c = getchar();
				square[j] = c-'0';
			}
			for (int j = squa;j>0;j--)
			{
				if(square[j-1] == 1)
				{
					rowNum[i] = j;
					break;
				}
			}
		}
		for (int nowNum = 1;nowNum<=squa;nowNum++)
		{
			int addr;
			for (int j = nowNum-1;j<squa;j++)
			{
				if(rowNum[j]<=nowNum)
				{
					addr = j;
					break;
				}
			}
			res+=addr-nowNum+1;
			int tempNum = rowNum[addr];
			for (int j = addr;j>=nowNum;j--)
			{
				rowNum[j] = rowNum[j-1];
			}
			rowNum[nowNum-1] = tempNum;
		}
		cout << "Case #"<<ToString(caseNum)<<": "<<ToString(res)<<endl;
	}
}