#include <stdio.h>
#include <sstream>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <iosfwd>

using namespace std;

#define _(a,b) memset(a, b, sizeof(a)) // TODO: learn what the hell is: memset(....)
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define fo(a,b,c) for(a=(b);a<(c);a++)
#define fr(a,b) fo(a,0,(b))
#define fi(a) fr(i,(a))
#define fj(a) fr(j,(a))
#define fk(a) fr(k,(a))
char sBuf[100005];
int ni() { int i; scanf("%d", &i); return i; }
string ns() { scanf("%s", sBuf); return sBuf; }

typedef stringstream ss;

template <class T> 
void out( T a, T b ) { 
	bool first = true; 
	for( T i = a; i != b; ++ i ) {
		if( !first ) printf( ", " ); 
		first = false;
		cout << * i;
	}
	printf( "" );
}

template <class T>
inline string to_string (const T& t)
{
	ss s_s("");
	string result;
	s_s << t;
	result = s_s.str();
	return result;
}

template <class T>
inline int to_int (const T& t)
{
	ss s_s(stringstream::in | stringstream::out);
	int result;
	s_s << t;
	s_s >> result;
	return result;
}

#define SMALL
//#define LARGE

int main(){
#ifdef SMALL
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
#endif
	
	int T;
	T=ni();
	
	for (int t=1; t<=T; t++) {
		int a;
		printf("Case #%d: ", t);
		int A, B;
		A=ni();
		B=ni();
		int x=0;
		
		for (int n = A; n<=B; n++){
			int m;
			string N = to_string(n);
			int length = N.length();
			
			if(length == 1) { x = 0; break; }
			
			for (int k=length-1; k>0; k--) {
				
				string mL=N.substr(k,length - 1);
				string mR=N.substr(0,k);
				
				string M = mL+mR;
				m=to_int(M);
				if(n<m && m <= B)
				{
					x++;
				}
			}
		}
		
		printf("%d", x);
		cout << endl;
	}
	
}


