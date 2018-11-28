#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

int N = -1;
unsigned int *c_i1 = NULL;

int  _M[1000];
int  *p;
int  *b;
char *ans;

int twiddle(int *x, int *y, int *z, int *p) {
	int i, j, k;
	j = 1;
	while (p[j] <= 0) {
		j++;
	}

	if (p[j - 1] == 0) {
		for (i = j - 1; i != 1; i--) {
			p[i] = -1;
		}

		p[j] = 0;
		*x = *z = 0;
		p[1] = 1;
		*y = j-1;
	} else {
		if (j > 1) {
			p[j-1] = 0;
		}

		do {
			j++;
		} while(p[j] > 0);

		k = j-1;
		i = j;
		while (p[i] == 0) {
			p[i++] = -1;
		}

		if(p[i] == -1) {
			p[i] = p[k];
			*z = p[k]-1;
			*x = i-1;
			*y = k-1;
			p[k] = -1;
		} else {
			if (i == p[0]) {
				return 1;
			} else {
				p[j] = p[i];
				*z = p[i]-1;
				p[i] = 0;
				*x = j-1;
				*y = i-1;
			}
		}
	}

	return 0;
}

void inittwiddle(int m, int n, int *p) {
	int i;
	p[0] = n + 1;
	for (i = 1; i != n-m+1; i++) {
		p[i] = 0;
	}

	while (i != n+1) {
		p[i] = i+m-n;
		i++;
	}

	p[n+1] = -2;
	if (m == 0) {
		p[1] = 1;
	}
}

void decimalToBinary_beforeRotate(unsigned int number, char *ret, int ret_index) {
	unsigned int remainder;

	if (number <= 1) {
		assert(number >= 0);
		assert(number <= 1);
		ret[ret_index] = number + 48;
		//printf("%d", number);
		return;
	}

	remainder = number % 2;
	decimalToBinary_beforeRotate(number >> 1, ret, ret_index + 1);

	assert(remainder >= 0);
	assert(remainder <= 1);
	ret[ret_index] = remainder + 48;
	//printf("%d", remainder);
}

char         bin[21];
char         sumBin0[21];
char         sumBin1[21];
unsigned int sum[2];

void rotate(char *data, int dataLen) {
	int tmp2 = dataLen / 2;
	for (int i = 0; i < tmp2; ++i) {
		// swap data[i] with data[len - 1 - i]
		char tmp = data[i];
		data[i] = data[dataLen - 1 - i];
		data[dataLen - 1 - i] = tmp;
	}
}

void zeroPadIt(char *data, int desiredLen) {
	int len = strlen(data);

	if (len < desiredLen) {
		int j = 0;
		int k = len - 1;
		for (int i = desiredLen - 1; j < len ; --i, ++j) {
			data[i] = data[k--];
		}

		int diff = desiredLen - len;
		for (int i = 0; i < diff; ++i) {
			data[i] = '0';
		}
	}
}

void doForgetfulAddition(char *acc) {
	for (int i = 0; i <= 20; ++i) {
		if (acc[i] == '1' && bin[i] == '1') {
			acc[i] = '0';
		} else if (acc[i] == '0' && bin[i] == '1') {
			acc[i] = '1';
		} else if (acc[i] == '1' && bin[i] == '0') {
			acc[i] = '1';
		} else if (acc[i] == '0' && bin[i] == '0') {
			acc[i] = '0';
		}
	}
}

int calculateNumberOfFeasible() {
	int bIsFeasible = 0; // 0 = not feasible, 1 = feasible.

	for (int i = 0; i < 20; ++i) {
		sumBin0[i] = '0';
		sumBin1[i] = '0';
	}
	sumBin0[20] = '\0';
	sumBin1[20] = '\0';

	sum[0] = 0;
	sum[1] = 0;

	for (int i = 0; i < N; ++i) {
		unsigned int val = c_i1[i];
		char        _ans = ans[i]; // '0' or '1';

		sum[_ans-48] += val;

		for (int i = 0; i < 21; ++i) {
			bin[i] = '\0';
		}
		decimalToBinary_beforeRotate(val, bin, 0);

		int binLen = strlen(bin);
		assert(binLen >= 1);
		assert(binLen <= 20);

		rotate(bin, binLen);

		//zeroPadIt(bin, 4);
		//printf("<%u = %s>\n", val, bin);

		zeroPadIt(bin, 20);

		if (_ans == '0') {
			doForgetfulAddition(sumBin0);
		}

		if (_ans == '1') {
			doForgetfulAddition(sumBin1);
		}
	}

	bool bSame = true;
	for (int i = 0; i <= 20; ++i) {
		if (sumBin0[i] != sumBin1[i]) {
			bSame = false;
			break;
		}
	}
	
	//printf("%d %s\n", sum[0], bin0);
	//system("pause");

	
	//decimalToBinary_beforeRotate(sum[1], bin1, 0);
	//rotate(bin0);
	//printf("%d %s\n", sum[1], bin1);
	//system("pause");

	//printf("before:<%s %s>\n", bin0, bin1);
	//zeroPadIt(bin0, bin1);
	//printf("after: <%s %s>\n\n", bin0, bin1);

	//printf("sum0=%u\n", sum[0]);
	//printf("sum1=%u\n", sum[1]);
	//system("pause");

	unsigned theValueOfLargerPile = sum[0] > sum[1] ? sum[0] : sum[1];

	return bSame ? theValueOfLargerPile : 0;
}

