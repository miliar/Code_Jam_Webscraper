#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

vector<string> res;

vector<double> wp;
vector<double> oowp;
vector<double> owp;
vector<double> played;
int main() {
	int T, n;
	scanf("%d", &T);
	char str[110];

	for(int q=0;q<T;q++) {
		scanf("%d", &n);
		res.clear();
		wp.clear();
		oowp.clear();
		owp.clear();
		played.clear();
		for(int i=0;i<n;i++) {
			scanf("%s", str);
			res.push_back(str);
		}
		
		for(int i=0;i<n;i++) {
			int play = 0;
			int win = 0;
			for(int j=0;j<n;j++) {
				
				if(res[i][j] == '1')
					win++;
				if(res[i][j] != '.')
					play++;
			}
			played.push_back(play);
			wp.push_back((double)win / play);
		}
		
		for(int i=0;i<n;i++) {
			double op = 0.0;
			for(int j=0;j<n;j++) {
				if(res[i][j] == '1') {
					if(played[j] != 1) {
						op += (double)(wp[j] * played[j]) / (played[j] - 1.0);
					} else {
						op += 1;
					}
				} else if(res[i][j] == '0'){
					if(played[j] != 1) {
						op += (double)(wp[j] * played[j] - 1.0) / (played[j] -1.0);
					} else {
						op += 1;
					}
				} 
			}
			owp.push_back(op / played[i]);
		}
		for(int i=0;i<n;i++) {
			double oop = 0.0;
			for(int j=0;j<n;j++) {
				if(res[i][j] != '.') {
					oop += owp[j];
				}
			}
			oowp.push_back(oop / played[i]);
		}
		printf("Case #%d:\n", q+1);
		
		for(int i=0;i<n;i++) {
			double rpi = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			printf("%lf\n", rpi);
		}

	}
	return 0;
}
