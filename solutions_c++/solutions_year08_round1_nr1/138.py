#include <cstdio>
#include <algorithm>
#include <functional>

int a[900], b[900];

int main(){
    int nc;
    scanf(" %d", &nc);
    for(int cc = 1; cc <= nc; ++cc){
	int len;
	scanf(" %d", &len);

	for(int i = 0; i < len; ++i)
	    scanf(" %d", &a[i]);
	for(int i = 0; i < len; ++i)
	    scanf(" %d", &b[i]);

	std::sort(a, a + len, std::greater<int>());
	std::sort(b, b + len, std::less<int>());

	long long int product = 0;
	for(int i = 0; i < len; ++i)
	    product += a[i] * b[i];

	printf("Case #%d: %lld\n", cc, product);
    }
}
