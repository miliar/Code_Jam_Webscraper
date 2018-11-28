#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cassert>

using namespace std;

double res[1010];
double sum[1010];
int a[1010];
bool byl[1010];

int main()
{
	sum[1] = 0; res[1] = 0;
	for(int i=2; i<=1000; ++i){
		res[i] = (sum[i-1] + 1.0) * i / (i-1);
		sum[i] = sum[i-1] + res[i] / i;
	}
	int cases;
	scanf("%d", &cases);
	for(int gi=1; gi<=cases; ++gi){
		int n;
		scanf("%d", &n);
		assert(n <= 1000);
		for(int i=1; i<=n; ++i) scanf("%d", &a[i]);
		double S = 0.0;
		memset(byl, false, sizeof(byl));
		for(int i=1; i<=n; ++i){
			if(byl[i]) continue;
			int ile = 0;
			int wsk = i;
			while(!byl[wsk]){
				byl[wsk] = true;
				ile++;
				wsk = a[wsk];
			}
			S += res[ile];
		}
		
		printf("Case #%d: %.8lf\n", gi, S);
	}
	return 0;
}
