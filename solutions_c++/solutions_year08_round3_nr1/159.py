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
typedef vector<long long int> vi; 
vi freq(2000);
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define debug 1
int main()
{
	long long int n,p,k,l,i,test;
	scanf("%lld",&n);
	for(test=0;test<n;test++)
	{
		scanf("%lld %lld %lld",&p,&k,&l);
		for(i=0;i<l;i++)
			scanf("%lld",&freq[i]);
		sort(freq.begin(),freq.begin()+l);
	//	for(i=0;i<l;i++)
	//		cout << freq[i] << " " ;
	//	cout << endl;
		long long int j,cnt=0,it;
		for(i=l-1,j=1;i>=0;i-=k,j++)
		{
			for(it=0;i-it>=0 && it<k;it++)
				cnt+= j*freq[i-it];
	//		cout << cnt << " " << i-k << endl;
		}
		printf("Case #%lld: %lld\n",test+1,cnt);
	}
	return 0;
}
