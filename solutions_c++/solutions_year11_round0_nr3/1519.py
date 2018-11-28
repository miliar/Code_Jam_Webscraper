#include <iostream>
//#include <cstdio>
//#include <cmath>
//#include <string>
#include <algorithm>
using namespace std;

inline int min(int x, int y)
{
	return x<y?x:y;
}
inline int max(int x, int y)
{
	return x>y?x:y;
}
inline int abs(int x)
{
	return x<0?-x:x;
}

#define FORIN for(int i = 0; i < n; i++)

void compute()
{
	int n;
	int nums[1005];
	cin >> n;
	FORIN cin >> nums[i];
	
	int a = 0;
	FORIN a ^= nums[i];
	
	if(a == 0) // has a solution
	{
		int s = 0;
		FORIN s += nums[i];
		cout << s - *min_element(nums, nums+n) << endl;
	}
	else cout << "NO" << endl;
}

int main()
{
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		cout << "Case #" << i+1 << ": ";
		compute();
	}
}
