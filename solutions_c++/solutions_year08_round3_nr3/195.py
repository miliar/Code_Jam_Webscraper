#include <map>
#include <set>
#include <vector>
#include <string>
#include <cstring>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <math.h>
using namespace std;

typedef vector<int> vi; 
typedef set<int> si; 
typedef vector<string> vs; 
 typedef vector<si> vsi; 
 typedef vector<vsi> vvsi; 
 typedef pair<int,int> ii; 
 #define sz(a) int((a).size()) 
 #define pb push_back 
 #define all(c) (c).begin(),(c).end() 
 #define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
 #define present(c,x) ((c).find(x) != (c).end()) 
 #define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define REP(i,n) for (int i = 0; i < (n); i++)
#define REPD(i,n) for (int i = (n) - 1; i >= 0; i--)
#define sqr(a) (a)*(a)
	double  eps2 = 1e-8;
	double  eps = 1e-15;


int main(){
	int N;
	cin >> N;
	REP(i,N) {
		int n, m, X, Y, Z;
		cin>>n>>m>>X>>Y>>Z;
		vi A(m);
		vi seq(n);
		REP(j, m){
			cin>>A[j];
		}
		REP(j, n){
			seq[j] = A[j % m];
			//cout<<A[j%m]<<"\n";
			A[j % m]=((long long)X*A[j % m] +(long long)Y*(j+1))% Z;
		}
		vi res(n, 0);
		long long sum=0;
		REP(j, n){
			res[j]=1;
			REP(k, j){
				//cout<<"k="<<k<<" j="<<j;
				if(seq[k]<seq[j]){
					//cout<<"in";
					res[j]=(res[j]+res[k])%1000000007;
				}
			}
			sum=(sum+res[j])%1000000007;
		}
		/*REP(j,n){
			//cout<<res[j]<<" ";
		}
		REP(j,n){
			cout<<seq[j]<<" ";
		}*/
		cout << "Case #" << i+1 << ": "<<sum<<"\n";
	}
	exit(0);
}

