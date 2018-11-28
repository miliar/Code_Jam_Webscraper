#include<cstdio>
#include<algorithm>

using namespace std;

int casos, n, a, x1, x2, sp, ans, lim;

int normal(int a){
	if(a%3 == 0) return a/3;
	if(a%3 == 1) return (a/3) + 1;
	if(a%3 == 2) return (a/3) + 1;
}

int super(int a){
	if(a == 0) return 0;
	if(a%3 == 0) return (a/3) + 1;
	if(a%3 == 1) return (a/3) + 1;
	if(a%3 == 2) return (a/3) + 2;
}

int main(){
	scanf(" %d", &casos);
	for(int inst=1;inst<=casos;inst++){
	scanf(" %d %d %d", &n, &sp, &lim);
	ans = 0;
	for(int i=0;i<n;i++){
		scanf(" %d", &a);
		x1 = normal(a);
		x2 = super(a);
		if(x1 >= lim) ans++;
		else if(x2 >= lim && sp > 0){
			ans++;
			sp--;
		}
	}
	printf("Case #%d: %d\n", inst, ans);
	}
	return 0;
}

