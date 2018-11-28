#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:16777216")
#include <ctime>
#include <string> 
#include <vector> 
#include <map> 
#include <list> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <stack> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <cstdlib> 
#include <cstdio> 
#include <cctype> 
#include <algorithm> 
#include <utility> 
using namespace std; 
typedef vector<int> vi; 
typedef vector<string> vs; 
typedef pair<int,int> pii; 
typedef long long ll; 
typedef istringstream iss;
#define FOR(i,f,n) for(int i=f; i<n; ++i) 
#define sz(a) ((int)a.size()) 
#define fill(w,v) memset(w,v,sizeof(w)) 
#define pb push_back 
#define all(a) a.begin(),a.end()
#define mp make_pair 
#define inf 1000000000 
#define X first
#define Y second
template<class T> inline T gcd(T a, T b){T t; while (a && b) t = a, a = b%a, b = t; return a+b; }
template<class T> inline T power(T a, int p) {T r = T(1); while (p) { if (p&1) r = r*a; a = a*a; p >>= 1; } return r; }
template<class T> T extgcd(T a, T b, T& x, T& y) { if (b==0) return x=1, y=0, a; T x1, y1, g; g = extgcd(b, a%b, x1, y1); x = y1; y = x1 - a/b*y1; return g; }
template<class T> inline T Floor(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return (a-b+1)/b; return a/b; }
template<class T> inline T Ceil(T a, T b) { if (b<0) a=-a, b=-b; if (a<0) return a/b; return (a+b-1)/b; }
int N, M, K,L, A;
char buf[10000], buftmp[10000];
char buf2[10000];
double calc(istringstream& iss, set<string>& features)
{
    char c;
    iss >> c;
    double w;
    iss >> w;
    iss >> c;
    if (c == ')')
    {
        //iss >> c;
        return w;
    }

    string f;
    if (!(iss.peek() == ' ' || iss.peek() == ')'))
    {
        iss >> f;
    }
    f = c + f;    
    if (features.count(f))
    {
        double d = calc(iss, features);
        calc(iss,features);
        iss >> c;
        return w * d;
    }
    else
    {
        calc(iss,features);
        double d = calc(iss,features);
        iss >> c;
        return w * d;
    }
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	clock_t startTime = clock();

	int Cases;
	scanf("%d", &Cases);
	FOR(Case,0,Cases)
	{
		printf("Case #%d:\n", Case+1);
		fprintf(stderr, "Case #%d:\n", Case+1);

        scanf("%d\n", &L);
        string s;
     
        FOR(i,0,L)
        {
            gets(buf);
            s += ' ';
            s += buf;
        }
        scanf("%d\n", &A);
        FOR(i,0,A)
        {
            gets(buf2);
            istringstream is(buf2);
            string name;
            int n;
            set<string> feat;
            is >> name >> n;
            FOR(j,0,n) 
            {
                string tmp;
                is >> tmp;
                feat.insert(tmp);
            }
            double p = calc(istringstream(s), feat);
            printf("%.7lf\n", p);
            fprintf(stderr, "%.7lf\n", p);
        }
	}

	clock_t endTime = clock();
	fprintf(stderr, "\nTime: %.3lf\n", double(endTime-startTime)/CLOCKS_PER_SEC);
	return 0;
} 
