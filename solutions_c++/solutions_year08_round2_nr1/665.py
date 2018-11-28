#include <climits>
#include <iostream>
#include <set>
#include <algorithm>
#include <queue>
#include <vector>
#include <bitset>
#include <map>

using namespace std;

long long 
solve()
{
	int n;
	long long A, B, C, D, x0, y0, M;
	cin >>n >>A >>B >>C >>D >>x0 >>y0 >>M;
	
	/*cout <<endl;
	cout <<"x0:"<<x0<<endl;
	cout <<"y0:"<<y0<<endl;
	cout <<"C:"<<C<<endl;
	cout <<"B:"<<B<<endl;
	cout <<"D:"<<D<<endl;*/
	
	vector<long long> xpos(n), ypos(n);
	long long x = x0, y = y0;
	xpos[0] = x0;
	ypos[0] = y0;
	for (int i = 1; i < n; i++) {
		x = xpos[i] = (A * x + B) % M;
		y = ypos[i] = (C * y + D) % M;
		//cout <<i<<": "<<x<<"x"<<y<<endl;
	}

	long long result = 0;
	for (int i = 0; i < n; i++) {
		for (int j = i+1; j < n; j++) {
			for (int k = j+1; k < n; k++) {
				int x1 = xpos[i];
				int x2 = xpos[j];
				int x3 = xpos[k];
				int y1 = ypos[i];
				int y2 = ypos[j];
				int y3 = ypos[k];
				if (((x1 + x2 + x3) % 3 == 0) && ((y1 + y2 + y3) % 3 == 0)) {
					/*float centerx = ((x1 + x2 + x3) / 3.0);
					float centery = ((y1 + y2 + y3) / 3.0);
					cout <<"center "<<centerx << "x" <<centery <<endl;
					cout <<"using "<<i<<" "<<j<<" "<<k<<endl;*/
					

					//if ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) != 0) {
						result++;
					//}
					/*cout <<x1 <<" " <<x2 <<" " <<x3 <<" "<<endl;
					cout <<y1 <<" " <<y2 <<" " <<y3 <<" "<<endl;
					cout <<((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1));
					cout <<endl;*/
				}
			}
		}
	}

	return result;
}

int
main(int argc, char **argv)
{
	int N, n;
	cin >> N;
	for (n = 1; n <= N; n++) {
		long long result = solve();
		cout << "Case #" << n << ": " << result << endl;
	}
	return 0;
}
