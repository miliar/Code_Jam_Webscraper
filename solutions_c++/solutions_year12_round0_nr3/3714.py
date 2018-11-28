#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int A,B,d,res,high,shifted;
char tmp[10];
int ten[7] = {1,10,100,1000,10000,100000,1000000};

int main() {
	int cases,cn=0;
	scanf("%d",&cases);
	while (cases--) {
		scanf("%d%d",&A,&B);
		sprintf(tmp,"%d",A);
		d = strlen(tmp);
		res = 0;
		for (int at=A; at <= B; ++at) {
			shifted = at;
			for (int k=1; k < d; ++k) {
				high = shifted%10;
				shifted = (shifted/10) + high*ten[d-1];
				if (shifted == at) break;
				else if (shifted > at && shifted <= B) ++res;
			}
		}
		printf("Case #%d: %d\n",++cn,res); fflush(stdout);
	}
	return 0;
}
