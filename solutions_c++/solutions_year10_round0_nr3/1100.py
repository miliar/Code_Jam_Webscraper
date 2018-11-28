#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#define maxSize 10003
#define LL long long

LL num[maxSize];
LL tmpNum[maxSize];
LL sumAcc[maxSize];
int posNum[maxSize];
LL r,k;
int n;

//large 
void getAC()
{
	memset(posNum,-1,sizeof(posNum));
	memset(tmpNum,0,sizeof(tmpNum));
	LL sum = 0;
	int cycleLength = 0;
	//first find the cycle
	posNum[0] = 0;
	sumAcc[0] = 0;
	int pos = -1;
	int start = 0;
	int count = 0;
	int cycle = 0;
	LL cycleSum = 0;
	while(true)
	{
		LL tmpSum = 0;
		int cnt = 0;
		bool same = true;
		LL tmpK = 0;
		count ++;
		for(;cnt<n;cnt++)
		{
			if(num[(start+cnt)%n]+tmpK>k)
			{
				same = false;
				break;
			}
			else 
			{
				tmpK +=num[(start+cnt)%n];
				tmpSum += num[(start+cnt)%n];
			}
		}
		if(same==true)
			cnt++;//表示这次要移几位
		start = (start+cnt)%n;
		if(posNum[start]!=-1)
		{
			cycle = count - posNum[start];
			sumAcc[count] = sumAcc[count-1] + tmpSum;
			cycleSum = sumAcc[count] - sumAcc[posNum[start]];
			pos = posNum[start];
			break;
		}
		else
		{
			sumAcc[count] = sumAcc[count-1] + tmpSum;
			posNum[start] = count;
		}
	}
	if(r<=count)
		printf("%I64d\n",sumAcc[r]);
	else
	{
		LL totalSum = sumAcc[pos];
		LL rr = r;
		rr -=pos;
		totalSum += (rr/cycle)*cycleSum;
		totalSum += sumAcc[pos+(rr%cycle)] - sumAcc[pos];
		printf("%I64d\n",totalSum);
	}
}
int main()
{
	freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);	
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("C-a.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		cin >> r >> k >> n;
		for(int j=0;j<n;j++)
		{
			scanf("%I64d",&num[j]);
		}
		printf("Case #%d: ",i);
		getAC();
	}
	return 0;
}
// small
//int num[maxSize];
//int tmpNum[maxSize];
//int r,k,n;
//void getAC()
//{
//	int sum = 0;
//	for(int i=1;i<=r;i++)
//	{
//		int j=0;
//		int tmpK = 0;
//		bool same = true;
//		for(j=0;j<n;j++)
//		{
//			if(tmpK+num[j]>k)
//			{
//				same = false;
//				break;
//			}
//			else
//			{
//				sum +=num[j];
//				tmpK += num[j];
//			}
//		}
//		int tt;
//		if(same==true)
//			tt = n-1;
//		else tt = j-1;
//		for(int m=0;m<n;m++)
//		{
//			num[m] = tmpNum[(tt+m+1)%n];
//		}
//		for(int m=0;m<n;m++)
//			tmpNum[m] = num[m];
//	}
//	printf("%d\n",sum);
//}
//int main()
//{
//	//freopen("C-large.in","r",stdin);
//    //freopen("C-large.out","w",stdout);
//	freopen("C-small-attempt0.in","r",stdin);
//	freopen("C-small-attempt0.out","w",stdout);
//	int t;
//	cin >> t;
//	for(int i=1;i<=t;i++)
//	{
//		cin >> r >> k >> n;
//		for(int j=0;j<n;j++)
//		{
//			scanf("%d",&num[j]);
//			tmpNum[j] = num[j];
//		}
//		printf("Case #%d: ",i);
//		getAC();
//	}
//	return 0;
//}