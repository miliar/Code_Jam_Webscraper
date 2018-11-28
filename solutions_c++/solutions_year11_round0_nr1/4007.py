#include <algorithm>
#include <cmath>
#include <cstdio>
using namespace std;

void solve(int num)
{
	int i, n, button, blue = 1, orange = 1, bluetime = 0, orangetime = 0, time = 0;
	char color;
	scanf("%d", &n);
	for(i = 0; i < n; i++) {
		scanf(" %c%d", &color, &button);
		if(color == 'O') {
			orangetime += abs(button - orange) + 1;
			time = max(time + 1, orangetime);
			orangetime = time;
			orange = button;
		} else {
			bluetime += abs(button - blue) + 1;
			time = max(time + 1, bluetime);
			bluetime = time;
			blue = button;
		}
	}
	printf("Case #%d: %d\n", num, time);
}
	

int main(void)
{
	int i, n;
	scanf("%d", &n);
	for(i = 0; i < n; i++)
		solve(i + 1);
	return 0;
}
