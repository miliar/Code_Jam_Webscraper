#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>

#define MAX 128
#define MM MAX*MAX
#define INF 1000000000000000000LL

using namespace std;
FILE *in; FILE *out;

int n;
int a[MAX];
long long dyn[MM];
long long L;


string toString(long long num)
{
    if (num == 0) return "0";
    string ret;
    while (num) {ret.push_back(num % 10 + 48); num /= 10;}
    reverse(ret.begin(), ret.end());
    return ret;
}

void doWork(int testNum)
{
	char buff[MAX];
	fscanf(in, "%s %d", buff, &n);
	L = 0;
	for (int i = 0; i < (int)strlen(buff); i++)
	   L = L * 10 + buff[i] - 48;
	
	for (int i = 0; i < n; i++)
	   fscanf(in, "%d", &a[i]);
	sort(a, a + n);
	
	dyn[0] = 0;
	for (int i = 1; i < MM; i++)
	{
        dyn[i] = INF;
        for (int c = 0; c < n; c++) if (a[c] <= i)
            dyn[i] = min(dyn[i], dyn[i - a[c]] + 1);
    }
	
	long long ans = L + 1;
	for (int i = n - 1; i >= 0; i--)
	{
        long long mult = -1;
        long long left = 0, right = L / a[i];
        while (left <= right)
        {
            long long mid = (left + right) / 2;
            if (L - mid * a[i] < MM) {mult = mid; break;}
            else left = mid + 1;
        }
        long long tmp = mult + dyn[L - mult * a[i]];
        ans = min(ans, tmp);
    }
    if (ans > L) fprintf(out, "IMPOSSIBLE\n");
    else fprintf(out, "%s\n", toString(ans).c_str());	
	return;
}

int main(void)
{
	int tests, i;
	
	in = fopen("Fence.in", "rt");
	out = fopen("Fence.out", "wt");
	
	fscanf(in, "%d", &tests);
	for (i=0; i<tests; i++)
	{
        cout << "Currently calculating test " << i << endl;
		fprintf(out, "Case #%d: ", i+1);
		doWork(i + 1);
	}
	cout << "Finished calculating tests!" << endl;
	system("pause");
	return 0;
}
