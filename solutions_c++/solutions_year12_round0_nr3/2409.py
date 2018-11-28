#include <cstdio>

int a, b, len;

int buf[64];

int get(int tmp) {
	int sum = 0;
	int flag= tmp;
	int x = tmp;
	while (flag) {
		flag/= 10;
		if (x%10){
			x = (x%10)*len + x/10;
			//printf("%d %d\n", tmp, x);
			if (x>tmp && x<=b) {
				int j=0;
				while (j<sum) {
					if (buf[j] == x) {
						break;
					}
					j++;
				}
				if (j==sum){	
					buf[sum++]=x;
				}
			}
		}else {
			x /= 10;
		}
	}
	return sum;
}

int main(int argc, char const *argv[])
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, sum, x;
	scanf("%d", &t);
	x = 0;
	while (x++ < t) {	
		scanf("%d %d\n", &a, &b);
		int tmp = a;
		len = 1;
		while (tmp /= 10) {
			len *= 10;
		}
		sum = 0;
		tmp = a;
		while (tmp < b) {
			sum += get(tmp);
			++tmp;
		}	
		printf("Case #%d: %d\n", x,sum);
	}
	return 0;
}