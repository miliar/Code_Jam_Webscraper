#include <stdio.h>

int Gcd(int x, int y){
	return y ? Gcd(y, x % y) : x;
}

int Get_D(int x, int n){
	int b;
	b = Gcd(x, 100);
	b = 100 / b;
	if(b <= n) return b;
	return -1;
}

int Ext_Gcd(int a, int b, int &x, int &y){
	if(b == 0){
		x = 1, y = 0;
		return a;
	}
	int r = Ext_Gcd(b, a % b, x, y);
	int t = x; 
	x = y, y = t - a / b * y;
	return r;
}

int main(){
	int a, b, Pd, Pg, d, n, falg, x, y, yue, a2, b2;
	int CASE, t;
	freopen("A-small-attempt1.in", "r", stdin);
	//freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &CASE);
	for(t = 1; t <= CASE; t ++){
		scanf("%d %d %d", &n, &Pd, &Pg);
		d = Get_D(Pd, n);
		a = (d * Pd) / 100;
		b = 100 * a - Pg * d;
		yue = Ext_Gcd(Pg, 100, x, y);
		if(d == -1 || b % yue){
			printf("Case #%d: Broken\n", t);
			continue;
		}
		falg = 0;
		x = (x * (b/yue) % 100 + 100) % (100 / yue);
		a2 = Pg / yue;
		b2 = Pg / yue;
		for(int k = 1; k <= yue; k ++){
			int xx = x + k * b2;
			y = - (b - Pg * xx) / 100;
			if(y >= 0 && y <= xx){
				falg = 1;
				break;
			}
		}
		if(falg)	printf("Case #%d: Possible\n", t);
		else	printf("Case #%d: Broken\n", t);
	}
	return 0;
}