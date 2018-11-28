#include <iostream>
#include <vector>
#include <map>
#include <cctype>
#include <climits>
#include <sstream>
#include <algorithm>
#include <cassert>
#include <cstring>
#include <cstdio>

#define ALL(v) (v).begin(),(v).end()
#define SORT(x) sort(ALL(x))
#define UNIQUE(x) (SORT(x), (x).resize(unique(ALL(x))-x.begin()))
#define REVERSE(x) reverse(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))

#define SZ(v) ((int)(v).size()) 
#define ARRSZ(a) (sizeof(a) / sizeof(a[0]))
#define PB push_back 
#define MP make_pair 

#define FOR(i,a,b) for(int i=(a),_b=(b); i<_b; i++)
#define FORE(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define FORDE(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

#define REP(i,n) FOR(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v)) 

#define DEBUG 

#define NOP do {} while(0)

#if !defined(DEBUG)

#define dprintf(x...)   NOP
#define DOUT(x)         NOP
#define DCOLL(x)        NOP
#define DARR(x,n)       NOP

#else
#define DC(x) cout << "# "#x" = "
#define dprintf(x,...) printf("# " x "\n", ##__VA_ARGS__)
#define DOUT(x) DC(x) << x << endl;
#define DCOLL(x) do { DC(x);			\
        FOREACH(it,x){ cout << *it << " "; }	\
        cout << endl; } while(0)
#define DARR(x,n) do { DC(x);			\
        REP(i,n) { cout << x[i] << " "; }	\
        cout << endl; } while(0)
#endif

typedef long long ll;
typedef std::vector<ll> VL;
typedef std::vector<VL> VVL;

using namespace std;

static void solve_case(int i);

int main(void){
    int N;
    cin >> N;
    for(int i = 0; i < N; i++){
        solve_case(i+1);
    }
    return 0;
}

void cancellation(vector<char>& list, vector<string>& oppositions)
{
    FOREACH(it,oppositions){
	if(find(ALL(list), (*it)[0]) != list.end() &&
	   find(ALL(list), (*it)[1]) != list.end()){
	    list.clear();
	    return;
	} 
    }
}
void process_combinations(vector<char>& list, vector<string>& combinations)
{
    bool change = list.size() > 1;
    while(change){
	change = false;
	size_t s = list.size();
	if(s < 2)
	    return;
	FOREACH(cit,combinations){
	    char a = (*cit)[0];
	    char b = (*cit)[1];
	    char c = (*cit)[2];

	    if( (a == list[s-2] && b == list[s-1]) ||
		(b == list[s-2] && a == list[s-1])){
		list.pop_back();
		list.pop_back();

		list.push_back(c);
		change = true;
		break;
	    }
	}
    }

}
void solve_case(int cn){
    int com, opp, N;

    std::vector<string> combinations;
    std::vector<string> oppositions;
    std::vector<char> list;

    string tmp;

    cin >> com;
    REP(i,com){
	cin >> tmp;
	combinations.push_back(tmp);
    }

    cin >> opp;
    REP(j,opp){
	cin >> tmp;
	oppositions.push_back(tmp);
    }

    cin >> N;
    cin >> tmp;
    REP(k, tmp.size()){
	list.push_back(tmp[k]);
	process_combinations(list, combinations);
	cancellation(list, oppositions);
    }



    cout << "Case #" << cn << ": [";
    if(list.size() > 0){
	cout << list[0];
    } 
    REP(l, list.size()-1){
	cout << ", " << list[l+1];
    }
    cout << "]" << endl;
}
