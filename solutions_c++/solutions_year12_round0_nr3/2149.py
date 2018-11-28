#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;

int a, b;
int p10[8];
int process(int z) {
	int dig = (int)(log(z) / log(10))+1;
	int left = z / 10, right = z % p10[dig-1], rl = left;
	int tr = 0;
	vector<int> gened;
	for (int i=1;i<dig;++i) {
		//printf("%d %d\n", right, rl);
		int gen = (right * 10 + left / p10[dig-2]);
		if (right > rl && gen <= b) {
			bool f = false;
			for (vector<int>::iterator vi=gened.begin();vi!=gened.end();++vi){
				if (*vi == gen) { f = true; break; }
			}
			if (!f) {++tr; gened.push_back(gen); }
		}
		right = gen % p10[dig-1];
		left = left % p10[dig-2];
		left = left * 10;
	}
	return tr;
}
bool recycle(int a, int b) {
	int diga = (int)(log(a) / log(10))+1;
	int digb = (int)(log(b) / log(10))+1;
	if (diga != digb) return false;
	vector<int> va, vb;
	for (int i=0;i<diga;++i) {
		va.push_back( a % 10 );
		vb.push_back( b % 10 );
		a /= 10; b/=10;
	}
	for (int i=1;i<diga;++i) {
		bool wrong = false;
		for (int j=0;j<diga;++j) {
			if (va[j] != vb[(j+i)%diga]) {
				wrong = true; break;
			}
		}
		if (!wrong) return true;
	}
	return false;
}
int bf() {
	int tr = 0;
	for (int i=a;i<=b;++i) {
		int mi = 0;
		for (int j=i+1;j<=b;++j) {
			if (recycle(i, j)) {
				mi++;
				++tr;
			}
		}
		if (mi != process(i)) {
			printf("invalid for %d %d %d", i, mi, process(i));
		}
	}
	return tr;
}

int main() {
	p10[0] = 1;
	for (int i=1;i<8;++i) p10[i] = p10[i-1] * 10;

	int T;
	scanf(" %d", &T);
	for (int i=1;i<=T;++i) {
		scanf( "%d%d", &a, &b);
		long long tr = 0;
		for (int j=a;j<=b;++j) {
			tr += process(j);
		}
		//printf("Case %d: %d\n", i, bf());
		printf("Case #%d: %lld\n", i, tr);
	}
	return 0;
}
