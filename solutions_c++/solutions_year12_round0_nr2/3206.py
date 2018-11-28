#include <iostream>
#include <fstream>
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define EPS 1e-9
#define INF MOD
#define MOD 1000000007LL
#define fir first
#define iss istringstream
#define sst stringstream
#define ite iterator
#define ll long long
#define mp make_pair
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<n;i++)
#define pi pair<int,int>
#define pb push_back
#define sec second
#define sh(i) (1LL<<i)
#define sz size()
#define vi vector<int>
#define vc vector
#define vl vector<ll>
#define vs vector<string>

int T,N,S,p,t;

int main(){
	cin>>T;
	rep(tc,T){
		cout<<"Case #"<<tc+1<<": ";
		cin>>N>>S>>p;//cout<<N<<" "<<S<<" "<<p<<endl;
		if(p==0){
			rep(i,N)cin>>t;
			cout<<N<<endl;
		}
		else if(p==1){
			int ans=0;
			rep(i,N)cin>>t,ans+=(t>=1);
			cout<<ans<<endl;
		}
		else{
			int a=0,b=0;
			rep(i,N){
				cin>>t;
				if(t>=3*p-2)a++;
				else if(t>=3*p-4)b++;
			}
			//cout<<a<<" "<<b<<" "<<S<<endl;
			cout<<a+min(b,S)<<endl;
		}
	}
}
