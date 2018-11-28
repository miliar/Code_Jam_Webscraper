
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<cstring>
#include<stack>
#include<sstream>
#include<complex>
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define DEBU true
#define debug(x) { if (DEBU) cerr << #x << " = " << x << "\n"; }
#define debugv(x) { if (DEBU) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; } }
#define fup(i,a,b) for(int i=(a);i<=(b);i++)
#define fdo(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof (x))
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) ((int)a.size())
#define inf 1000000000
#define SQR(a) ((a)*(a))

using namespace std;
typedef long long lli;
typedef double ld;
string in[] = {
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up"
};

string out[] = {
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

char co[200];
bool tak[200];
int main() {
   // co['z'] = 'q';
   // tak['q'] = 1;
    //co['d'] = 'z';
    //co['q'] = 'q';
    co['z'] = 'q';
    co['q'] = 'z';

    fup(i, 0, 2) {
        string a, b;
        a = in[i];
        b = out[i];
        fup(j, 0, siz(a) - 1) {
            if (a[j] != ' ') { 
                co[b[j]] = a[j]; tak[b[j]] = 1;} 
        }
    }
    //fup(i, 'a', 'z') cout << (char)i << " " << (char)co[i] << " " << tak[i] << endl;
    int cas;
    scanf("%d", &cas);
    char c;
    scanf("%c", &c);
    fup(c, 1, cas) {
        string x;
        getline(cin, x);
        fup(i, 0, siz(x) - 1) if (x[i] != ' ') x[i] = co[x[i]];
        cout << "Case #" << c << ": ";
        cout << x << endl;

    }
	return 0;
}

