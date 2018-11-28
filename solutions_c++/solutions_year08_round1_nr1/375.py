#include <stdio.h>
#include <algorithm>
using namespace std; 
int tcnt, n1[1020], n2[1020]; 
int go()
{ 
	int n, i; 
	scanf("%d", &n); 
	for (i = 0; i < n; i++) 
		scanf("%d", &n1[i]), n1[i] = -n1[i]; 
	for (i = 0; i < n; i++) 
		scanf("%d", &n2[i]); 
	sort(n1, n1 + n); 
	sort(n2, n2 + n); 
	for (i = 0; i < n; i++) 
		n1[i] = -n1[i]; 
	/*for (i = 0; i < n && n1[i] > 0 && n2[i] < 0; i++)
		ans += n1[i] * n2[i]; 
	for (j = n - 1; j >= 0 && n1[i] < 0 && n2[i] > 0; j--) 
		ans += n1[i] * n2[i]; 
	for (k = i; k <= j; k++) */
	int ans = 0; 
	for (i = 0; i < n; i++) 
		ans += n1[i] * n2[i]; 
	printf("Case #%d: %d\n", ++tcnt, ans); 
}
int main()
{ 
	freopen("A-small-attempt0.in", "r", stdin); 
	freopen("ans.txt", "w", stdout); 
	int T; 
	tcnt = 0; 
	scanf("%d", &T); 
	while (T--) 
		go();
	return 0; 
}
