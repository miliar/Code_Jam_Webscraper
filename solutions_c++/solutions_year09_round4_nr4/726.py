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


struct node 
{
	double x;
	double y;
	double z;
};
int main()
{

	freopen("F:\\code\\topcoder\\compete\\compete\\D-small-attempt0.in","r",stdin);
	freopen("F:\\code\\topcoder\\compete\\compete\\test2.out","w",stdout);
	int testCase;
	cin >> testCase;
	node plants[50];

	for (int caseNum = 1;caseNum<=testCase;caseNum++)
	{
		int N;
		cin >> N;
		double res =1000000;
		for (int i=0;i<N;i++)
		{
			cin >> plants[i].x >> plants[i].y >> plants[i].z;
		}
		if(N == 1)
		{
			res =  plants[0].z;
		}
		else if(N == 2)
		{
			res =  max(plants[1].z,plants[0].z);
		}
		else
		{
			for (int i = 0;i<3;i++)
			{
				int j = (i+1)%3;
				int k = (i+2)%3;
				double dis = sqrt((plants[i].x-plants[j].x)*(plants[i].x-plants[j].x) +(plants[i].y-plants[j].y) *(plants[i].y-plants[j].y) );
				dis+=plants[i].z;
				dis+=plants[j].z;
				dis/=2;
				dis = max(plants[k].z,dis);
				res = min(res,dis);
			}
		}
		cout << "Case #"<<ToString(caseNum)<<": "<<ToString(res)<<endl;
	}
}