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
typedef vector<string> vs; 
 typedef vector<vi> vvi; 
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
		int n;
		cin>>n;
		vi x(n),y(n);
		REP(j, n){
			cin>>x[j];
		}
		REP(j, n){
			cin>>y[j];
		}
		sort(all(x)); sort(all(y));
		long long sum = 0;
		cout.setf(ios::fixed); 
		REP(j, n){
			sum+=(long long)x[j]*y[n-1-j];
			//cout<<sum<<" ";
		}
		cout << "Case #" << i+1 << ": " << sum<< "\n";
	}
	exit(0);
}

