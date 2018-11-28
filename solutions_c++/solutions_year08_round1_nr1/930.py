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

using namespace std;
int arr1[1000],arr2[1000];
int main()
{
	freopen("a.txt","w",stdout);
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int n,j;
		cin>>n;
		for(j=0;j<n;j++)
			cin>>arr1[j];
		for(j=0;j<n;j++)
			cin>>arr2[j];
		sort(arr1,arr1+n);
		sort(arr2,arr2+n);
		int min = 0;
		for(j=0;j<n;j++)
			min += arr1[j]*arr2[n-j-1];
		cout<<"Case #"<<i+1<<": "<<min<<endl;
	}
	return 0;
}
