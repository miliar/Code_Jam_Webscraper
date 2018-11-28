#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <climits>

using namespace std;

#define PB push_back
#define MP make_pair
#define two(a) (1 << (a))
#define contain(a, b) (((a) & two(b)) != 0)
#define lowbit(a) ((a) & -(a))

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
int a[101],i,z,j,l,h,mins,t,n;
int main()
{
	//freopen("PerfectHarmony.txt", "r", stdin);
	//freopen("PerfectHarmony.out", "w", stdout);
	ofstream fout("PerfectHarmony.out");
	z=0;
	cin>>t;
	while(t--)
	{
		z++;
		mins=-1;
		cin>>n>>l>>h;
		for(i=0;i<n;i++)
		{
			cin>>a[i];
		}
		for(i=l;i<=h;i++)
		{
			for(j=0;j<n;j++)
			{
				if(a[j]%i==0||i%a[j]==0)
				{
					continue;
				}
				else 
				{
					break;
				}
			}
			if(j==n)
			{
				mins=i;
				break;
			}
		}
		if(mins!=-1)
		{
			fout<<"Case #"<<z<<": "<<mins<<endl;
		}
		else 
		{
			fout<<"Case #"<<z<<": "<<"NO"<<endl;
		}
		
	}
	return 0;
}
