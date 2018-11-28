#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <functional>
#include <utility>//pair
#include <iomanip>

using namespace std;

#define dbg(x) cerr<<#x<<" : "<<x<<endl;
#define inf (1<<30)
#define PB push_back
#define MP make_pair
#define mset(x, a) memset(x, (a), sizeof(x))
typedef long long LL;
const double PI = acos(-1.0);
const double eps = 1e-8;
const int INF = 0x3f3f3f3f;

int main(int argc, char *argv[])
{
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int n;
	cin>>n;
	for(int k=1;k<=n;k++)
	{
		int m;
		cin>>m;
		pair<char,int> q[100];
		for(int i=0;i<m;i++)
		{
			cin>>q[i].first>>q[i].second;
		}
		int o=1;
		int b=1;
		int sum=0,temp=0;
		int t1=0,t2=0;
		for(int j=0;j<m;j++)
		{
			if(q[j].first=='O')
			{
				t1=(abs(q[j].second-o)+1);
				o=q[j].second;
				
				if(q[j-1].first!='O')
				{
					if(t1-temp>0)
					{
						sum+=t1-temp;
						temp=t1-temp;
					}
					else
					{
						temp=1;
						sum+=temp;
					}
				}
				else
				{
					sum+=t1;
					temp+=t1;
				}
			}
			if(q[j].first=='B')
			{
				t2=(abs(q[j].second-b)+1);
				b=q[j].second;
				if(q[j-1].first!='B')
				{
					if(t2-temp>0)
					{
						sum+=t2-temp;
						temp=t2-temp;
					}
					else
					{
						temp=1;
						sum+=temp;
					}
						
				}
				else
				{
					sum+=t2;
					temp+=t2;
				}
			}
		}
		cout<<"Case #"<<k<<":";
		cout<<" "<<sum<<endl;
	}
	return 0;
}

