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
map<int,double> memory;


ll Chose(int all,int c)
{
	if(c > all)
		return 0;
	ll res = 1;
	for (int i = 0;i<c;i++)
	{
		res*=all;
		all--;
	}
	for (int i = c;i>1;i--)
	{
		res/=i;
	}
	return res;
}

double dp(int have,int all,int once)
{
	if(have == all)
		return 0;
	if(memory.count(have)>0)
		return memory[have];
	ll allChose = Chose(all,once);
	double haveP = (double)(Chose(have,once))/allChose;
	double y = 0;
	double res = 0;
	for(int i = 1;i+have<=all&&i<=once;i++)
	{
		double p = (double)(Chose(all-have,i)*Chose(have,once-i))/allChose;
		y+=p*dp(have+i,all,once);
	}
	res =  (y+1)/(1-haveP);
	memory[have] = res;
	return res;
}

int main()
{
	freopen("F:\\code\\topcoder\\compete\\compete\\C-small-attempt0.in","r",stdin);
	freopen("F:\\code\\topcoder\\compete\\compete\\test1.out","w",stdout);
	int testCase;
	cin >> testCase;
	double res;
	getchar();
	for (int caseNum = 1;caseNum<=testCase;caseNum++)
	{
		memory.clear();
		int all,once;
		cin >> all;
		cin >> once;
		res = dp(0,all,once);
		cout << "Case #"+ToString(caseNum)+": "+ToString(res)<<endl;
	}
}
