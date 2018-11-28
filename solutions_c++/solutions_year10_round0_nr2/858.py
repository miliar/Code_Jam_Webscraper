#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

class bigInt {

	friend ostream & operator << (ostream &, const bigInt &);
	friend istream & operator >> (istream &, bigInt &);

public:
	bigInt() {
		num.clear();
	}
	bigInt(const char *str) {
		int n = strlen(str);
		num.resize(n);
		for(int i = n-1; i>=0; --i) {
			num[n-i-1] = str[i] - '0';
		}
	}
	bigInt(int a) {
		while(a) {
			num.push_back(a%10);
			a /= 10;
		}
	}
	bigInt &operator = (const char *str) {
		*this = bigInt(str);
		return *this;
	}
	bigInt operator + (const bigInt &r) const {
		int i=0, left=0, cur;
		bigInt res;
		int n = max(num.size(), r.num.size());
		for(i=0; i<n; ++i) {
			cur = (i<num.size() ? num[i] : 0) + (i<r.num.size() ? r.num[i] : 0) + left;
			res.num.push_back(cur%10);
			left = cur/10;
		}
		if (left) {
			res.num.push_back(left);
		}
		return res;
	}

	bigInt operator - (const bigInt &r) const {
		int i=0, left=0, cur;
		bigInt res;
		int n = num.size();
		for(i=0; i<n; ++i) {
			cur = num[i] - (i<r.num.size() ? r.num[i] : 0) - left;
			left = 0;
			while(cur<0) {
				cur+=10;
				left++;
			}
			res.num.push_back(cur);
		}
		while(res.num[res.num.size()-1] == 0)
			res.num.pop_back();
		return res;
	}


	bigInt operator * (const bigInt &r) const {
		bigInt res;
		if (r.num.size() == 0) return res;
		if (r.num.size() == 1) {
			int i=0, left=0, cur;
			int n = num.size();
			for(i=0; i<n; ++i) {
				cur = num[i] * r.num[0] + left;
				res.num.push_back(cur%10);
				left = cur/10;
			}
			if (left) {
				res.num.push_back(left);
			}
			return res;
		}
		vector<bigInt> a(r.num.size());
		for(int i=0; i<a.size(); ++i) {
			a[i] = (*this) * bigInt((int)r.num[i]);
		}
		int cur = 0, left = 0;
		for(int i=0; i < num.size() + r.num.size(); ++i) {
			cur = left;
			for(int j=0; j<=i && j<a.size(); ++j) {
				cur += (i-j < a[j].num.size() ? a[j].num[i-j] : 0);
			}
			res.num.push_back(cur%10);
			left = cur/10;
		}
		if (left) {
			res.num.push_back(left);
		}
		return res;
	}

	bigInt operator / (const bigInt &r) const {
		return bdiv(r).first;
	}
	bigInt operator % (const bigInt &r) const {
		return bdiv(r).second;
	}

	bool operator < (const bigInt &r) const {
		if (num.size() != r.num.size()) {
			if (num.size() < r.num.size()) return true;
			return false;
		}
		for(int i=num.size()-1; i>=0; --i) {
			if (num[i] != r.num[i]) {
				if (num[i] < r.num[i]) return true;
				return false;
			}
		}
		return false;
	}
	bool operator > (const bigInt &r) const {
		return r < (*this);
	}
	bool operator != (const bigInt &r) const {
		return (*this) < r || r < (*this);
	}
	bool operator == (const bigInt &r) const {
		return !(r != (*this));
	}
private:
	vector<char> num;
	pair<bigInt, bigInt> bdiv(const bigInt &r) const {
		if (r == bigInt(1)) {
			return make_pair(*this, 0);
		}
		if (r == bigInt(2)) {
			bigInt p;
			p.num.resize(num.size());
			int left = 0, cur;
			for (int i = num.size() - 1; i>=0; --i) {
				cur = num[i] + left*10;
				p.num[i] = cur/2;
				left = cur%2;
			}
			if (p.num[num.size()-1] == 0) {
				p.num.pop_back();
			}
			return make_pair(p, bigInt(left));
		}
		bigInt b, e = *this, m, cur;
		while(e-b > bigInt(1)) {
			m = b+e;
			m = m.bdiv(2).first;
			cur = r * m;
			if (cur == *this) {
				return make_pair(m, bigInt());
			}
			if (cur < *this) {
				b = m;
			}
			else {
				e = m;
			}
		}
		return make_pair(b, *this - b*r);
	}
};

ostream & operator << (ostream &out, const bigInt &r) {
	for(int i = r.num.size() - 1; i>=0; --i) {
		out<<((int)r.num[i]);
	}
	if (r.num.size() == 0) {
		out<<0;
	}
	return out;
}

istream & operator >> (istream &inp, bigInt &r) {
	char str[128];
	inp>>str;
	r = str;
	return inp;
}

//bigInt lcd(bigInt a, bigInt b) {
//	if (b == 0) return a;
//	if (a > b) return lcd(b, a%b);
//	return lcd(a, b%a);
//}

int lcd(int a, int b) {
	if (b == 0) return a;
	if (a > b) return lcd(b, a%b);
	return lcd(a, b%a);
}

int main() {
	int t, n;
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	cin>>t;
	/*bigInt a[1<<10], b;*/
	int a[1<<10], b;
	int i, j, k;
	for(i=1; i<=t; ++i) {
		cin>>n;
		//bigInt r;
		int r=0;
		for(j=0; j<n; ++j) {
			cin>>a[j];
		}
		sort(a, a+n);
		reverse(a, a+n);
		for(j=1; j<n; ++j) {
			r = lcd(a[0] - a[j], r);
		}
		cout<<"Case #"<<i<<": "<<(r - (a[0]%r) == r ? 0 : r - a[0]%r)<<endl;
	}
	return 0;
}