int compute() {
	int numOfFeasible = 0;
	int theValueOfLargerPile;
	int theValueOfLargerPile_max = INT_MIN;

	for (int M_ = 1; M_ <= _M[N]; ++M_) {
		int M = M_; // choose M
		int i, x, y, z;

		inittwiddle(M, N, p);
		
		int ans_i = 0;

		for (i = 0; i != N - M; ++i) {
			b[i] = 0;
			ans[ans_i++] = '0';
		}

		while (i != N) {
			b[i++] = 1;
			ans[ans_i++] = '1';
		}

		theValueOfLargerPile = calculateNumberOfFeasible();
		if (theValueOfLargerPile > theValueOfLargerPile_max) {
			theValueOfLargerPile_max = theValueOfLargerPile;
		}
		numOfFeasible += theValueOfLargerPile;
				
		while (!twiddle(&x, &y, &z, p)) {
			ans_i = 0;

			b[x] = 1;
			b[y] = 0;
			for (i = 0; i != N; ++i) {
				if (b[i]) {
					ans[ans_i++] = '1';
				} else {
					ans[ans_i++] = '0';
				}
			}

			theValueOfLargerPile = calculateNumberOfFeasible();
			if (theValueOfLargerPile > theValueOfLargerPile_max) {
				theValueOfLargerPile_max = theValueOfLargerPile;
			}
			numOfFeasible += theValueOfLargerPile;
		}
	}

	if (numOfFeasible == 0) {
		return 0;
	} else {
		return theValueOfLargerPile_max;
	}
}

int main() {
	_M[0] = -1;
	_M[1] = -1;
	_M[2] = 1;
	int _M_tmp = 1;
	for (int _M_i = 3; _M_i <= 1000; ++_M_i) {
		if (_M_i % 2 == 0) {
			++_M_tmp;
		}

		_M[_M_i] = _M_tmp;
	}

	//FILE *fp = fopen("C:\\gcj\\Candy_Splitting\\test", "r");
	FILE *fp = fopen("C:\\gcj\\Candy_Splitting\\small", "r");
	//FILE *fp = fopen("C:\\gcj\\Candy_Splitting\\big", "r");

	FILE *fp2 = fopen("C:\\gcj\\Candy_Splitting\\output", "w");

	int T;
	fscanf(fp, "%d", &T);

	assert(T >= 1);
	assert(T <= 100);

	c_i1 = (unsigned int *) malloc(1000 * sizeof(unsigned int));

	p = (int *) malloc((1000 + 2) * sizeof(int));
	b = (int *) malloc((1000) * sizeof(int));
	ans = (char *) malloc((1000 + 1) * sizeof(char));

	assert(c_i1 != NULL);
	
	for (int i = 0; i < T; ++i) {
		fscanf(fp, "%d", &N);

		assert(N >= 2);
		assert(N <= 1000);

		for (int j = 0; j < N; ++j) {
			fscanf(fp, "%d", &c_i1[j]);

			assert(c_i1[j] >= 1);
			assert(c_i1[j] <= 1000000);
		}

		int ret = compute();
		fprintf(fp2, "Case #%d: ", i + 1);
		if (ret == 0) {
			fprintf(fp2, "NO");
		} else {
			fprintf(fp2, "%d", ret);
		}

		fprintf(fp2, "\n");
	}

	free(c_i1);
	free(p);
	free(b);
	free(ans);
	fclose(fp);
	fclose(fp2);
	return 0;
}
