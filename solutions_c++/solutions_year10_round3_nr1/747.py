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
#define maxSize 100000
#define LL long long

int n;
int a[maxSize];
int b[maxSize];
int cnt = 0;
struct node
{
	double x;
	double y;
}inter[maxSize];

void getAC()
{
	int tmpcnt = 0;
	for(int i=0;i<n;i++)
	{
		for(int j=i+1;j<n;j++)
		{
			if(a[i]==b[i])
			{
				if(a[j]==b[j])
					;
				else {
					if(a[i]<std::min(a[j],b[j]))
						;
					else if(a[i]>std::max(a[j],b[j]))
						;
					else {
						cnt++;
					}
				}
			}
			else if(a[i]>a[j] && b[i]<b[j])
				cnt++;
			else if(a[j]>a[i] && b[j]<b[i])
				cnt++;
		}
	}
	cout<<cnt<<endl;
	return;
}
int main()
{
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int t;
	cin >> t;
	for(int cases=1;cases<=t;cases++)
	{
		cin >> n;
		cnt = 0;
		for(int i=0;i<n;i++)
			cin >> a[i] >> b[i];
		printf("Case #%d: ",cases);
		getAC();
	}
	return 0;
}
