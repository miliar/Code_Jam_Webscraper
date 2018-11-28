/* C Libs */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
/* IOstream Libs */
#include <iostream>
#include <fstream>
#include <sstream>
/* String Libs */
#include <string>
/* STL Containers */
#include <bitset>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
/* STL Algorithm */
#include <algorithm>
/* Miscellaneous */
#include <complex>
#include <functional>
#include <iterator>
//#include <limits>
#include <numeric>
#include <typeinfo>
#include <utility>
#include <valarray>

using namespace std;

#define REP(i,s,t) for(int _t=t,i=s;i<_t;i++ )
#define REPP(i,s,t) for(int _t=t,i=s;i<=_t;i++)

#define LET(x,a) __typeof(a) x (a)
#define ITER(i,a,b) for(LET(i,a);i!=(b);++i)
#define FOREACH(it,v) ITER(it,v.begin(),v.end())

#define FILLA(a,x) memset(&a,x,sizeof(a))
#define FILL(a,x) memset(a,x,sizeof(a))
#define CLEARA(a,x) FILLA(a,0)
#define CLEAR(a) FILL(a,0)

#define m_p make_pair
#define fst first
#define snd second
typedef pair<int,int> PII;
typedef long long ll;
template<class T> void check_max( T&a, T b ){ if ( a < b ) a = b; }
template<class T> void check_min( T&a, T b ){ if ( a > b ) a = b; }

//#define debug

const int MAXC = 26;

int combine[MAXC][MAXC];
bool oppose[MAXC][MAXC];

int main(){
	int T; cin >> T;
	REP(Case,1,T+1){
		memset(combine,-1,sizeof(combine));
		memset(oppose,false,sizeof(oppose));
		int c,d;
		cin>>c;
		REP(i,0,c){
			string s;
			cin >> s;
			int a = s[0]-'A', b = s[1]-'A', c = s[2]-'A';
			combine[a][b] = combine[b][a] = c;
		}
		cin>>d;
		REP(i,0,d){
			string s;
			cin >> s;
			int a = s[0]-'A', b = s[1]-'A';
			oppose[a][b] = oppose[b][a] = true;
		}

		int n;
		cin>>n;
		string input;
		cin>> input;
		
		string ans = "";
		for( int i = 0; i < (int) input.size(); i++ ){
			ans += input[i];
			if ( ans.length() >= 2 ){
				int a = (*ans.rbegin())-'A';
				int b = (*(ans.rbegin()+1))-'A';

				if ( combine[a][b] > -1 ){
					ans = string(ans.begin(),ans.begin()+ans.length()-2);
					ans += ( combine[a][b] + 'A' );
				}
			}
			for( int i = 0; i < (int)ans.length()-1 ; i++ ){
				int a = (*ans.rbegin())-'A';
				int b = ans[i]-'A';
				if ( oppose[a][b] ){
					ans = "";
					break;
				}
			}
		}
		
		printf("Case #%d: [",Case);
		REP(i,0,ans.length()) printf("%c%s",ans[i],i==(int)ans.length()-1?"":", ");
		putchar(']');
		putchar('\n');
	}
	return 0;
}
