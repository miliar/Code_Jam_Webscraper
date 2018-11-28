#include<cstdio>
#include<algorithm>
using namespace std;

int main(){
	int t; scanf("%d",&t);
	for (int tc = 1; tc <= t; tc += 1) {
		int n; scanf("%d",&n);
		int angka[n];
		for (int i = 0; i < n; i += 1) {
			scanf("%d",&angka[i]);
		}
		int hasil=-1;
		for (int x = 1; x < (1<<(n-1)); x += 1) {
			int sum1=0,sum2=0,xor1=0,xor2=0;
			for (int i = 0; i < n; i += 1) {
				if((1<<i)&(x)){
					sum1 += angka[i];
					xor1 ^= angka[i];
				} else {
					sum2 += angka[i];
					xor2 ^= angka[i];
				}
			}
			if(xor1==xor2) hasil = max(hasil,max(sum1,sum2));
		}
		printf("Case #%d: ",tc);
		if (hasil!=-1) printf("%d\n",hasil);
		else printf("NO\n");
	}
	return 0;
}
