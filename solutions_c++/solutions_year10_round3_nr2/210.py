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
#include <fstream>
#define FALSE 0
#define TRUE 1
using namespace std;
typedef long long ll;
typedef pair<int,int> ipair;
#define SIZEARRAY(x) (sizeof(x)/sizeof(x[0]))

const ll maxnum = 1000000000LL;

int main()
{
	ll data[30];
	fstream fin,fout;
	fin.open("D:\\coding\\codejam2010_round1\\codejam2010_round1\\B-large.in",ios_base::in);
	fout.open("D:\\coding\\codejam2010_round1\\codejam2010_round1\\B-large.out",ios_base::out);
	int caseNum;
	fin>>caseNum;
	int caseIndex = 1;
	while(caseIndex<=caseNum)
	{
		ll l,p,C;
		fin>>l>>p>>C;
		ll tempData = C;
		int tempIndex = 0;
		while (tempData<maxnum)
		{
			data[tempIndex++] = tempData;
			tempData *= tempData;
		}
		data[tempIndex++] = tempData;
		int res = 0;
		for (int i = 0;i<30;i++)
		{
			if (data[i]*l>=p)
			{
				res = i;
				break;
			}
		}
		fout << "Case #"<<caseIndex<<": "<<res<<endl;
		caseIndex++;
	}
}