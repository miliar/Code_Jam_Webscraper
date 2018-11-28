#include<iostream>
#include<stack>
#include<queue>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
#include<cstring>
#include<map>
#include<numeric>
#include<sstream>
#include<cmath>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i = x; i<y; i++ )
#define FORV(it,A) for(vector<int>::iterator it = A.begin(); it!= A.end(); it++)
#define FORS(it,A) for(set<int>::iterator it = A.begin(); it!= A.end(); it++)
#define quad(x) (x) * (x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;

#define inf 
#define N

char s[1000];

int V[] = {24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25,19, 13, 22, 9, 15, 5, 12, 0, 16};

void limpa (){
    char c = getchar();
    while (c != '\n') c = getchar();
}

int main (){
    int n; scanf("%d", &n);
    limpa ();
    set <char> S;
    f (t, 0, n) {
        fgets (s, 1000, stdin);
        int sz = strlen(s);
        f (i, 0, sz) if (s[i] >= 'a' && s[i] <= 'z'){
            int x = s[i]-'a';
            s[i] = V[x]+'a';
        }
        printf("Case #%d: %s", t+1, s);
    }

	return 0;
}
