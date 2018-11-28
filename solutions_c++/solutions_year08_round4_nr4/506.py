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
		int k;
		string s;
		cin>>k>>s;
		string b(s);
		int t=s.size()/k;
		vi a(k);
		int re=INT_MAX;
		for(int i=0; i<k; i++) a[i]=i;
		do{
			for(int j=0; j<t; j++){
			  for(int i=0; i<k; i++)
				b[j*k+i]=s[j*k+a[i]];
			}
			int ret=1;
			for(int i=1; i<b.size(); i++)
			  if(b[i]!=b[i-1]) ret++;
			re<?=ret;  
		}while(next_permutation(all(a)));
	    cout<<"Case #"<<l<<": "<<re<<endl;
	}
}
