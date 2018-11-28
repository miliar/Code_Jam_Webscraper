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
#include <stdio.h>
#include <string.h>

int numbers[105][105];
int k;
bool checkLine(int lineNum)
{
	int diff = (lineNum+1)%2;
	int leftNum = (lineNum+1)/2-1;
	int rightNum = leftNum+diff+1;
	for (int i = k-1;i>=0;i--)
	{
		int width = min(i+1,2*k-1-i);
		for (int j = 0;j<min(leftNum+1,width-rightNum);j++)
		{
			if (numbers[i][leftNum-j]!= numbers[i][rightNum+j])
			{
				return FALSE;
			}
		}
		diff = 1-diff;
		leftNum-=diff;
		rightNum = leftNum+diff+1;
	}
	diff = (lineNum+1)%2;
	leftNum = (lineNum+1)/2-1;
	rightNum = leftNum+diff+1;
	for (int i = k-1;i<2*k-1;i++)
	{
		int width = min(i+1,2*k-1-i);
		for (int j = 0;j<min(leftNum+1,width-rightNum);j++)
		{
			if (numbers[i][leftNum-j]!= numbers[i][rightNum+j])
			{
				return FALSE;
			}
		}
		diff = 1-diff;
		leftNum-=diff;
		rightNum = leftNum+diff+1;
	}
	return TRUE;
}

bool checkRow(int rowNum)
{
	int rows = min(rowNum,2*k-2-rowNum);
	int base = 0;
	if (rowNum<=k-1)
	{
		for (int i = 0;i<rows;i++)
		{
			int width = rows-i;
			if (rowNum+i+1<k)
			{
				base++;
			}
			for (int j = 0;j<width;j++)
			{
				if (numbers[rowNum-i-1][j] != numbers[rowNum+i+1][base+j])
				{
					return FALSE;
				}
			}
		}
	}
	else
	{
		for (int i = 0;i<rows;i++)
		{
			if (rowNum-i-1>=k-1)
			{
				base++;
			}
			int width = rows-i;
			for (int j = 0;j<width;j++)
			{
				if (numbers[rowNum-i-1][base+j] != numbers[rowNum+i+1][j])
				{
					return FALSE;
				}
			}
		}
	}
	return TRUE;
}



int main()
{
	freopen("F:\\code\\topcoder\\A-large (2).in","r",stdin);
	freopen("F:\\code\\topcoder\\compete\\compete\\test2.out","w",stdout);
	int caseNum;
	int caseIndex = 1;
	cin>>caseNum;
	while(caseIndex<=caseNum)
	{
		cin>>k;
		for (int i = 0;i<2*k-1;i++)
		{
			int width = min(i+1,2*k-1-i);
			for (int j = 0;j<width;j++)
			{
				scanf("%d",&(numbers[i][j]));
			}
		}
		int rowNum,colNum;
		for (int i = 0;i<k;i++)
		{
			if (checkRow(k-1+i))
			{
				rowNum = i;
				break;
			}
			if (checkRow(k-1-i))
			{
				rowNum = i;
				break;
			}
		}
		for (int j = 0;j<k;j++)
		{
			if (checkLine(k-1-j))
			{
				colNum = k-j-1;
				break;
			}
			if (checkLine(k+j-1))
			{
				colNum = k+j-1;
				break;
			}
		}
		int baseNum;
		if (colNum%2 == 0)
		{
			baseNum = max(colNum/2,k-1-colNum/2);
			baseNum*=2;
			baseNum++;
		}
		else
		{
			baseNum = max((colNum+1)/2,k-(colNum+1)/2);
			baseNum*=2;
		}
		baseNum+=rowNum;
		cout<<"Case #"<<caseIndex<<": ";
		cout<<baseNum*baseNum-k*k<<endl;
		caseIndex++;
	}
}



