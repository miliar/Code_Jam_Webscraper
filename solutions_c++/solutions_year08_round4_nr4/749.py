#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
 
typedef long long int lint;
typedef pair<int,int> par;
 
#define sz size
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define sqr(x) (x)*(x)
#define x first
#define y second
#define rep(i,n)  for (int (i)=0;(i)<(int)(n);(i)++)
#define Rep(i,a,n) for (int (i)=(int)(a);(i)<(int)(n);(i)++)

int k;
string S;
int coun(string s) {
	int dif=1;
	Rep(i,1,s.sz()) {
		if (s[i]!=s[i-1]) dif++;
	}	
	return dif;	
}

int main() {
	int N;
	cin >> N;
	Rep(i,1,N+1) {
		cin >> k;
		cin >> S;
		vector<int> v;
		rep(j,k)
			v.pb(j);
		int count=100000001;
		do {
			string s4="";
			for (int j=0;j<(int)S.sz();j+=k) {
				string s3=S.substr(j,k);
				for (int z=0;z<k;z++)
					s4+=s3[v[z]];
			}			
			//cout << s4 << endl;
			count=min(count,coun(s4));
		}
		while (next_permutation(all(v)));
		cout << "Case #" << i << ": " << count << endl;
	}
	return 0;
}
