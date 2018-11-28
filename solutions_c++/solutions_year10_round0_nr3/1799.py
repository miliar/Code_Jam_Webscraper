#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <set>
#include <sstream>
#include <fstream>
#include <map>
#include <algorithm>
#define sqr(a) (a*a)
#define pb push_back
#define fs first
#define sd second
#define debug(a) cout<<#a<<" = "<<a<<endl;
#define DDB cout<<"%"<<endl;
#define all(a) a.begin(),a.end()
#define forn(i,n) for(int i=0;i<n;i++)
using namespace std;

typedef vector<int> vint;
typedef vector<vector<int> > vvint;

const double EPS=1E-10;

void dbgVint(vector <long long> a){
	for (size_t i=0;i<a.size();i++){
		printf("%lld ",a[i]);
	}
	printf("\n");
}

void dbgVVint(vector <vector <long long> > a){
	for (size_t i=0;i<a.size();i++){
		dbgVint(a[i]);
	}
}

void dbgVstr(vector <string> a){
	for (size_t i=0;i<a.size();i++){
		printf("%s\n",a[i].data());
	}
}

vector <vector <long long> > s;
vector <long long> g;
vector <long long> z;
vector <long long> zk;
long long test(long long r, long long k, int n){
	s.clear();
	s.resize(n,vector <long long> (n,0));
	z.clear();
	z.resize(n,-1);
	zk.clear();
	zk.resize(n,0);
	for (int i=0;i<n;i++){
		for (int j=i;j<n;j++){
			if (i==j) s[i][j]=g[j]; else s[i][j]=s[i][j-1]+g[j];
		}
	}
	for (int i=0;i<n;i++){
		for (int j=0;j<i;j++){
			if (j==0) s[i][j]=s[i][n-1]+g[0]; else s[i][j]=s[i][n-1]+s[0][j-1]+g[j];
		}
	}
	//dbgVVint(s);
	vector <long long> v(n,0);
	vector <long long> h(n,0);
	//printf("Debugging nabiranie\n");
	for (int i=0;i<n;i++){
		bool b=true;//еще не набрали
		int j=i;
		long long ts=0;
		while (b && j<n){
			if (s[i][j]>k){
				b=false;
				break;
			} else {
				ts=s[i][j];
				j++;
			}
		}
		if (b) j=0;
		while (b && j<i){
			if (s[i][j]>k){
				b=false;
				break;
			} else {
				ts=s[i][j];
				j++;
			}
		}
		v[i]=ts;
		h[i]=j;
	}
	//cout << endl;
	//dbgVint(v);
	//dbgVint(h);
	//cout << endl;
	long long ans=0;
	int ti=0;
	for (int i=0;i<r;i++){
		if (v[ti]==0) break;
		
		if (z[ti]==-1){
			z[ti]=i;
			zk[ti]=ans;
		} else {
			long long df=i-z[ti];
			long long dd=ans-zk[ti];
			while (i+df<r){
				i+=df;
				ans+=dd;
			}
		}
		
		ans+=v[ti];
		ti=h[ti];
	}
	return ans;
}


int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	long long r,k;
	int n,t;
	cin >> t;

	for (int i=0;i<t;i++){
		cin >> r >> k >> n;
		g.resize(n);
		for (int j=0;j<n;j++) scanf("%lld ",&g[j]);
		cout <<"Case #" << i+1 <<": "<<test(r,k,n)<<endl;
	}
	return 0;
}

