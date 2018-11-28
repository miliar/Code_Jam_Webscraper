#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int case_nr, C, N, M, x1, x2, x3, y1, y2, y3, A;

	cin >> C;

	for (case_nr=1; case_nr<=C; case_nr++) {
		cin >> N >> M >> A;

		cout << "Case #" << case_nr << ": ";

		if (A>N*M)
			cout << "IMPOSSIBLE" << endl;
		else {
			for (x1=0; x1<=N; x1++)
				for (x2=0; x2<=N; x2++)
					for (x3=0; x3<=N; x3++)
						for (y1=0; y1<=M; y1++)
							for (y2=y1; y2<=M; y2++)
								for (y3=y2; y3<=M; y3++) {
									int S=abs(x1*y2+x2*y3+x3*y1-x3*y2-x1*y3-x2*y1);

									if (S==A)
										goto answer;
								}

			cout << "IMPOSSIBLE" << endl;
			continue;
answer:
			cout << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
		}
	}
}
