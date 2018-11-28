#include<iostream>
#include<cmath>
#include<cstring>
#include<string>
#include<queue>
#include<stack>
#include<vector>
#include<algorithm>
#include<map>
#include<vector>
#include<set>
#include<cstdio>
#include<list>
#include<cctype>
#include<complex>
#include<sstream>
#include<numeric>

using namespace std;

typedef vector< int > vi;
typedef vector< vi > vii;
typedef map< int , string > mis;
typedef map< string, int > msi;
typedef vector< string > vs;
typedef pair<int,int> pii;
typedef map<int,int> mii;

#define mem(a,i) memset(a,i,sizeof(a))
#define pb push_back
#define Inf ( 1 << 30 )

int test_case;
int N;
string inp;
int n;

vector< int > b;
vector< int > o;
vector< pair< char, int > > v;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &test_case);
    for( int caseId = 1; caseId <= test_case; caseId ++ ){
        scanf("%d", &N);
        b.clear();
        o.clear();
        v.clear();
        for( int i = 0; i < N; i ++ ){
            cin >> inp >> n;
            char c = inp[ 0 ] ;
            v.pb( make_pair( c, n ) );
            if( c == 'B' ) b.pb( n );
            else o.pb( n );
        }

        int i = 0;
        int j = 0;
        int k = 0;
        int ans;
        int B,O;
        B = O = 1;
        for( ans = 0; k < N ; ans ++ ){
            bool flag = false;
            char now = v[ k ].first;
            int nt = v[ k ].second;

            if( b.size() > 0 && i < b.size() ){
                if( B < b[ i ] ) B ++;
                else if( B > b[ i ] ) B --;
                else {
                    if( now == 'B' ){
                        i ++;
                        flag = true;
                    }
                }

            }

            if( o.size() > 0 && j < o.size() ){
                if( O < o[ j ] ) O ++;
                else if( O > o[ j ] ) O --;
                else {
                    if( now == 'O' ){
                        j ++;
                        flag = true;
                    }
                }

            }

            if( flag ) k ++;
        }

        printf("Case #%d: %d\n", caseId, ans );
    }
	return 0;
}
