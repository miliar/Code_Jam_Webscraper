#include <cstdio>
using namespace std; 

int pd, pg, n, a, b, c, d, T; 

int gcd(int a, int b){
	if (a > b) return gcd(b,a);
	if (a == 0) return b; 
	return gcd(b%a, a); 
}

bool work(){
	if (pg == 100 && pd < 100) return false; 
	if (pg == 0 && pd > 0) return false; 
	int div; 
	div = gcd(pd, 100);
	a = 100 / div; 
	b = pd / div; 
	div = gcd(pg, 100);
	c = 100 / div; 
	d = pg / div; 
	if (a > n) return false; 
	return true; 
}

int main(){
	//freopen("E:\\Algorithms\\GoogleJam\\GoogleJam\\input\\A-small-attempt0.in","r",stdin);
	//freopen("E:\\Algorithms\\GoogleJam\\GoogleJam\\input\\A-small-attempt0.out","w",stdout);
	bool result; 
	scanf("%ld", &T); 
	for (int i = 0; i < T; i++) {
		scanf("%ld %ld %ld", &n, &pd, &pg); 
		result = work();
		printf("Case #%ld: ", i + 1);
		if (result)	printf("Possible\n"); 
		else printf("Broken\n");
	}
	//fclose(stdin);
	//fclose(stdout); 
}