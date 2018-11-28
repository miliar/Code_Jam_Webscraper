#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
using namespace std;
#define ONLINEJUDGE
int iLastVal;

vector<int> v, v1, v2;

int main()
{
	int iCaseTimes;
	long long iRet;
	string str;

#ifdef ONLINEJUDGE
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
#endif

	scanf("%d", &iCaseTimes);
	for(int k = 1; k <= iCaseTimes; k++)
	{
		scanf("%d", &iLastVal);
		v.clear();
		stringstream ss;
		ss << iLastVal;
		ss >> str;

		for(int i = 0; i < str.length(); i++)
		{
			v.push_back(str[i] - '0');
		}
		
		v1.clear();
		v1 = v;
		while(1)
		{
			next_permutation(v1.begin(), v1.end());
			iRet = 0;
			for(int i = 0; i < v1.size(); i++)
			{
				iRet = iRet * 10 + v1[i];
			}
			v1.clear();
			if(iRet <= iLastVal)
			{
				v1.push_back(0);
				for(int j = 0; j < v.size(); j++)
				{
					v1.push_back(v[j]);
				}
			}
			else break;

		}
		
		printf("Case #%d: %ld\n", k, iRet); 
		
	}
	return 0;
}