
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream> 
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int nt;
	cin>>nt;
	for(int it=1;it<=nt;it++)
	{
		int n;
		cin>>n;
		vector<string> a(n);
		vector<int> leftmost(n,0);
		for(int i=0;i<n;i++)
			cin>>a[i];
		int ans = 0;
		for(int i=0;i<n;i++)
		{
			for(int j=n-1;j>=0;j--)
			{
				if(a[i][j] == '1')
				{
					leftmost[i] = j;
					break;
				}
			}
		}
		for(int i=0;i<n;i++)
		{
			while(leftmost[i] > i)
			{
				for(int j=i+1;j<n;j++)
				{
					if(leftmost[j] <= i)
					{
						for(int k=j;k>i;k--)
						{
							swap(a[k],a[k-1]);
							swap(leftmost[k],leftmost[k-1]);
							ans++;
						}
						break;
					}
				}
			}
		}
		cout<<"Case #"<<it<<": "<<ans<<endl;
	}
	return 0;
}
