#include <algorithm>
#include <numeric>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <locale>

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORE(i,n) for (int i=0; i<=n; ++i)
#define REP(i,a,b) for (int i=a; i<b; ++i)
#define REPE(i,a,b) for (int i=a; i<=b; ++i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))


typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
const double pi = acos(-1.0);
const int inf =(int) 1e9;


int main()
{
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d",&t);
	int a,b;
	int res,res1;
	int k,m;
	FOR(i,t)
	{
		scanf("%d%d",&a,&b);
		//vector<bool> z(2000005);
		res=0;
		res1=0;
		REPE(j,a,b)
		{
			if (j==2221)
				j=j;
			char s[20]="";
			itoa(j,s,10);
			k=strlen(s);
			res1=0;
			REP(l,1,k)
			{
				char s1[20]="";
				if (s[l]=='0')
					continue;
				m=l;
				for(;m<k; ++m)
					s1[m-l]=s[m];
				m=m-l;
				for (int n=0; n<l; ++n,++m)
					s1[m]=s[n];
				m=atoi(s1);
				if (m>=a && m<=b && m!=j)
				{
					//cout<<j<<"  "<<m<<endl;
					++res;
					//z[m]=true;
				}
			}
			//res+=((1+res1)/2)*res1;
		}

		cout<<"Case #"<<i+1<<": "<<res/2<<endl;
	}
	return 0;
}