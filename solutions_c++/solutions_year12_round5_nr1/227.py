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
#include <ctime>
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

#pragma comment(linker, "/STACK:400000000")

#define EPS 1e-9
#define INF MOD
#define MOD 1000000007LL
#define fir first
#define foreach(it,X) for(it=X.begin();it!=X.end();it++)
#define iss istringstream
#define ite iterator
#define ll long long
#define mp make_pair
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<n;i++)
#define pi pair<int,int>
#define pb push_back
#define sec second
#define sh(i) (1LL<<i)
#define sst stringstream
#define sz size()
#define vi vector<int>
#define vc vector
#define vl vector<ll>
#define vs vector<string>

int T,N,L[1011],P[1011];

int main(){
	cin>>T;
	rep(tc,T){
		cout<<"Case #"<<tc+1<<":";
		cin>>N;
		rep(i,N)cin>>L[i];
		rep(i,N)cin>>P[i];
		int used[1011]={};
		rep(i,N){
			int worst=-1,p=-1;
			rep(j,N)if(!used[j]){
				if(P[j]>p){
					worst=j;
					p=P[j];
				}
			}
			used[worst]=1;
			cout<<" "<<worst;
		}
		cout<<endl;
	}
}
