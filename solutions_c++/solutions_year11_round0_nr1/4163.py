#include <stdio.h>
#include <vector>
#include <stdlib.h>
using namespace std;

class inst {
public:
	bool blue;
	int button;
};

vector<inst> seq;

int main() {
	int T, n;
	char str[3];
	scanf("%d", &T);

	for(int q=0;q<T;q++) {

		scanf("%d", &n);
		int t;
		inst tt;
		seq.clear();
		for(int i=0;i<n;i++) {
			scanf("%s %d", str, &t);
			tt.button = t;
			tt.blue = (str[0] == 'B');
			seq.push_back(tt);
		}
		int op = 1, bp = 1;
		int ot = 0, bt = 0;
		int sum = 0;
		for(int i=0;i<seq.size();i++) {
			if(seq[i].blue) {
				int diff = abs(seq[i].button - bp);
				if(ot < diff) {
					bt += (diff - ot);
					sum += (diff - ot);
				}
				sum += 1;
				bt += 1;
				bp = seq[i].button;
				ot = 0;
			} else {
				int diff = abs(seq[i].button - op);
				if(bt < diff) {
					ot += (diff - bt);
					sum += (diff - bt);
				}
				sum += 1;
				ot += 1;
				op = seq[i].button;
				bt = 0;
			}
		}
		printf("Case #%d: %d\n", q+1, sum);
	}
}
