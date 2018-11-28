#include <iostream>

using namespace std;

long long cnt[4][3][3];

int main() {
	int cases;
	cin >> cases;
	for(int c=0; c<cases; c++) {
		int N;
		long long A, B, C, D, x, y, M;

		cin >> N >> A >>B >> C >> D >> x >> y >> M;
		memset(cnt,0,sizeof(cnt));
		cnt[0][0][0] = 1;
		for(int i=0; i<N; i++) {
			for(int got=2; got>=0; got--) for(int ax=0; ax<3; ax++) for(int ay=0; ay<3; ay++) {
				cnt[got+1][(ax+x)%3][(ay+y)%3] += cnt[got][ax][ay];
			}
			x = ((A * x) + B) % M;
			y = ((C * y) + D) % M;
		}

		cout << "Case #" << (c+1) << ": " << cnt[3][0][0] <<endl;

	}
}
