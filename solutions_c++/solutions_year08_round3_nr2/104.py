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


int main(){
    int N;
	cin>>N;
    for(int l=1; l<=N; l++){
		string s;
		cin>>s;
	    int n=s.size();
		long long ret=0;
		long long m=1;
		for(int i=0; i<n-1; i++) m=m*3;
		for(long long k=0; k<m; k++){
			long long kk=k;
			long long num=0;
			long long cur=s[0]-'0';
			long long sign=1;
			for(int j=1; j<n; j++){ 
			  int t=kk%3;
			  if(t==0) cur=cur*10+s[j]-'0';
			  else if(t==1) {num+=sign*cur; sign=1; cur=s[j]-'0';}
			  else {num+=sign*cur; sign=-1; cur=s[j]-'0';}
			  kk=kk/3;
			}
			num+=sign*cur;
			if(num%2==0||num%3==0||num%5==0||num%7==0) ret++;
		}
	    cout<<"Case #"<<l<<": "<<ret<<endl;
	}
}
