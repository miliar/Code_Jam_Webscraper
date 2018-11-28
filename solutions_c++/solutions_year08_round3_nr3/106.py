#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef stringstream sst;
#define fri(a,i) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define fr(i,n) for(int i=0; i<(int)(n); i++)
#define zer(a) memset((a),0,sizeof(a));
#define all(a) (a).begin(), (a).end()
#define pb push_back

#define M 1000000007
int main(){
    int N;
	cin>>N;
    for(int l=1; l<=N; l++){
		long long n,m,X,Y,Z;
		cin>>n>>m>>X>>Y>>Z;
	    vector<long long> A(m);
		vector<long long> a(n);
		for(int i=0; i<m; i++)
		  cin >>A[i];
		for(int i=0; i<n; i++){
			a[i]=A[i%m];
			A[i%m] = (X*A[i%m]+Y*(i+1))%Z;
		}
		vector<long long> b(n,1);
		long long ret=0;
		for(int i=0; i<n; i++){
		   for(int j=0; j<i; j++)
		     if(a[j]<a[i]) b[i]=(b[i]+b[j])%M;
		   ret=(ret+b[i])%M;	   
		}
	    cout<<"Case #"<<l<<": "<<ret<<endl;
	}
}
