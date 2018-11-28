#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define ONLINEJUDGE

set<char> s;
int iBase;
int R[2][30];
int iCurVal;

vector<int> v;
int Store(char c)
{
	int iIndex1, iIndex2;

	if(c <= '9' && c >= '0')
	{
		iIndex1 = 0;
		iIndex2 = c - '0';
	}
	if(c <= 'z' && c >= 'a')
	{
		iIndex1 = 1;
		iIndex2 = c - 'a';
	}
	if(R[iIndex1][iIndex2] != -1) return R[iIndex1][iIndex2];
	
	R[iIndex1][iIndex2] = v[iCurVal++];
	return R[iIndex1][iIndex2];
}

int main()
{
#ifdef ONLINEJUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif

	int iCaseTimes, i, j;
	string str;

	scanf("%d", &iCaseTimes);
	for(int k = 0; k < iCaseTimes; k++)
	{
		printf("Case #%d: ", k + 1);
		cin >> str;
		s.clear();
		for(i = 0; i < str.length(); i++)
		{
			s.insert(str[i]);
		}
		iBase = s.size();
		if(iBase == 1) iBase = 2;

		memset(R, -1, sizeof(R));

		v.clear();
		v.push_back(1);
		long long iRet;
		iRet = 0;

		
		if(str.length() > 1)
			v.push_back(0);
		for(i = 2; i < iBase; i++)
			v.push_back(i);


		

			
			iCurVal = 0;
			for(i = 0; i < str.length(); i++)
			{
				//cout << Store(str[i]) << endl;
				iRet = iRet * iBase + Store(str[i]);
			}
		printf("%lld\n", iRet);

	}	
	return 0;
}