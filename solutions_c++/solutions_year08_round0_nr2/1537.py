#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int toTime(string str);

int main(void)
{
	int t,i,no=0;
	int turnard;
	int na,nb;
	vector<int> depA,depB,arrA,arrB;
	string str;
	
	cin >> t;
	while (t--)
	{
		cin >> turnard;
		cin >> na >> nb;

		for (i=0; i<na; i++)
		{
			cin >> str;
			depA.push_back(toTime(str));
			cin >> str;
			arrA.push_back(toTime(str)+turnard);
		}

		for (i=0; i<nb; i++)
		{
			cin >> str;
			depB.push_back(toTime(str));
			cin >> str;
			arrB.push_back(toTime(str)+turnard);
		}
		
		sort(depA.begin(),depA.end());
		sort(depB.begin(),depB.end());
		sort(arrA.begin(),arrA.end());
		sort(arrB.begin(),arrB.end());

		vector<int>::iterator iter1,iter2;
		int cur,max;

		iter1=depA.begin();
		iter2=arrB.begin();
		cur=0;
		max=0;
		while (iter1!=depA.end() || iter2!=arrB.end())
		{
			if (iter1==depA.end())
			{
				cur++;
				iter2++;
			}
			else if (iter2==arrB.end())
			{
				if (!cur)
					max++;
				else
					cur--;
				iter1++;
			}
			else
			{
				if (*iter1 < *iter2)
				{
					if (!cur)
						max++;
					else
						cur--;
					iter1++;
				}
				else
				{
					cur++;
					iter2++;
				}
			}
		}
		cout << "Case #" << ++no << ": " << max << " ";


		iter1=depB.begin();
		iter2=arrA.begin();
		cur=0;
		max=0;
		while (iter1!=depB.end() || iter2!=arrA.end())
		{
			if (iter1==depB.end())
			{
				cur++;
				iter2++;
			}
			else if (iter2==arrA.end())
			{
				if (!cur)
					max++;
				else
					cur--;
				iter1++;
			}
			else
			{
				if (*iter1 < *iter2)
				{
					if (!cur)
						max++;
					else
						cur--;
					iter1++;
				}
				else
				{
					cur++;
					iter2++;
				}
			}
		}
		cout << max << endl;

		depA.clear();
		depB.clear();
		arrA.clear();
		arrB.clear();
	}

	cin >> t;

	return 0;
}

int toTime(string str)
{
	int ret=0,tmp=0;
	ret=str[0]-'0';
	ret*=10;
	ret+=str[1]-'0';
	ret*=60;

	tmp=str[3]-'0';
	tmp*=10;
	tmp+=str[4]-'0';
	ret+=tmp;

	return ret;
}