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
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;
int main()
{
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int nt;
	cin>>nt;
	for(int it=0;it<nt;it++)
	{
		int n,k,t;
		cin>>n;
		vector<int> vals(n+1,-1);
		int cur=0;
		int rev=0;
		for(int i=1;i<=n;i++)
		{
			while(1)
			{
				if(vals[cur+1] > 0)
					cur=(cur+1)%n;
				else
				{

					if(rev + 1 == i )
					{
						vals[cur+1] = i;
						rev=0;
						cur=(cur+1)%n;
						break;
					}
					else
					{
						rev++;
						cur=(cur+1)%n;
					}
				}
			}
		}
		cin>>k;
		int id;
		cout<<"Case #"<<it+1<<":";
		for(int j=0;j<k;j++)
		{
			cin>>id;
			cout<<" "<<vals[id];
		}
		cout<<endl;
	}
	return 0;
}
