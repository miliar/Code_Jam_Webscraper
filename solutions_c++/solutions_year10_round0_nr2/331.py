#include <iostream>
#include <algorithm>
#include <cassert>

using namespace std;

struct big {
	long long val[20];

	big(long long v = 0) {
		fill(val, val + 20, 0);
		val[0] = v;
		carry();
	}

	void set(int pos, int v) {
		assert(pos < 70);
		assert(v < 10);
		int mult[5] = {1,10,100,1000,10000};
		val[pos / 5] += v * mult[pos % 5];
	}

	big(string s) {
		fill(val, val + 20, 0);
		for (int i = 0; i < s.size(); i++)
			set(s.size() - i - 1, s[i] - '0');
	}

	void swap(big& o) {
		for (int i = 0; i < 20; i++) ::swap(val[i], o.val[i]);
	}

	big& carry() {
		for (int i = 0; i < 19; i++) {
			val[i + 1] += val[i] / 100000;
			val[i] %= 100000;
		}
		return *this;
	}

	big& operator+=(const big& o) {
		for (int i = 0; i < 20; i++)
			val[i] += o.val[i];
		return carry();
	}

	big& operator-=(const big& b) {
		assert(*this >= b);
		for (int i = 0; i < 20; i++) {
			val[i] -= b.val[i];
			if (val[i] < 0) { val[i] += 100000; val[i + 1]--; }
		}
		return carry();
	}

	big& operator*=(const big& o) {
		big a(0);
		swap(a);
		for (int i = 0; i < 20; i++)
			for (int j = 0; j < 20; j++) {
				if (i + j >= 20) continue;
				val[i + j] += a.val[i] * o.val[j];
			}
		return carry();
	}
	big& operator*=(long long a) {
		for (int i = 0; i < 20; i++)
			val[i] *= a;
		return carry();
	}

friend ostream& operator<<(ostream& out, const big& a);
	big& operator%=(const big& o) {
		if (*this < o) return *this;
		big c = o, n = c;
		n *= 2;
		while (n < *this) { c = n; n *= 2; }
		*this -= c;
		return *this %= o;
	}

	operator bool() const { for (int i = 0; i < 20; i++) if (val[i]) return 1; return 0; }

	bool operator<(const big& b) const {
		for (int i = 19; i >= 0; i--) {
			if (b.val[i] < val[i]) return false;
			if (val[i] < b.val[i]) return true;
		}
		return false;
	}
	bool operator>(const big& b) const {
		return b < *this;
	}
	bool operator<=(const big& b) const {
		return !(b < *this);
	}
	bool operator>=(const big& b) const {
		return b <= *this;
	}
	bool operator==(const big& b) const {
		return !(*this < b) && !(b < *this);
	}
	bool operator!=(const big& b) const {
		return !(*this == b);
	}


};

big operator+(const big& a, const big& b) {
	big ret = a;
	return ret += b;
}
big operator-(const big& a, const big& b) {
	big ret = a;
	return ret -= b;
}
big operator%(const big& a, const big& b) {
	big ret = a;
	return ret %= b;
}

ostream& operator<<(ostream& out, const big& a) {
	int i = 19;
	for (; i > 0; i--) if (a.val[i]) break;
	for (int j = i; j >= 0; j--) {
		if (j != i) {
			int k = 10000;
			while (k > 1 && a.val[j] < k) { k /= 10; out << 0; }
		}
		out << a.val[j];
	}
	return out;
}


big gcd(const big& a, const big& b) {
	return b ? gcd(b, a % b) : a;
}
	

int main() {
	int ncases;
	cin >> ncases;
	for (int caseno = 1; caseno <= ncases; caseno++) {
		big nums[1002];
		int n;
		cin >> n;
		for (int i = 0; i < n; i++) {
			string num;
			cin >> num;
			nums[i] = big(num);
			if (nums[i] < nums[0]) nums[0].swap(nums[i]);
		}
		for (int j = 1; j < n; j++)
			nums[j] -= nums[0];
		big v = nums[1];
		for (int j = 2; j < n; j++)
			v = gcd(v, nums[j]);
		nums[0] %= v;
		if (!nums[0]) cout << "Case #" << caseno << ": 0" << endl;
		else cout << "Case #" << caseno << ": " << (v - nums[0]) << endl;

	}
	return 0;
}
