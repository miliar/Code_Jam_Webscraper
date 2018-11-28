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

const int size=1000000;
int T,casenum,num,ans,cnt,i,j;
long long n,tmp;
long long prime[size+1];
bool primeQ[size+1];
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	cin>>T;
	for (i=2;i<=size;i++)
		primeQ[i]=true;
	for (i=2;i<=size;i++)
		for (j=2;i*j<=size;j++)
			primeQ[i*j]=false;
	num=0;
	for (i=2;i<=size;i++)
		if (primeQ[i])
			prime[++num]=i;
	for (casenum=1;casenum<=T;casenum++)
	{
		cout<<"Case #"<<casenum<<": ";
		ans=1;
		cin>>n;
		if (n==1)
		{
			cout<<0<<endl;
			continue;
		}
		for (i=1;i<=num;i++)
		{
			if (prime[i]>n) break;
			tmp=prime[i];
			ans+=floor(log(n)/log(prime[i]))-1;
			/*cnt=0;
			while (1)
			{
				tmp*=prime[i];
				if (tmp<=n) cnt++;
				else break;
			}
			ans+=cnt;*/
		}
		cout<<ans<<endl;
	}
}

