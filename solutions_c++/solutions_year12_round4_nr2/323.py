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

int T,N;
double W,L,r[1010],x[1010],y[1010];

int main(){
	cin>>T;
	rep(tc,T){
		cout<<"Case #"<<tc+1<<": ";
		cin>>N>>W>>L;
		rep(i,N)cin>>r[i];
		sort(r,r+N);
		reverse(r,r+N);
		x[0]=y[0]=0;
		double X=r[0],Y=0,nxY=r[0]+0.0;
		
		rep2(i,1,N){
			if(X==0 || W-X >= r[i]){
				if(X==0){
					Y=nxY+r[i];
					//cout<<Y<<" "<<nxY<<" "<<r[i]<<endl;
					nxY=Y+r[i];
					//cout<<nxY<<endl;
					x[i]=0;
					y[i]=Y;
					X=r[i];
				}
				else{
					x[i]=X+r[i]+0.0;
					X=x[i]+r[i]+0.0;
					y[i]=Y;
					//cout<<x[i]<<" "<<y[i]<<endl;
				}
			}else{
				X=0;
				i--;
			}
		}
		
		rep(i,N)cout<<setprecision(15)<<x[i]<<" "<<y[i]<<" ";
		cout<<endl;
	}
}
