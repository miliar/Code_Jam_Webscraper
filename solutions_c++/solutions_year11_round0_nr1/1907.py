#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, N, count = 0;
	vector <int> O, OO, B, BB;
	scanf("%d", &T);
	while (T--)
	{
		printf("Case #%d: ", ++count);
		scanf("%d", &N);
		O.clear();
		OO.clear();
		B.clear();
		BB.clear();
		int temp = 0;
		while (N--)
		{
			temp += 1;
			char str[11];
			int num;
			scanf("%s", str);
			scanf("%d", &num);
			if (str[0] == 'O')
			{
				O.push_back(num);
				OO.push_back(temp);
			}
			else
			{
				B.push_back(num);
				BB.push_back(temp);
			}
		}
		int res = 0;
		int op = 0, bp = 0;
		int poso = 1, posb = 1;
		temp = 1;
		while (op < O.size() || bp < B.size())
		{
			int flag = 0;
			if (op < O.size())
			{
				if (poso == O[op])
				{
					if (temp == OO[op])
					{
						flag = 1;
						++op;
						++temp;
					}
				}
				else
				{
					if (poso < O[op])
					{
						++poso;
					}
					else
					{
						--poso;
					}
				}
			}
			if (bp < B.size())
			{
				if (posb == B[bp])
				{
					if (temp == BB[bp] && flag == 0)
					{
						++bp;
						++temp;
					}
				}
				else
				{
					if (posb < B[bp])
					{
						++posb;
					}
					else
					{
						--posb;
					}
				}
			}
			res += 1;
		}
		printf("%d\n", res);
	}
	return 0;
}
