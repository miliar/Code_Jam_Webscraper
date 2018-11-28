#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
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
using namespace std;

#define PB push_back
#define MP make_pair

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int casenum,T;
int S,R,X,n,b,e,w,i;
double a[101];
double ans,t,tmp;

int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	cin>>T;
	for (casenum=1;casenum<=T;casenum++)
	{
		cout<<"Case #"<<casenum<<": ";
		cin>>X>>S>>R>>t>>n;
		memset(a,0,sizeof(a));
		a[0]=X;
		for (i=1;i<=n;i++)
		{
			cin>>b>>e>>w;
			a[w]+=e-b;
			a[0]-=e-b;
		}
		cerr<<w;
		ans=0;
		for (i=0;i<=100;i++)
		{
			if (fabs(t)<1e-8) ans+=a[i]/(S+i);
			else
			{
				tmp=a[i]/(R+i);
				if (tmp>t)
				{
					tmp=t;
					ans+=tmp+(a[i]-tmp*(R+i))/(S+i);
					t=0;
				}
				else
				{
					ans+=tmp;
					t-=tmp;
				}
			}
		}
		printf("%.7f\n",ans);
	}
}

