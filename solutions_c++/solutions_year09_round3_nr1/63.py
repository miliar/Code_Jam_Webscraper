#include <cstdio>
#include <cstring>
#include <iostream>
#include <sstream>
using namespace std;

int num[36];
char buf[100];

int main()
{
	int N_;
	scanf("%d\n", &N_);
	for (int n_=1; n_<=N_; ++n_) {
		memset(num, -1, sizeof(num));
		scanf("%s", buf);
		int len = strlen(buf);
		int c_base = 1;
		int base = 1;
		bool zero_used = false;
		for (int i=0; i<len; ++i) {
			int index; 
			if (buf[i]>='0' && buf[i]<='9') {
				index = buf[i] - '0';
			} else {
				index = buf[i] -'a' + 10;
			}
			if (num[index] != -1) {

			} else {
				if (i!=0 && !zero_used) {
					num[index] = 0;
					zero_used = true;
				} else {
					num[index] = c_base;
					++c_base;
				}
			}
		}
		base = c_base;
		unsigned long long int sum = 0;
		for (int i=0; i<len; ++i) {
			sum *= base;
			int index; 
			if (buf[i]>='0' && buf[i]<='9') {
				index = buf[i] - '0';
			} else {
				index = buf[i] -'a' + 10;
			}
			if (num[index] != -1) {
				sum += num[index];
			} else {
				printf("!!!\n");
			}
		}
		printf("Case #%llu: %d\n", n_, sum);
	}
	return 0;
}

