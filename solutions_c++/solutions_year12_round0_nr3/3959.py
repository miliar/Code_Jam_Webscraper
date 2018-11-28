#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;


struct BCD {
	int val;
	int len;

	BCD(int v)
	{
		val=0;
		len=0;
		for (int i=0;i<8 && v>0;++i){
			val |= (v%10) << (i*4);
			v /= 10;
			len++;
		}
	}

	BCD rotate_left(int i)
	{
		BCD r = *this;
		r.val = (val << (i * 4)) | (val >> ((len - i) * 4));
		for (int j=len;j<8;++j) {
			r.val &= ~(0xF << j*4);
		}
		return r;
	}
};


int main() {
	int T; scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d of %d...\n", Ti, T);

		set< pair<int, int> > pairs;
		int A, B, BB;
		scanf("%d %d", &A, &B);
		BB = BCD(B).val;

		for (int n = A; n <= B; ++n) {
			BCD bn(n);
			for (int i = 1;i<bn.len;++i) {
				BCD bm = bn.rotate_left(i);
				if (bn.val < bm.val && bm.val <= BB) {
					if (pairs.insert(make_pair(bn.val, bm.val)).second) {
						//fprintf(stderr, "%X, %X\n", bn.val, bm.val);
					}
				}
			}
		}
		printf("Case #%d: %d\n", Ti, (int)pairs.size());
	}
	return 0;
}
