#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <math.h>


#define abs(x) ((x) >= 0 ? (x) : -(x))
#define bit_clear (a, b) ((a) & ~((uinteger)1 << (b)))
#define bit_set (a, b) ((a) | ((uinteger)1 << (b)))
#define bit_test (a, b) ((a) >> (b) & 1)

#define max (a, b) ((a) >= (b) ? (a) : (b))
#define min (a, b) ((a) <= (b) ? (a) : (b))

using namespace std;
int is_prime(int n){
	for (int i=2; i<n; i++)
		if ((n%i)==0) return 0;
	return 1;

}

int main(int argc, char *argv[])
{
	int lines;
	std::cin >> lines;
	int SET[1000003];

	for (int i=0;i<lines;i++) {
		int A,B,P;
		std::cin >> A >> B >> P;
		int snum=1;
		for (int k=0; k<B-A+2; k++)
			SET[k]=0;
		for (int k=P; k<=B-A; k++) 
			if (is_prime(k)==1){
			int s=0;
			int f=0;
			for (int j=((A-1)/k)*k+k;j<=B;j+=k) {
				if (SET[j-A]!=0)
					s=SET[j-A];
				f++;
//				printf("%d %d %d\n",j,k,f);
				}
			if (f>1) {
				if (s==0) {
					s=snum;
					snum++;
				}
				for (int j=((A-1)/k)*k+k;j<=B;j+=k)
					SET[j-A]=s;

				}

		}
		for (int k=A; k<=B; k++) {
			if (SET[k-A]==0) snum++;
//			printf("%d %d\n", k, SET[k-A]);
			}
		printf("Case #%d: %d\n",i+1,snum-1);
	}
	return 0;
}
