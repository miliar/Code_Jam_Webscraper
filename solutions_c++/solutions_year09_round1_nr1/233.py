#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

char s[1024];
int b[10], len;
bool v[1000000];
bool Solve(int n, int base){
	if(n == 1)  return true;
	if(v[n])  return false;
	v[n] = true;
	int ret = 0;
	while(n){
		int now = n % base;
		n /= base;
		ret += now * now;
	}
	return Solve(ret, base);
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	int i, j, k;
	scanf("%d", &t);
	getchar();
	for(int tt = 1; tt <= t; tt++){
		len = 0;
		memset(v, 0, sizeof(v));
		gets(s);
		for(char *tmp = strtok(s, " "); tmp != NULL; tmp = strtok(NULL, " "))
					b[len++] = atoi(tmp);
		for(i = 2; ;i++){
			for(j = 0; j < len; j++){
				memset(v, 0, sizeof(v));
				if(!Solve(i, b[j]))
					break;
			}
			if(j >= len)
				break;
		}
		printf("Case #%d: %d\n", tt, i);
	}

	return 0;
}
