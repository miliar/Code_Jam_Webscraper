#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

char a[1005];
string good[50];
string bad[50];

int c,d,n,len;

int combine(int k)
{
    if (k==0) return 0;
    char x = a[k-1];
    char y = a[k];
    For(i, 0, c-1)
    if((good[i][0] == x && good[i][1] == y) || (good[i][0] == y && good[i][1] == x))
    {
                  a[k-1]=good[i][2];
                  return combine(k-1);
    }
    return k;
}

int oppo(int k)
{
    char x = a[k];
    For(i, 0, d-1)
    {
        if (bad[i][0] == x)
            For(j, 0, k-1)
            {
                   if(bad[i][1] == a[j]) return -1;
            }
        else if (bad[i][1] == x)
            For(j, 0, k-1)
            {
                   if(bad[i][0] == a[j]) return -1;
            }
    }
    return k;
}


int main() {
	freopen("B-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

    int t,i;

	scanf("%d", &t);
	For(test, 1, t)
    {
        cin>>c;
        For(i, 0, c-1) cin>>good[i];
        cin>>d;
        For(i, 0, d-1) cin>>bad[i];
        cin>>n;
        len = 0;
        For(i, 0, n-1)
        {
               cin>>a[len];
               len = combine(len);
               len = oppo(len);
               //printf("%d   ", len);
               //For(j, 0, len) printf("%c, ",a[j]);printf("\n");
               len++;
        }
		printf("Case #%d: [", test);
		if (len == 0) printf("]\n");
		else
		{

    		For(i, 0, len-2) printf("%c, ",a[i]);
    		printf("%c]\n", a[len-1]);
      }
	}

	exit(0);
}
