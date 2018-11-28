#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <cstring>
#include <queue>
#define vvi vector<vector<int> > 
#define pii pair<int,int>
#define vpii vector<vector<pair<int,int> > > 
#define mp(a,b) make_pair(a,b)
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define sz size()
#define pb push_back
#define all(x) x.begin(),x.end()
using namespace std;
int A[2000];
int B[2000];
int main()
{
	int tc;
	scanf("%d",&tc);
	int caseno=1;
	while(tc--){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%d%d",&A[i],&B[i]);
		}
		int ret=0;
		for(int i=0;i<n;i++){
			for(int j=i+1;j<n;j++){
				if((A[i]<A[j]&&B[i]>B[j])||(A[i]>A[j]&&B[i]<B[j]))ret++;
			}
		}
		printf("Case #%d: %d\n",caseno++,ret);
	}
	return 0;
}
