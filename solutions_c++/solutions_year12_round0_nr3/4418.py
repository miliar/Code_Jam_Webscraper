#include <stdio.h>


bool check(int a, int b) {
if (b >= 10 && b < 100) {
if (a == b / 10 + b % 10 * 10) return true;
} else if(b >= 100) {
if (a == b / 10 + b % 10 * 100) return true;
if (a == a / 100 + b % 100 * 10) return true;
}
return false;
}

int main(){
int tc;
scanf("%d", &tc);
for (int t = 1; t <= tc; t++) {
int a, b;
scanf("%d %d", &a, &b);
int sum = 0;
for (int i = a; i <= b; i++){
for (int j = i + 1; j <= b; j++) {
if (check(i, j)) {
sum++;
}
}
}
printf("Case #%d: %d\n", t, sum);
}
return 0;
}
