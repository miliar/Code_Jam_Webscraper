#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int num[1009]; 
int n;
bool cmp(const int a, const int b){
	return a > b;
}
void solve(int cas){
	
	int i, ans = 0;
	scanf ("%d", &n);
	for(i = 0; i < n;i ++)
		scanf ("%d", &num[i]);
	for(i = 0; i < n; i ++){
		ans ^= num[i];
	}
	if(ans != 0 ) {
		printf ("Case #%d: NO\n", cas); return ;
	}
	sort(num, num+n, cmp);
	ans = 0;
	for(i = 0; i < n-1; i ++)
		ans += num[i];
	printf ("Case #%d: %d\n", cas, ans);
	return ;

}
int main()
{
	int t;
	int i;
	freopen("C-large.in","r", stdin);
	freopen("C-large.out","w", stdout);
	scanf("%d", &t);

	for(i = 1; i <= t; i ++){
		solve(i);
	}
}