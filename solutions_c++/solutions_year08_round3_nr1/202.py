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
		int K, P, L;
		cin>>P>>K>>L;
		if(double(L)/K>P+eps){
			cout << "Case #" << i+1 << ": Impossible\n";
		
		}else{
		vi freq(L);
		REP(j, L){
			cin>>freq[j];
		}
		sort(freq.rbegin(), freq.rend());
		long long sum = 0;
//		cout.setf(ios::fixed); 
		for(int j=0; j<L;j++){
			int mult=j/K+1;
			sum+=(long long)mult*freq[j];
			//cout<<sum<<" ";
		}
		cout << "Case #" << i+1 << ": " << sum<< "\n";
		}
	}
	exit(0);
}

