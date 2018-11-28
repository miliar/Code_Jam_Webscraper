#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>

#define LL long long
#define LD long double
#define pi 3.1415926535897932384626433
#define sqr(a) ((a)*(a))

using namespace std;

int T;

int size; //current size,globle var
int mFactor; // 

int maxtry(int value){
	int i = 1;
	size = 1;
	while(value/i>=10){
		i *= 10;
		size ++;
	}
	mFactor = i;
	
	return (value / i + 1) * i;
}

long long paircount(int a,int b){
	long long ans = 0;
	set<int> hasCounted;
	maxtry(a);
	for (int num=a; num<b;num++)
	{
		if (hasCounted.count(num)!=0)
			continue;
		int count = 1;
		int factor = mFactor;
		int factorTail = 10;
		for (int i=1;i<size;i++)
		{
			int newNum = num/factor+(num%factor)*factorTail;
			
			
			if (num<newNum && newNum>=a && newNum<=b && hasCounted.count(newNum)==0)
			{
				count ++;
				hasCounted.insert(newNum);
				hasCounted.insert(num);
			}
			
			factor /= 10;
			factorTail *= 10;
		}
	
		 ans += (count * (count-1)) / 2;
	}
	
	return ans;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	
	scanf("%d\n", &T);
	
	for (int Case=1; Case<=T; Case++)
	{
		int A,B;
		scanf("%d%d",&A,&B);
		cout << "Case #" << Case << ": " << paircount(A,B) << endl;	
	}
	
	return 0;
}