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
int ar[1001];
int sel[1001];
ll store[2001];
int main()
{
	int tc;
	scanf("%d",&tc);
	int caseno=1;
	while(tc--){
		int R,k,N;
		scanf("%d%d%d",&R,&k,&N);
		memset(sel,-1,sizeof(sel));
		for(int i=0;i<N;i++)scanf("%d",ar+i);
		int is=0;
		int si=0;
		while(sel[si]==-1){
			int gsi=si;
			ll val=ar[si];
			//val<=k given :))
			si=(si+1)%N;
			while((si!=gsi)&&val+ar[si]<=k){val+=ar[si];si=(si+1)%N;}
			store[is++]=val;
			sel[gsi]=is-1;
		}
		//cout<<"ASD"<<endl;
		//Cycle goes from sel[si] to is-1
		si=sel[si];
		R--;
		ll sum=0;
		for(int i=0;i<is;i++){sum+=store[i];store[i]=sum;}
		if(R<si){
			sum=store[R];
			printf("Case #%d: %lld\n",caseno++,sum);
		}
		else{
			int rlen=R-si;
			sum=(sum-store[si-1])*(rlen/(is-si))+(store[si+rlen%(is-si)]);
			printf("Case #%d: %lld\n",caseno++,sum);
		}
	}
	return 0;
}
