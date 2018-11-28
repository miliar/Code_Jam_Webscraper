#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<iterator>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<deque>
#include<stack>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<string>
#include<cmath>
#include<ctime>
using namespace std;
long long int X[100005],Y[100005];
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define debug 1
int main()
{
	long long int n,A,B,C,D,x0,y0,M,N,cnt;
	scanf("%lld",&N);
	for(long long int test=0;test<N;test++)
	{
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld",&n,&A,&B,&C,&D,&x0,&y0,&M);
		cnt=0;
		A%=M;B%=M;C%=M;D%=M;
		X[0]=x0;Y[0]=y0;
		for(long long int i=0;i<n-1;i++)
		{
			X[i+1] = ((long long int)(A*X[i])%M + B)%M;
			Y[i+1] = ((long long int)(C*Y[i])%M + D)%M;
		}
		for(long long int i=0;i<n-2;i++)
			for(long long int j=i+1;j<n-1;j++)
				for(long long int k=j+1;k<n;k++)
					if((X[i]+X[j]+X[k])%3==0 && (Y[i]+Y[j]+Y[k])%3==0)
						cnt++;
		printf("Case #%lld: %lld\n",test+1,cnt);
	}
	return 0;
}
