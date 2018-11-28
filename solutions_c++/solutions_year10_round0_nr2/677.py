
#include <iostream>
#include <vector>

using namespace std;

class positivebigint {

public:

	vector<int> _n;
	
	positivebigint& operator=(const positivebigint& i) {
		_n.clear();
//		_n.reserve(i._n.size());
		_n.resize(i._n.size());
		copy(i._n.begin(), i._n.end(), _n.begin());
		return (*this);
	}

	bool operator==(const positivebigint& i) {

		if(_n.size() != i._n.size()) return false;
		for(int j = _n.size()-1; j >= 0; j--) {
			if(_n[j] != i._n[j]) return false;
		}
		return true;
	}

	bool operator==(const int& i) {

		positivebigint pi;
		int ti = i;
		if(ti == 0) pi._n.push_back(0);
		while(ti) {
			pi._n.push_back(ti % 10);
			ti /= 10;
		}

		return (*this == pi);
	}

	positivebigint operator-(positivebigint& i) {
		positivebigint t, t1, td;
		if(*this >= i) {
			t = i;
			t1 = *this;
			int sizediff = _n.size() - i._n.size();
			for(int j = 0; j < sizediff; j++) {
				t._n.push_back(0);
			}

			for(int j = 0; j < t1._n.size()-1; j++) {
				if(t1._n[j] >= t._n[j])
					td._n.push_back(t1._n[j] - t._n[j]);
				else {
					t1._n[j+1]--;
					td._n.push_back(t1._n[j] + 10 - t._n[j]);
				}
			}
			td._n.push_back(t1._n[_n.size()-1]-t._n[_n.size()-1]);
			int j;
			for(j = td._n.size()-1; j > 0; j--) {
				if(td._n[j]) break;
				td._n.pop_back();
			}
		}
		return td;
	}

	int operator>(const positivebigint& i) {
		//if(*this == i) return 0;
		//if(_n.size() > i._n.size()) return 1;
		//if(_n.size() < i._n.size()) return -1;
		//if(_n.size() == i._n.size()) {
		//	for(int j = _n.size()-1; j >= 0; j++) {
		//		if(_n[j] > i._n[j]) return 1;
		//		if(_n[j] < i._n[j]) return -1;
		//	}
		//}
		if(*this == i) return 0;
		if(_n.size() > i._n.size()) return 1;
		if(_n.size() < i._n.size()) return 0;
		if(_n.size() == i._n.size()) {
			for(int j = _n.size()-1; j >= 0; j--) {
				if(_n[j] > i._n[j]) return 1;
				if(_n[j] < i._n[j]) return 0;
			}
		}
	}

	bool operator>=(positivebigint& i) {
		if(*this > i) return true;
		else if(*this == i) return true;
		return false;
	}

	positivebigint operator%(positivebigint& i) {

		positivebigint p1;
		for(int j = _n.size() - 1; j >= 0; j--) {
			p1._n.insert(p1._n.begin(), _n[j]);
			if(p1 >= i) {
				while(p1 >= i) {
					p1 = p1 - i;
				}
			}
		}
		return p1;
	}

	positivebigint operator*(int i) {

		positivebigint t1;
		int tm, tc = 0;
		for(int j = 0; j < _n.size(); j++) {
			tm = this->_n[j] * i + tc;
			t1._n.push_back(tm % 10);
			tc = tm / 10;
		}
		while(tc) {
			t1._n.push_back(tc % 10);
			tc /= 10;
		}
		return t1;
	}

	int operator << (char* tc) {
		_n.clear();
		int tlen = strlen(tc);
		for(int i = 0; i < tlen; i++) {
			_n.push_back(tc[tlen - 1 - i] - '0');
		}
		return 0;
	}

	int operator >> (char* tc) {

		for(int i = _n.size()-1; i >= 0; i--) {
			tc[i] = _n[_n.size()-1-i] + '0';
		}
		tc[_n.size()] = '\0';
		return 0;
	}

};

positivebigint gcd(positivebigint a, positivebigint b) {

	if(a == b) return a;
	if(a > b) {
		positivebigint t;
		t = b;
		b = a;
		a = t;
	}
	if(a == 0) return b;
	if(a == 1) {
		positivebigint p1;
		p1._n.push_back(1);
		return p1;
	}
	return gcd(a, b-a);
}

int main() {

	FILE *ipf, *opf;
	ipf = freopen("B-small-attempt2.in", "r", stdin);
	opf = freopen("B-small-attempt2.out", "w", stdout);

	int T;
	cin >> T;
	for(int i = 1; i <= T ; i++) {
		int N;
		cin >> N;
		char tc[64];
		positivebigint* p_ints = new positivebigint[N];
		for(int j = 0; j < N; j++) {
			cin >> tc;
			p_ints[j] << tc;
		}

		positivebigint cgcd;
		if(p_ints[1] > p_ints[0])
			cgcd = p_ints[1] - p_ints[0];
		else
			cgcd = p_ints[0] - p_ints[1];
		positivebigint p1;
		for(int j = 1; j < N-1; j++) {
			if(p_ints[j+1] > p_ints[j])
				p1 = p_ints[j+1] - p_ints[j];
			else
				p1 = p_ints[j] - p_ints[j+1];
			cgcd = gcd(cgcd, p1);
		}

		positivebigint tmin = p_ints[0];
		for(int j = 1; j < N; j++) {
			if(tmin > p_ints[j]) tmin = p_ints[j];
		}

		positivebigint fin;
		positivebigint modgcd = tmin % cgcd;
		fin._n.clear();
		if(modgcd == 0)
			fin._n.push_back(0);
		else
			fin = cgcd - modgcd;
		char* tc2 = new char[64];
		fin >> tc2;

		cout << "Case #" << i << ": " << tc2 << endl;
	}

	fclose(ipf);
	fclose(opf);
	return 0;
}
