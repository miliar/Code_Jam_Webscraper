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
#include <queue>
#include <string>
#include <cstring>
using namespace std;

#define FOR(i,a,b)   	for(int (i)=(a);(i)<(b);(i)++)
#define REP(i,a,b)   	for(int (i)=(a);(i)<=(b);(i)++)
typedef long long 		bint;

#define PB           	push_back
#define INF          	1e10
#define DEBUG(___x)     cout<<#___x<<" = ["<<___x<<"]"<<endl
#define SORT(___a)      sort(___a.begin(),___a.end())
#define RSORT(___a)     sort(___a.rbegin(),___a.rend())
#define PI           	3.141592653589793238
#define MP           	make_pair
#define PII          	pair<int,int>
#define ALL(___v)       (___v).begin(), (___v).end()
#define VS           	vector<string>
#define VI           	vector<int>
#define S            	size()
#define print(___v)     {cout<<"[";if(___v.S)cout<<___v[0];FOR(i,1,___v.S)cout<<","<<___v[i];cout<<"]\n";}

int main()
{
	freopen("A-large.in", "r", stdin);
	//freopen("in.txt", "r", stdin);
	freopen("BigA.out", "w", stdout);
	
	int T, pd, pg;
	bint N;
	cin >> T;
	
	FOR(t,0,T) {
		
		cin >> N >> pd >> pg;
		
		int vl = __gcd(pd, 100);
		
		int a = pd;
		int b = 100;
		
		if(vl > 0 && (a%vl)==0) {
			
			a /= vl;
			b /= vl;
		}
		
		
		if( b > N) {
			
			cout << "Case #"<<t+1<<": Broken"<<endl;
			continue;
		}
		
		if(pg == 100) {
			
			if(pd != 100) {
				
				cout << "Case #"<<t+1<<": Broken"<<endl;
				continue;
			}
		}
		if(pd > 0 && pg == 0) {
			
			cout << "Case #"<<t+1<<": Broken"<<endl;
			continue;
		}
		
		cout << "Case #"<<t+1<<": Possible"<<endl;
	}
	
	return 0;
}

