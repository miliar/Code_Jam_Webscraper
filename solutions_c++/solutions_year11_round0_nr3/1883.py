#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<cstdlib>
#include<cstring>
#include<sstream>
#include<cassert>
#include<climits>
using namespace std;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vb> vvb;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef pair<int,int> ii;
typedef pair<int,ii> pii;
typedef long long LL;
#define sz(c) (int)c.size()
#define pb push_back
#define all(v) v.begin(),v.end()
#define inc(i,n) for(int i=0;i<n;i++)
#define dec(i,n) for(int i=n-1;i>=0;i--)
#define FOR(i,a,n) for(int i=a;i<n;i++)
#define INF 15000001
#define F first
#define S second
long long P;

int main(){

	int T;
	cin>>T;
	for(int g=1;g<=T;g++){
		int N;
		cin>>N;
		vector<int> arr(N);int sum=0,minval=1000001;
		P=0;
		inc(i,N){
			cin>>arr[i];
			P^=arr[i];
			sum+=arr[i];
			minval = min(minval,arr[i]);
		}
		if(P)
			printf("Case #%d: NO\n",g);
		
		else{
			printf("Case #%d: %d\n",g,sum-minval);
		}		
		arr.clear();
	}
return EXIT_SUCCESS;

}
