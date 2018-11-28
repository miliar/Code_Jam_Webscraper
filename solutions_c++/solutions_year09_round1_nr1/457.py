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

bool IsGood(int num,int baseNumIndex);
template <typename T>
string ToString(T var)
{
	ostringstream os;
	os << var;
	return os.str();
}

vector<int>baseNumArr;
map<int,int>memory[10];
vector<string>& splitc(const string&s,vector<string>& vs,const string &seps=" ")
{
	string::size_type i,j;
	for (i = 0;(j = s.find_first_of(seps,i))!=string::npos;i = j+1)
	{
		vs.push_back(string(s,i,j-i));
	}
	vs.push_back(string(s,i,j));
	return vs;
}
template <typename T> 
T parse(const string &ts)
{
	T r;
	istringstream iss(ts);
	if(!(iss>>r))
		throw "Type conversion failed";
	return r;
}
int main()
{
	freopen("F:\\code\\topcoder\\compete\\compete\\A-small-attempt0.in","r",stdin);
	freopen("F:\\code\\topcoder\\compete\\compete\\test1.out","w",stdout);
	int testCase;
	cin>>testCase;
	getchar();
	for (int caseNum = 1;caseNum<=testCase;caseNum++)
	{
		baseNumArr.clear();
		for (int i = 0;i<10;i++)
		{
			memory[i].clear();
		}
		string line;
		int  res;
		getline(cin,line);
		vector<string> midGroup;
		splitc(line,midGroup);
		for (int i = 0;i<midGroup.size();i++)
		{
			int tempBase = parse<int>(midGroup[i]);
			baseNumArr.push_back(tempBase);
		}
		for(int num = 2;;num++)
		{
			int baseNumIndex = 0;
			for (baseNumIndex = 0;baseNumIndex<baseNumArr.size();baseNumIndex++)
			{
				if(!IsGood(num,baseNumIndex))
				{
					break;
				}
			}
			if(baseNumIndex == baseNumArr.size())
			{
				res = num;
				break;
			}
		}
		cout << "Case #"+ToString(caseNum)+": "+ToString(res)<<endl;
	}
}

bool IsGood(int num,int baseNumIndex)
{
	int oldNum = num;
	if(num == 1)
		return 1;
	if (memory[baseNumIndex].count(num)>0)
	{
		return memory[baseNumIndex][num];
	}
	memory[baseNumIndex][oldNum] = 0;
	vector<int> numArr;
	while(num)
	{
		numArr.push_back(num%baseNumArr[baseNumIndex]);
		num/=baseNumArr[baseNumIndex];
	}
	int resNum = 0;
	for (int i = 0;i<numArr.size();i++)
	{
		resNum+=numArr[i]*numArr[i];
	}
	memory[baseNumIndex][oldNum] =  IsGood(resNum,baseNumIndex);
	return memory[baseNumIndex][oldNum];
}