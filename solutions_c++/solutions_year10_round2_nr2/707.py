/*
ID: harrymw1
LANG: C++
TASK: 
*/
 
#include <iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include <cstdio>
#include<map>
#include<stack>
#include<set>
#include<queue>
#include<cctype>
#include<assert.h>
#include<numeric>
#include<ctime>
#include<iterator>
//#include<sstream>
using namespace std;

#define PI acos(-1.0)
#define fore(i,a) for(int i=0; i<(a); i++)
#define forv(i,a) for(typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define pb push_back
#define all(x) x.begin(),x.end()
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
/*template<class T> string toString(T n){
	ostringstream ost;ost<<n;ost.flush();
	return ost.str();
}*/

//__builtin_popcount(int x);
int main()
{
	freopen("A.in.txt", "r", stdin);
	freopen("A.out.txt", "w", stdout);
	//clock_t start, finish;
   	//double duration;
   	//start = clock();
	int t,ca=1;
	cin>>t;
	while(t--){
		int n,k,b,t;scanf("%d%d%d%d",&n,&k,&b,&t);
		int arr[55],speed[55];
		for(int i=0;i<n;i++)scanf("%d",arr+i);
		for(int i=0;i<n;i++)scanf("%d",speed+i);
		bool can[55];
		for(int i=n-1;i>=0;i--){
			int nt=ceil(abs(b-arr[i])/(speed[i]+0.0));
			if(nt<=t)can[i]=true;
			else can[i]=false;
		}
		int cc=0;
		for(int i=0;i<n;i++)if(can[i])++cc;
		if(cc<k)printf("Case #%d: IMPOSSIBLE\n",ca++);
		else {
			int ret=0,unable=0,ncan=0;
			for(int i=n-1;i>=0;i--){
				if(ncan>=k)break;
				if(can[i]==false)++unable;
				else ncan++,ret+=unable;
			}
			printf("Case #%d: %d\n",ca++,ret);
		}

	}


	//finish = clock();
   	//duration = (double)(finish - start) / CLOCKS_PER_SEC;
	//printf( "%f seconds\n", duration );
	return 0;
}
