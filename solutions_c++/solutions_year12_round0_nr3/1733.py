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

string intostr( int m){

std::ostringstream sstream;
sstream<<m;
std::string x=sstream.str();
return x;

}
int main(){	

	freopen("3l.in", "r", stdin);
	freopen("3l.out", "w", stdout);
	int A,B,n,t,t1;
	int res = 0;
	vs p(0);
	cin>>t1;
	FOR(k, 1, t1){
	cin >> A >>B;
	string x, y, z;
	y = intostr(B);
	FOR(i, A, B-1){

		x = intostr(i);
		n = x.si();
		t = n;
		while(--t){
			z.append(x, t, n-t);
			z.append(x, 0, t);
			if(z[0] == '0') {
			z = "";
			continue;
			}
			int a = 1;
			int b = p.si();
			FOR(l, 0, b-1){
			if(p[l] == z) a = 0;
			}
			p.pb(z);
			if(z <= y && z > x && a == 1) res++;
			z = "";
		}
		p.clear();
	}
	cout <<"Case #"<<k<<": "<< res <<endl;
	res = 0;
	}
return 0;
}
