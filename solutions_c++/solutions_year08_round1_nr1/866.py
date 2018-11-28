#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <math.h>
#include <iomanip>
#include <algorithm>

using namespace std;

long g_minCost;

void driveCase()
{
	long vecSize;
	cin>>vecSize;
	vector<long> xArr, yArr;
	for(long i=0; i<vecSize; i++)
	{
		long d;
		cin>>d;
		xArr.push_back(d);
	}
	for(long i=0; i<vecSize; i++)
	{
		long d;
		cin>>d;
		yArr.push_back(d);
	}
	sort(xArr.begin(), xArr.end());
	sort(yArr.begin(), yArr.end());
	g_minCost = 0;
	for(int i=0; i<vecSize; i++)
	{
		g_minCost+= xArr[i]*yArr[vecSize-i-1];
	}
}

int main()
{
    int caseCount;
    cin>>caseCount;
    vector<long> costVec;
    for(int i=0;i<caseCount; i++)
    {
        driveCase();
        costVec.push_back(g_minCost);
    }
    //cout.setf(ios_base::fixed, ios_base::floatfield);
    //cout.setf(ios_base::showpoint);
    //cout.precision(7);
    for(int i=1; i<=caseCount; i++)
    {
        cout<<"Case #"<<i<<": "<<costVec[i-1]<<endl;
    }
    return 0;
}
