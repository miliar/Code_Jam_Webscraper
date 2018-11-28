#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <stack>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define FOR(i,a,b) for( int i=(a); i<(b); ++i)
#define FORD(i,a,b) for( int i=(a); i>(b); --i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) (int)(X).size()
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end(); ++it)

#define N 0
#define E 1
#define S 2
#define W 3

#define R(x) (((x)+1)%4)
#define L(x) (((x)+3)%4)

int ax[4] = { 0, 1, 0, -1 };
int ay[4] = { 1, 0, -1, 0 };

int main(){

	freopen("large.in", "r", stdin );
	freopen("out", "w", stdout );

	int tn;
	int cn = 1;
	cin >> tn;
	while( tn-- ){
		int l;
		cin >> l;
		int x, y, bx, by;
		x = y = 3001;
		bx = by = 3001;
		int d = N;

		VI maxp = VI(8192, -8192);
		VI minp = VI(8192, 8192 );

		LL oarea = 0;
		REP( i, l ){
			string s;
			int t;
			cin >> s >> t;
			REP( j, t ){
				REP( k, SZ(s) ){
					if( s[k] == 'F' ){ 
						x += ax[d], y += ay[d];
						oarea += bx * y - by * x;
						bx = x;
						by = y;
						minp[x] = min( minp[x], y );
						maxp[x] = max( maxp[x], y );
					}
					else if( s[k] == 'R' ) d = R(d);
					else if( s[k] == 'L' ) d = L(d);
					else while(1);
				}
			}
		}

		oarea = abs(oarea) / 2;

		stack<int> st;
		VI ip1, ip2;

		st.push(-1);
		REP( i, 8192 ){
			if( maxp[i] == -8192 ) continue;
			//while( st.top() != -1 && maxp[st.top()] < maxp[i] ) st.pop();
			if( st.top() == -1 || maxp[st.top()] < maxp[i] ) st.push( i );
		}

		while( st.top() != -1 ){
			ip1.PB(st.top());
			st.pop();
		}

		FORD( i, 8191, -1 ){
			if( maxp[i] == -8192 ) continue;
			//while( st.top() != -1 && maxp[st.top()] < maxp[i] ) st.pop();
			if( st.top() == -1 || maxp[st.top()] < maxp[i] ) st.push( i );
		}

		while( st.top() != -1 ){
			ip1.PB(st.top());
			st.pop();
		}

		sort( ALL(ip1) );
		ip1.erase( unique(ALL(ip1)), ip1.end() ); 

	
		REP( i, 8192 ){
			if( minp[i] == 8192 ) continue;
			//while( st.top() != -1 && minp[st.top()] > minp[i] ) st.pop();
			if( st.top() == -1 || minp[st.top()] > minp[i] ) st.push( i );
		}

		while( st.top() != -1 ){
			ip2.PB(st.top());
			st.pop();
		}

		FORD( i, 8191, -1 ){
			if( minp[i] == 8192 ) continue;
			//while( st.top() != -1 && minp[st.top()] > minp[i] ) st.pop();
			if( st.top() == -1 || minp[st.top()] > minp[i] ) st.push( i );
		}

		while( st.top() != -1 ){
			ip2.PB(st.top());
			st.pop();
		}
		sort( ALL(ip2) );
		ip2.erase( unique(ALL(ip2)), ip2.end() ); 


		x = 0;
		y = 0;
		int area = 0;

		while( x < SZ(ip1)-1 && y < SZ(ip2)-1 ){
			//int len = maxp[ip1[x]] - minp[ip2[y]];
			int len;

			if( maxp[ip1[x]] < maxp[ip1[x+1]] ) len = maxp[ip1[x]];
			else len = maxp[ip1[x+1]];

			if( minp[ip2[y]] > minp[ip2[y+1]] ) len -= minp[ip2[y]];
			else len -= minp[ip2[y+1]];
			
			if( ip1[x+1] < ip2[y+1] ){
				area += len * (ip1[x+1] - max(ip1[x], ip2[y]));
				x++;
			}
			else{
				area += len * (ip2[y+1] - max(ip1[x], ip2[y]));
				y++;
			}
		}

		printf("Case #%d: %d\n", cn++, area-(int)oarea);
		//cout << oarea << endl;
		//cout << area << endl;




	}


}