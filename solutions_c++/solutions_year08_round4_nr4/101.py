#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

#define maxn 11000
#define maxm 1000000
#define eps 1e-8

using namespace std;

typedef long long int64;

typedef double real;

int per[maxn];
char buff[1 << 20];
char temp[1 << 20];
int k;


int calc(){
 	memset(temp, 0, sizeof(temp));
 	int len = strlen(buff);
 	int i;
 	for (i = 0; i < len; i++) temp[i] = buff[k * (i / k) + per[i % k]];
 	int res = 1;
 	for (i = 1; i < len; i++) if (temp[i] != temp[i - 1]) ++res;
 	return res;
}


int main() {
	int ferlon;
	scanf("%d", &ferlon);
	int _;
	for (_ = 0; _ < ferlon; ++_){
		scanf("%d\n", &k);
		gets(buff);
		int i;
		for (i = 0; i < k; i++) per[i] = i;
		int ans = maxm;
		do{
			int tmp = calc();
			if (tmp < ans) ans = tmp;
/*			if (tmp == 9){
			 	for (i = 0; i < k; i++) std::cerr << per[i] << ' ';
			 	std::cerr << std::endl << temp << std::endl;
			}
*/
	   	}while (next_permutation(per, per + k));
		printf("Case #%d: %d\n", _ + 1, ans);
	}
	return 0;
}
