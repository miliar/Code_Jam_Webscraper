#include <stdio.h>
#include <algorithm>
#include <set>

using namespace std;

int N, n;
int T;
int NA, NB;
int i;

struct TDep {
	int dep;
	int arr;
	int st;
} d[1000];

multiset <int> A;
multiset <int> B;

multiset <int>::iterator iter;

int len;
int resA, resB;

int h1, m1, h2, m2;
int t1, t2;

bool sort_function(TDep a, TDep b)
{
	return a.dep < b.dep;
}

int main() {

	//FILE *in = fopen("B-small.in", "rt");
	//FILE *out = fopen("B-small.out", "wt");

	FILE *in = fopen("B-large.in", "rt");
	FILE *out = fopen("B-large.out", "wt");

	fscanf(in, "%d", &N);

	for (n = 1; n <= N; n++) {

		A.clear(); B.clear();

		fscanf(in, "%d", &T);
		fscanf(in, "%d %d", &NA, &NB);

		len = 0;

		for (i = 0; i < NA; i++) {
			fscanf(in, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			t1 = h1 * 60 + m1;
			t2 = h2 * 60 + m2;
			d[len].dep = t1;
			d[len].arr = t2;
			d[len].st = 1;
			len++;
		}

		for (i = 0; i < NB; i++) {
			fscanf(in, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			t1 = h1 * 60 + m1;
			t2 = h2 * 60 + m2;
			d[len].dep = t1;
			d[len].arr = t2;
			d[len].st = 2;
			len++;
		}

		sort(d, d+len, sort_function);

		resA = 0; resB = 0;

		for (i = 0; i < len; i++) {
			if (d[i].st == 1) {
				iter = A.begin();
				while (iter != A.end()) {
					if (*iter <= d[i].dep) break;
					iter++;
				}
				if (iter == A.end())
					resA++;
				else
					A.erase(iter);
				B.insert(d[i].arr + T);				
			} else {
				iter = B.begin();
				while (iter != B.end()) {
					if (*iter <= d[i].dep) break;
					iter++;
				}
				if (iter == B.end())
					resB++;
				else 
					B.erase(iter);
				A.insert(d[i].arr + T);				
			}
		}

		fprintf(out, "Case #%d: %d %d\n", n, resA, resB);
	}
	
	fclose(in);
	fclose(out);

	return 0;
}