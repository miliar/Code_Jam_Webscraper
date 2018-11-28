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
#include <fstream>
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
#include <string.h>

using namespace std;

#define max(a,b) (((a) > (b)) ? (a) : (b))
#define min(a,b) (((a) < (b)) ? (a) : (b))

double dat[10005];

double datC[10005];

int L;
double T;
int N,C;

int main()
{

	freopen("B-small-attempt2.in","r",stdin);
	freopen("B-small-attempt2.out","w",stdout);
	
	vector<double> v;
	int cas;

	int i,j,k;
	cin>>cas;

	for (k=1;k<=cas;k++)
	{
		memset(datC,0,sizeof(datC));
		memset(dat,0,sizeof(dat));
//		if (k==9)
//			cout<<"yun"<<endl;

		cin>>L>>T>>N>>C;
		for (i=0;i<C;i++)
			cin>>datC[i];

	//	if (k<35)
	//		continue;
		
		cout<<"Case #"<<k<<": ";
		for (i=0;i<N;i++)
		{
			dat[i]=datC[i%C];
		}

		double t=0;

		double planett=0;

		for (i=0;i<N;i++)
		{
			planett=dat[i]*2;

			if (t+planett>=T&&L!=0)
			{
				v.clear();

				v.push_back(dat[i]-((T-t)*0.5));

				for (j=i+1;j<N;j++)
				{
					v.push_back(dat[j]);
				}

				sort(v.begin(),v.end(),greater<double>());

				t=t+(T-t);
				
				double lasttime=0;
				
				for (j=0;j<L&&j<v.size();j++)
				{
					lasttime+=v[j];
				}

				for (;j<v.size();j++)
				{
					lasttime+=v[j]*2;
				}

				t+=lasttime;
				break;
			}

			t+=planett;
		}

		int intt=t;

		cout<<intt<<endl;

	}
	return 0;
}
