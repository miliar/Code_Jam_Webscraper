#include <iostream>
#include <stdio.h>
#include <set>
#include <list>
#include <algorithm>

using namespace std;


int main()
{
	int nTestCases;
	int nCols;
	list<int> row1;
	list<int> row2;
	long long result;
	int num;

	scanf("%d", &nTestCases);

	for (int i=1;i<=nTestCases;++i)
	{
		scanf("%d", &nCols);

		row1.clear();
		row2.clear();
		for (int j=1;j<=nCols;++j)
		{
			scanf("%d", &num);
			row1.push_back(num);
		}
		for (int j=1;j<=nCols;++j)
		{
			scanf("%d", &num);
			row2.push_back(num);
		}

		result = 0;

		row1.sort();//sort(row1.begin(),row1.end());
		row2.sort();
		row2.reverse(); //reverse(row2.reverse.begin(), row2.end());

		list<int>::iterator iter1 = row1.begin();
		list<int>::iterator iter2 = row2.begin();
		//++iter2;
		while (iter1 != row1.end())
		{
			result += (*iter1) * (*iter2);
			++iter1;
			++iter2;
		}

		cout <<"Case #"<<i<<": "<<result<<"\n";

	}

	return 0;
}