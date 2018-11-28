#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <vector>
#include <map>
#include <ctime>

using namespace std;

typedef long long ll;
const int N = 10005;


int id[N];
int n, __xs, __ys;
int r[N];
int __x[N], __y[N];

bool ok() 
{
    int ll = 0, right = __ys;
    int cur = r[id[0]], maxv = r[id[0]];
    __x[id[0]] = 0;
    __y[id[0]] = 0;
    for (int i = 1; i < n; ++i) 
    {
        if (cur + r[id[i]] <= __xs) 
	{
            __x[id[i]] = cur + r[id[i]];
            __y[id[i]] = ll;
            cur += 2 * r[id[i]];
            maxv = max(maxv, r[id[i]]);
            //cout << cur << endl;
        } 
	else 
	{
            ll += maxv;
            maxv = r[id[i]];
            ll += maxv;
            __x[id[i]] = 0;
            __y[id[i]] = ll;
            cur = r[id[i]];
            if (ll > right) return false;
        }
    }
    return true;
}

bool cmp(const int a, const int b) {
    return r[a] > r[b];
}

int main() {
    int cas, tcas = 0;

    for (cin >> cas; cas; --cas) {
        printf("Case #%d: ", ++tcas);
        scanf("%d%d%d", &n, &__xs, &__ys);
        for (int i = 0; i < n; ++i) {
            scanf("%d", r + i);
            id[i] = i;
        }

        sort(id, id + n, cmp);

        if (ok()) {
            for (int i = 0; i < n; ++i) {
                if (i) putchar(' ');
                printf("%d %d", __x[i], __y[i]);
            }
            puts("");
        } else 
	{

		swap(__xs, __ys);
		for (int i = 0; i < n; ++i)
			swap(__x[i], __y[i]);
		if(ok()) {
			for (int i = 0; i < n; ++i) {
				if (i) putchar(' ');
				printf("%d %d", __x[i], __y[i]);
			}
			puts("");
		}
	}
    }
}
