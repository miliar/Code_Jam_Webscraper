#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

int buf_len;
char buf[256];

struct bi {
	vector<int> d;
	
	void read() {
		scanf("%s", buf);
		buf_len = strlen(buf);
		for (int i = buf_len - 1; i >= 0; i--)
			d.push_back(buf[i] - '0');
		while (!d.empty() && d.back() == 0)
			d.pop_back();
	}
	
	void write() {
		if (d.size() == 0)
			printf("0");
		else {
			for (int i = (int)d.size() - 1; i >= 0; i--)
				printf("%d", d[i]);
		}
	}
	
	bool zero() {
		return d.empty();
	}
	
	bi& operator+=(const bi& b) {
		d.resize(max(d.size(), b.d.size()));
		for (int i = 0; i < (int)b.d.size(); i++)
			d[i] += b.d[i];
		for (int i = 0; i < (int)d.size(); i++) {
			if (d[i] >= 10) {
				if (i + 1 >= (int)d.size())
					d.push_back(0);
				d[i + 1] += d[i] / 10;
				d[i] %= 10;
			}
		}
		return *this;
	}
	
	bi& operator-=(const bi &b) {
		for (int i = 0; i < (int)b.d.size(); i++)
			d[i] -= b.d[i];
		for (int i = 0; i < (int)d.size(); i++) {
			while (d[i] < 0) {
				d[i] += 10;
				d[i + 1]--;
			}
		}
		while (!d.empty() && d.back() == 0)
			d.pop_back();
		return *this;
	}
	
	bool operator<(const bi &b) {
		if (d.size() < b.d.size())
			return true;
		if (d.size() > b.d.size())
			return false;
		for (int i = (int)d.size() - 1; i >= 0; i--) {
			if (d[i] < b.d[i])
				return true;
			else if (d[i] > b.d[i])
				return false;
		}
		return false;
	}
	
	bool por(const bi &b, int poz) {
		if (poz + b.d.size() < d.size())
			return true;
		if (poz + b.d.size() > d.size())
			return false;
		for (int i = poz + (int)b.d.size() - 1, j = (int)b.d.size() - 1; i >= 0, j >= 0; i--, j--) {
			if (d[i] < b.d[j])
				return false;
			else if (d[i] > b.d[j])
				return true;
		}
		return true;
	}
	
	bi& odj2(const bi &b, int poz) {
		for (int i = 0; i < (int)b.d.size(); i++)
			d[poz + i] -= b.d[i];
		for (int i = 0; i < (int)b.d.size(); i++) {
			while (d[poz + i] < 0) {
				d[poz + i] += 10;
				d[poz + i + 1]--;
			}
		}
		while (!d.empty() && d.back() == 0)
			d.pop_back();
		return *this;
	}
	
	bi& operator%=(const bi &b) {
		int poz = (int)d.size() - (int)b.d.size();
		while (poz >= 0) {
			while (this->por(b, poz)) {
				this->odj2(b, poz);
			}
			poz--;
		}
		return *this;
	}
};

int n, tests;
vector<bi> tab;

int main() {
	scanf("%d", &tests);
	for (int t = 0; t < tests; t++) {
		scanf("%d", &n);
		tab.resize(n);
		for (int i = 0; i < n; i++)
			tab[i].read();
		int ind = 0;
		for (int i = 0; i < n; i++)
			if (tab[i] < tab[ind])
				ind = i;
		for (int i = 0; i < n; i++)
			if (i != ind)
				tab[i] -= tab[ind];
		int ind2 = 0;
		for (int i = 0; i < n; i++)
			if (i != ind && !tab[i].zero()) {
				ind2 = i;
				break;
			}
		for (int i = ind2 + 1; i < n; i++)
			if (i != ind && !tab[i].zero()) {
				while (!tab[ind2].zero() && !tab[i].zero()) {
					if (!tab[i].zero()) tab[ind2] %= tab[i];
					if (!tab[ind2].zero()) tab[i] %= tab[ind2];
				}
				if (tab[ind2].zero())
					ind2 = i;
			}
		bi t1 = tab[ind2], t2 = tab[ind];
		t2 %= t1;
		if (!t2.zero())
			t1 -= t2;
		else 
			t1.d.clear();
		printf("Case #%d: ", t + 1);
		t1.write();
		printf("\n");
		tab.clear();
	}
	return 0;
}