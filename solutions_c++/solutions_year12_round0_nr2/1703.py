#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <iomanip>


using namespace std;

#define vs  vector <string>
#define vi vector <int>
#define vii vector <vector <int> >
#define vp vector <pair <int,int> >
#define pb push_back
#define si size
#define FOR(i,j,k) for(int i = (j); i <= (k); i++)
#define FORN(i,j,k) for(int i = (j); i >= (k); i--)
#define ll long long

int main(){
	freopen("2l.in","r",stdin);
	freopen("2l.out","w",stdout);

	
	int t;
	cin >> t;
	FOR(k, 0, t-1){
	int n,s,p;
	cin >> n >> s >> p;
	vi v(n);
	FOR(i, 0, n-1) cin >> v[i];
	int res = 0;
	int x; 
	if(p <= 2) x = p;
	else
	x = p + p - 2 + p - 2;  
	FOR(i, 0, n-1){
		   if(v[i] < x) continue;
		   else if(v[i] == 0 || v[i] == 1) res++;
		   else if((v[i] == x || v[i] == x + 1) && s > 0) {
			res++;
			s--;
			}
			else if(v[i] > x+1) res++;
		}
		cout <<"Case #"<<k+1<<": "<< res <<endl;
	}
return 0;
}
