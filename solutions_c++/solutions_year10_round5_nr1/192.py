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

#define MAX 1024

using namespace std;
FILE *in; FILE *out;

struct RNG
{
    int a, b, p;
};

int isPrime(int num)
{
    if (num < 2) return 0;
    for (int i = 2; i * i <= num; i++)
        if (num % i == 0) return 0;
    return 1;
}

void doWork(int testNum)
{
	int d, k;
	vector <int> v; int tmp;
	
	fscanf(in, "%d %d", &d, &k);
	for (int i = 0; i < k; i++)
	{
        fscanf(in, "%d", &tmp);
        v.push_back(tmp);
    }
	int lim = 1;
	for (int i = 0; i < d; i++) lim *= 10;
	
	set <int> ans;
	int maxx = 2;
	for (int i = 0; i < k; i++) maxx = max(maxx, v[i] + 1);
	for (int p = maxx; p <= lim; p++) if (isPrime(p))
	{
        for (int a = 0; a < p; a++)
        {
            int good = 1, b = -1;
            for (int i = 0; i < k - 1; i++)
            {
                int next = (v[i + 1] - (v[i] * a) % p + p) % p;
                if (b == -1) b = next;
                if (next != b) {good = 0; break;}
            }
            if (good && b != -1) ans.insert((v.back() * a + b) % p);
            if (ans.size() > 1) break;
        }
        if (ans.size() > 1) break;
    }
    if (ans.size() == 0 || ans.size() > 1)
        fprintf(out, "I don't know.\n");
    else
    {
        vector <int> prnt(ans.begin(), ans.end());
        fprintf(out, "%d\n", prnt[0]);
    }
	
	return;
}

int main(void)
{
	int tests, i;
	
	in = fopen("DeRNG.in", "rt");
	out = fopen("DeRNG.out", "wt");
	
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
