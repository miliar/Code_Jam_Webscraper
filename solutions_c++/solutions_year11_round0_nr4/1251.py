#include <iostream>
using namespace std;

int num[1000+10];
int mark[1000+10];
double cd[1010];
double work(int t){
	int i, j;
	double ans = 0, cc;
	for( i = 1; i <= 1000; i ++){
		cc = i*1.0/t;
		double pp = (t-1)*1.0/t;
		for( j = 1; j < i; j ++){
			cc *= pp;

		}
		ans += cc;
	}
	return ans;
}
void solve(int k){
	int n, i, j, cnt;
	double ans  = 0;
	scanf ("%d", &n);
	memset(mark, 0, sizeof(mark));
	for(i = 1; i <= n; i ++)
		scanf ("%d", &num[i]);
	for(i = 1; i <= n;i ++)
	{
		if(num[i] == i ||mark[i] == 1) continue;
		int t = num[i]; cnt = 1;
		while(t != i){
			mark[t] = 1;
			t = num[t];
			cnt ++;
		}
		ans += cd[cnt];
		
	}
	printf ("Case #%d: %.6lf\n", k, ans);
}
int main()
{
	int t, i, j;
	for(i = 2; i <= 1000; i ++){
		cd[i] = work(i);
	}
	freopen("D-small-attempt2.in","r", stdin);
	freopen("D-small-attempt2.out","w", stdout);
	/*freopen("d:\\out.out","w", stdout);
	
	for(int k = 2; k <= 1000; k ++ ){
		double c = 0;
		for(i = 1; i <= 1000; i ++)
		{
			double tt = 1/k;
			double qq = (i-1)/k;
			for(j = 1; j < i; j ++)
			{
				tt *= qq;
			}
			c += tt*;
		}
		printf ("%.7lf,", c);
	}*/
	scanf ("%d", &t);
	for(i = 1; i <= t; i ++)
	{
		solve(i);
	}
	return 0;
}