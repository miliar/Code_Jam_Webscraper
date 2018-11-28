#include <iostream>
#include <vector>
using namespace std;

int main() {
	int T;
	cin >> T;
	

	for (int tn=0;tn<T;tn++) {
		int L,N, C;
		long long  t;
		cin >> L >> t >> N >> C;
		vector<int> dist;
		
		for (int i=0;i<C;i++) {
			int d;
			cin >> d;
			dist.push_back(d);
		}
		int len=0;
		for (int i=0;i<N;i++) {
			len += dist[i%C];
			//cout << dist[i%C] << " ";
		}
		//cout << L  << "," << t << endl;
		
		long long t1=0,t2=0;
		double maxsh = 0;
		double sh1 = 0,sh2 = 0;
		if (L>0)
		for (int i=0;i<N;i++) {
			if (t1+dist[i%C]*2<t) {
				t1+=dist[i%C]*2;
				continue;
			}
			if (t1<t) {
				sh1 = dist[i%C] - (t-t1)/2.0;
			} else {
				sh1 = dist[i%C];
			}
			t2 = t1;
			for (int j=i+1;j<=N;j++) {
				if (j==N || L == 1) {
					sh2=0;
					j=N+1;
				} else {
					if (t2+dist[j%C]*2<t) {
						t2+=dist[j%C]*2;
						continue;
					}
					if (t2<t) {
						sh2 = dist[j%C] - (t-t2)/2.0;
					} else {
						sh2 = dist[j%C];
					}

				}
				if (sh1 + sh2 > maxsh){
					maxsh = sh1+sh2;
					//cout << i << " " << j  << " "<< sh1  << " "<< sh2 << endl;
				}
				t2+=dist[j%C]*2;
			}
			t1+=dist[i%C]*2;
		}
		

		cout << "Case #" << (tn+1) << ": "  << (long)(len*2-maxsh) << endl;
		if ((long)(len*2-maxsh) != (len*2-maxsh)) {
			cout << "ERR!" << endl;
			break;
		}
	}

	return 0;
}
