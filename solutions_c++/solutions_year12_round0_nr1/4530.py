/* Author       :        Arpit Sood
 * Algorithm    :        bruteforce mapping
 * */
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <queue>
#include <cstdio>
#include <cmath>
#include <climits>

using namespace std;

#define FOR(i,a,b) for(int i = (a) ; i < (b) ; i ++ ) 
#define FOR0(i,a) for(int i = 0 ; i < (a) ; i ++ ) 
#define FOR1(i,a) for(int i = 1 ; i < (a) ; i ++ )
#define REP(i,a,b,c) for(int i = (a) ; i < (b) ; i+= (c) ) 
#define PRINT printf 
#define PB push_back
#define MP make_pair
#define all(c) (c).begin(),(c).end()
#define present(c,x) (find(all(c),x) != (c).end())
#define SQ(x) (x)*(x)
#define INF 0xffffff00
#define ESP 1e-6
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define MININ(a) *min_element(a.begin(), a.end())
#define MININ_A(a,n) *min_element(a, a+n)
#define MAXIN(a) *max_element(a.begin(), a.end())
#define MAXIN_A(a,n) *max_element(a, a+n)

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef vector<int> vi;

// Unlike lower_bound, upper_bound function does not return an 
// iterator to the element if it compares equivalent to value,
// but only if it compares strictly greater.

bool comparator(const ii& left, const ii& right)
{
    if(left.second == right.second)
        return left.first < left.second;
    
    return left.second < right.second;
}

int main()
{
       int n = 0, k, c, t;
       char str[105];
       cin >> t;
       getchar();
       map<char, char> mp;
       mp['a'] = 'y';
       mp['b'] = 'h';
       mp['c'] = 'e';
       mp['d'] = 's';
       mp['e'] = 'o';
       mp['f'] = 'c';
       mp['g'] = 'v'; 
       mp['h'] = 'x';
       mp['i'] = 'd';
       mp['j'] = 'u';
       mp['k'] = 'i';
       mp['l'] = 'g';
       mp['m'] = 'l';
       mp['n'] = 'b';
       mp['o'] = 'k';
       mp['p'] = 'r';
       mp['q'] = 'z'; 
       mp['r'] = 't';
       mp['s'] = 'n';
       mp['t'] = 'w';
       mp['u'] = 'j';
       mp['v'] = 'p';
       mp['w'] = 'f';
       mp['x'] = 'm';
       mp['y'] = 'a';
       mp['z'] = 'q';
       mp[' '] = ' ';
       while(t--)
       {
           n++;
           scanf("%[^\n]", str);
           getchar();
           cout << "Case #" << n << ": ";

           FOR0(i, strlen(str))
               cout << mp[str[i]];
           
           cout << endl;
       }
       return 0;
}
