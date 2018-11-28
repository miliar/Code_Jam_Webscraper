#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <numeric>
using namespace std;

typedef long long tint;
typedef pair<int,int> pii;
typedef complex<double> pto;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<string> vs;

#define forn(i,n) forsn(i,0,n)
#define forsn(i,s,n) for( tint ___n=tint(n), i=tint(s) ; i<___n ; ++i )
#define fordn(i,n) fordsn(i,0,n)
#define fordsn(i,s,n) for( tint ___s=tint(s), i=tint(n)-1 ; i>=___s ; --i )
#define forall(i,c) for( typeof((c).begin()) i=(c).begin() ; i!=(c).end() ; ++i )
#define all(c) (c).begin(), (c).end()
#define sz(a) ((int)(a).size())
#define pb push_back
#define clear(x,c) memset(x,c,sizeof(x))

const int mx[] = {-1,0,1,0};
const int my[] = {0,-1,0,1};
const int inf=0x7fffffff;

int main() {
	
	tint T;
	cin >> T;
	
	for(tint t = 1; t <= T; t++){
		queue <tint> q;
		tint R, K, N;
		cin >> R >> K >> N;
		tint euros = 0;
		for(tint n = 1; n <= N; n++){
			tint pass;
			cin >> pass;
			q.push(pass);
		}
		for(tint r = 1; r <= R; r++){
			tint max = N;
			tint size = K;
			tint top;
			if(q.empty() == false){
				top = q.front();
				while(size - top >= 0 && max != 0){
					q.pop();
					size -= top;
					euros += top;
					max--;
					q.push(top);
					top = q.front();
				}		
			}
		}
		cout << "Case #" << t << ": " << euros << endl;
		
	}
    return 0;
}
