class BigNum {
private:
	void _add(int *result, int *x, int *y, int mul) {
		int a[MAXB], b[MAXB];
		copy(a, x);
		copy(b, y);

		int i, tmp = 0;
		for(i = 1; i <= a[0] || i <= b[0] || tmp > 0; i++) {
			if(i <= a[0])tmp += a[i];
			if(i <= b[0])tmp += b[i] * mul;
			if(tmp < 0) {
				a[i + 1]--;
				tmp += MOD;
			}
			result[i] = tmp % MOD;
			tmp /= MOD;
		}
		result[0] = i - 1;
		trim(result);
	}

public:
	// ----- Compare Method
	int compare(int *a, int *b) {
		// (a < b) return -1
		// (a = b) return 0
		// (a > b) return 1
		if(a[0] < b[0])return -1;
		if(a[0] > b[0])return 1;
		for(int i = a[0]; i >= 1; i--) {
			if(a[i] < b[i])return -1;
			if(a[i] > b[i])return 1;
		}
		return 0;
	}

	int compare_num(int *a, int num) {
		int tmp[MAXB];
		set(tmp, num);
		return compare(a, tmp);
	}

	bool less(int *a, int *b) {
		return compare(a, b) < 0;
	}

	bool less_num(int *a, int num) {
		return compare_num(a, num) < 0;
	}

	bool less_equal(int *a, int *b) {
		return compare(a, b) <= 0;
	}

	bool less_equal_num(int *a, int num) {
		return compare_num(a, num) <= 0;
	}

	bool equal(int *a, int *b) {
		return compare(a, b) == 0;
	}

	bool equal_num(int *a, int num) {
		return compare_num(a, num) == 0;
	}

	bool more(int *a, int *b) {
		return compare(a, b) > 0;
	}

	bool more_num(int *a, int num) {
		return compare_num(a, num) > 0;
	}

	bool more_equal(int *a, int *b) {
		return compare(a, b) >= 0;
	}

	bool more_equal_num(int *a, int num) {
		return compare_num(a, num) >= 0;
	}


	// ----- Common Method
	void set_string(int *result, char *str) {
		set(result, 0);
		for(int i = 0; str[i] != 0; i++) {
			mul_num(result, result, 10);
			add_num(result, result, str[i] - '0');
		}
	}

	void set(int *a, int num) {
		int i, tmp = num;
		for(i = 1; tmp > 0; i++) {
			a[i] = tmp % MOD;
			tmp /= MOD;
		}
		a[0] = i - 1;
	}

	void copy(int *dst, int *src) {
		for(int i = 0; i <= src[0]; i++)
			dst[i] = src[i];
	}

	void trim(int *result) {
		while(result[result[0]] == 0 && result[0] > 0)
			result[0]--;
	}

	void scan(int *result) {
		char str[MAXB * DIGIT];
		scanf("%s", str);
		set_string(result, str);
	}

	void print(int *a) {
		char pattern[MAXB];
		strcpy(pattern, "%00d");
		pattern[2] = DIGIT + '0';
		printf("%d", a[a[0]]);
		for(int i = a[0] - 1; i >= 1; i--)
			printf(pattern, a[i]);
	}


	// ----- Math Method
	void add_num(int *result, int *a, int num) {
		int i, tmp = num;
		for(i = 1; i <= a[0] || tmp > 0; i++) {
			if(i <= a[0])tmp += a[i];
			if(tmp < 0) {
				a[i + 1]--;
				tmp += MOD;
			}
			result[i] = tmp % MOD;
			tmp /= MOD;
		}
		result[0] = i - 1;
		trim(result);
	}

	void add(int *result, int *a, int *b) {
		_add(result, a, b, 1);
	}

	void sub_num(int *result, int *a, int num) {
		add_num(result, a, -num);
	}

	void sub(int *result, int *a, int *b) {
		_add(result, a, b, -1);
	}

	void mul_num(int *result, int *a, int num) {
		int i, tmp = 0;
		for(i = 1; i <= a[0] || tmp > 0; i++) {
			if(i <= a[0])tmp += a[i] * num;
			result[i] = tmp % MOD;
			tmp /= MOD;
		}
		result[0] = i - 1;
	}

	void mul(int *result, int *a, int *b) {
		int sum[MAXB], tmp[MAXB];
		set(sum, 0);
		for(int i = 1; i <= b[0]; i++) {
			mul_num(tmp, a, b[i]);
			for(int j = 1; j < i; j++)
				mul_num(tmp, tmp, MOD);
			add(sum, sum, tmp);
		}
		copy(result, sum);
	}

	void div_num(int *result, int *a, int num) {
		int i, out[MAXB], tmp[MAXB];
		copy(out, a);
		set(tmp, 0);
		for(i = a[0]; i >= 1; i--) {
			mul_num(tmp, tmp, MOD);
			add_num(tmp, tmp, a[i]);
			out[i] = 0;
			while(!equal_num(tmp, 0) && more_equal_num(tmp, num)) {
				sub_num(tmp, tmp, num);
				out[i]++;
			}
		}
		trim(out);
		copy(result, out);
	}

	void div(int *result, int *a, int *b) {
		int i, out[MAXB], tmp[MAXB];
		copy(out, a);
		set(tmp, 0);
		for(i = a[0]; i >= 1; i--) {
			mul_num(tmp, tmp, MOD);
			add_num(tmp, tmp, a[i]);
			out[i] = 0;
			while(!equal_num(tmp, 0) && more_equal(tmp, b)) {
				sub(tmp, tmp, b);
				out[i]++;
			}
		}
		trim(out);
		copy(result, out);
	}

	void mod(int *result, int *a, int *b) {
		int tmp[MAXB];
		div(tmp, a, b);
		mul(tmp, tmp, b);
		sub(result, a, tmp);
	}

	void gcd(int *result, int *a, int *b) {
		int x[MAXB], y[MAXB], c[MAXB];
		copy(x, a);
		copy(y, b);
		mod(c, x, y);
		while(!equal_num(c, 0)) {
			copy(x, y);
			copy(y, c);
			mod(c, x, y);
		}
		copy(result, y);
	}
};
