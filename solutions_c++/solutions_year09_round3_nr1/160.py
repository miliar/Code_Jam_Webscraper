/*
TASK: 
LANG: C++
USER: smilitude1
*/

#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define SET(t,v) memset((t), (v), sizeof(t))
#define sz size()
#define pb push_back
#define i64 long long
#define ALL(x) x.begin(), x.end()

#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define REV(x) reverse( ALL( x ) )

#define IO freopen("a.in","r",stdin); freopen("a.out","w",stdout);
#define debug(x) cerr << __LINE__ <<" "<< #x " = " << x << endl


string add( string a, string b ) {
    if( a.sz < b.sz ) swap( a, b);    
    while( b.sz != a.sz ) b = "0" + b; // adding leading zeros
    
    reverse( a.begin(), a.end() );
    reverse( b.begin(), b.end() );
    
    int sum, carry = 0;
    string ret;
    REP(i,a.sz) {
        sum = a[i] - '0' + b[i] - '0' + carry;
        carry = 0;
        if( sum <= 9 ) ret += sum + '0' ;
        else {
            ret += (sum-10) + '0';
            carry = 1;
        }
    }
    if( carry ) ret += '1';
    reverse( ret.begin() , ret.end() );
    return ret;
    
}

string multiply( string a, string b ) {
    string mul[10];
    
    mul[0] = "0";
    mul[1] = a;
    FOR(i,2,9) mul[i] = add( mul[i-1], a );
    
    reverse( b.begin(), b.end() );
    string ret = "0";
    REP(i,b.sz) {
        string s = mul[ b[i]-'0' ];
        if( s != "0" ) REP(k,i) s += "0";
        ret = add( ret, s );
    }
    
    
    return ret;    
}

string multiply( string a, int b ) {
    ostringstream sout;
    sout << b;
    return multiply ( a, sout.str() );
}


bool better( string a, string b ) {
	if( a.sz < b.sz ) return true;
	if( a.sz > b.sz ) return false;
	REP(i,a.sz) if( a[i] < b[i] ) return true; else if( a[i] > b[i] ) return false;
	return false; // equal! 
}

string process( vector< int > v, int base ) {
	string ret;
	REV( v );
	string mul = "1";
	
	ret = multiply( mul, v[0] );
	FOR(i,1,v.sz-1) {
		mul = multiply( mul, base );
		string t = multiply( mul, v[i] );
		ret = add( ret, t );
	}

	return ret;
}

string convert( string s, int base ) {
	bool used = false;
	int unused[ base + 1 ]; SET( unused, 1 );
	int value[500]; SET( value, -1 );
	
//	cout << s << " " << base<<" entering convert "<<endl;

	vector< int > v;
	REP(i,s.sz) if( value[ s[i] ] == -1 ) {
		REP(j,base) if( unused[j] ) {
			if( j == 0 && !used ) continue;
			used = true;
			value[ s[i] ] = j;
			unused[j] = false;
			v.pb( j );
			break;
		}
	}else v.pb( value[ s[i] ] );
		
//	cout <<"printing v "<< v.sz << endl;
//	REP(i,v.sz ) cout <<" " << v[i] ; cout << endl;
	return process( v, base ); // use the bigint to make it a decimal number	
}

int main() {
	int t, ncase = 0;
	string s;
	
	IO

	scanf("%d",&t);
	while( t-- ) {
		cin >> s;
		set< char > abdul; REP(i,s.sz) abdul.insert( s[i] );
		int totalchar = abdul.sz;
		string ans = "";
		
//		cout << totalchar << endl;
			
		FOR(base,2,36) if( totalchar <= base ) {
//			cout <<"trying "<< base << endl;
			string p = convert( s, base );
			if( ans == "" || better( p, ans ) ) ans = p;
//			cout <<"processing "<< base <<" " << ans << endl;
		}

		printf("Case #%d: %s\n", ++ncase, ans.c_str());
	}

	return 0;
}
