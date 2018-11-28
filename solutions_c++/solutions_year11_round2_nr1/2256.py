#include <fstream>
#include <vector>
#include <math.h>

using namespace std;




int main() {

	int T;
	int N;
	int A[100][100];
	float wp[100];
	float owp[100];
	float oowp[100];
	int sum[100];
	int count[100];

	char c;
	
	fstream f, g;

	f.open("rpi.in", fstream::in);
	g.open("rpi.out", fstream::out);
	
	f >> T;
	for (int t = 1; t <= T; t++) {
		f >> N;
		memset(A, 0, sizeof( A));

		memset(wp, 0, sizeof(wp));
		memset(owp, 0, sizeof(owp));
		memset(oowp, 0, sizeof(oowp));
		memset(sum, 0, sizeof( sum));
		memset(count, 0, sizeof( count));

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				f >> c;
				
				if (c == '.') 
					A[i][j] = -1;
				else if (c == '0') 
					A[i][j] = 0;
				else if (c == '1') 
					A[i][j] = 1;
				
			}
		}

		for (int i = 0; i < N; i++) {
			count[i] = 0;
			sum[i] = 0;
			for (int j = 0; j < N; j++) {
				if (A[i][j] != -1) {
					count[i]++;
					sum[i] += A[i][j];
				}
			}
			wp[i] = (float ) sum[i] / (float ) count[i];
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (A[i][j] != -1) {
					owp[i] += (float ) (sum[j] - A[j][i]) / (float ) (count[j] - 1);
				}
			}
			owp[i] /= (float ) count[i];
		}

		for (int i = 0; i < N; i++) {
			oowp[i] = 0;
			for (int j = 0; j < N; j++) {
				if (A[i][j] != -1) {
					oowp[i] += owp[j]; 
				}
			}
			oowp[i] /= (float ) count[i];
			
		}
		
		g << "Case #" << t << ":" << endl; 
		for (int i = 0; i < N; i++) {
			g << (float ) (wp[i] * 0.25 + 0.50 * owp[i] + 0.25 * oowp[i]) << endl;
		}
	}

	return 0;
}