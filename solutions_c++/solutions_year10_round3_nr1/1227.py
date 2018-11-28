#include<iostream>
#include<vector>
#include<map>
#include<sstream>
#include<math.h>
#include<set>
#include<fstream>
#include<algorithm>
#include<cstring>
#include<cassert> 
#include <list>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

#define debug(x) cout << #x << " = " << x << "\n";
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define sz size()
#define pb push_back
#define mp make_pair
#define fr(i, n) for(i=0;i<n;i++)
#define fr2(i, a, n) for(i=a;i<n;i++)
#define mem(a, n) memset(a, n, sizeof(a))
typedef vector<int> VI;
typedef long long LL;
typedef vector<string> VS;
typedef stringstream SS; 
const int INF = (int) 1e9;
#define LLMax LLONG_MAX

#define cs c_str()
#define frIt(it, s) for(typeof(s.begin()) it=s.begin();it!=s.end();it++)
typedef vector<double> VD;
int compareDouble(double a, double b)
{
	double EPS = 1e-10;
	if(a < b - EPS)
		return -1;
	if(a > b + EPS)
		return 1;
	return 0;
}

int main() {
	int t;
	cin >> t;
	int n, k;
	fr2(k, 1, t+1) {
		cin >> n;
		LL B[n], A[n];
		int i, j;
		int c = 0;
		fr(i, n)
			cin >> A[i] >> B[i];
		fr(i, n) {
			fr2(j, i+1, n) {
				if(A[j]>A[i] && B[j]<B[i]) c++;
				else if(A[j]<A[i] && B[j]>B[i])
					c++;
			}
		}
		cout << "Case #" << k << ": " << c << endl;
	}
	
}
