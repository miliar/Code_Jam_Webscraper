#include <stdio.h>

void solve(int case_no)
{
	int n, ans = 0;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++) {
		int num;
		scanf("%d", &num);
		if(num != i)
			ans++;
	}
	printf("Case #%d: %.6lf\n", case_no, (double)ans);
}


int main() {
	int cases_count;
	scanf("%d", &cases_count);
	for(int i = 1; i <= cases_count; i++)
		solve(i);
	return 0;

}
