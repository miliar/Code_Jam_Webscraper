#include <cstdio>
#include <iostream>

using namespace std;

int t, n, num, x, y;
char ch;
int a[2000], b[2000];
int ar[2000];

int main () {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tc = 0;
    scanf("%d", &t);
	while(t--){
		x = y = 0;
		scanf("%d %c %d", &n, &ch, &num);
		
		if(ch == 'O'){
			ar[0] = 0;
			a[x++] = num;
		}
		else{
			ar[0] = 1;
			b[y++] = num;
		}
		
		for(int i = 0; i < n-1; i++){
			scanf(" %c %d", &ch, &num);
			if(ch == 'O'){
				ar[i+1] = 0;
				a[x++] = num;
			}
			else{
				ar[i+1] = 1;
				b[y++] = num;
			}
		}
		
		int j, k, l, px, py;
		int ans = 0;
		j = k = l = 0;
		px = py = 1;
		while (j < n) {
			if(!ar[j]){
				int ta = abs(a[k] - px) + 1;
				int tb = min(ta, abs(b[l] - py));
				ans += ta;
				px = a[k++];
				py += tb * (py > b[l] ? -1 : 1);
			}
			else {
				int tb = abs(b[l] - py) + 1;
				int ta = min(tb, abs(a[k] - px));
				ans += tb;
				py = b[l++];
				px += ta * (px > a[k] ? -1 : 1);
			}

			j++;
		}
		
		printf("Case #%d: %d\n", ++tc, ans);
	}
    return 0;
}
