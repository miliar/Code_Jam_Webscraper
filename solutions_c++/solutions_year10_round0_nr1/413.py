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


int main()
{
	freopen("F:\\code\\topcoder\\A-large.in","r",stdin);
	freopen("F:\\code\\topcoder\\testout.txt","w",stdout);
	int testCase;
	cin>>testCase;
	for (int i = 0;i<testCase;i++)
	{
		int N,K;
		cin>>N>>K;
		int alls = 1<<N;
		K%=alls;
		cout << "Case #"<<i+1<<": ";
		if (K == alls -1)
		{
			cout<<"ON"<<endl;
		}
		else
		{
			cout <<"OFF"<<endl;
		}
	}
}