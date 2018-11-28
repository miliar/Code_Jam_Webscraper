#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

const long long inf = 1e18;

int b[1000005];
long long a[1000005], m[1000005];
bool f[1000005];
int l, n, c;
long long t;

bool cmp(int d1, int d2){
	return (m[d1] > m[d2]);
}

void game(){
	long long curt = 0, ost = 0;
	int i, j, kol;
	bool f0 = false;
	for (i = 0;i < n;i++){
		f[i] = false;
	}
	for (i = 0;i < n;i++){
		if (curt + a[i] > t){
			break;
		}
		curt += a[i];
	}
	if (i == n){
		printf("%lld",curt);
		return ;
	}
	long long pred = curt;
	ost = (pred + a[i]) - t;
	if (ost == 0){
		i--;
	}
	curt += t - curt;
	kol = n - i;
	for (j = i + 1;j < n;j++){
		m[j - i - 1] = a[j];
		b[j - i - 1] = j - i - 1;
	}
	if (l < kol){
		sort(b, b + kol - 1, cmp);
		for (i = 0;i < l - 1;i++){
			f[b[i]] = true;
		}
		if (ost > m[b[l - 1]]){
			f0 = true;
		}else
		{
			f[b[l - 1]] = true;
		}
	}else
	{
		f0 = true;
		for (i = 0;i < kol - 1;i++){
			f[i] = true;
		}
	}
	if (f0 == true){
		curt += ost / 2;
	}else
	{
		curt += ost;
	}
	for (i = 0;i < kol - 1;i++){
		if (f[i]){
			curt += m[i] / 2;
		}else
		{
			curt += m[i];
		}
	}
	printf("%lld",curt);
}

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int test, t1, i;
	scanf("%d\n",&test);
	for (t1 = 0;t1 < test;t1++){
		if (t1)
			printf("\n");
		printf("Case #%d: ",t1 + 1);
		scanf("%d%lld%d%d",&l,&t,&n,&c);
		if (l == 0){
			t = inf;
		}
		for (i = 0;i < c;i++){
			scanf("%lld",&a[i]);
			a[i] *= 2;
		}
		for (i = c;i < n;i++){
			a[i] = a[i - c];
		}
		game();
	}
	return 0;
}