#include <iostream>
#include <vector>
#include <utility>
#include <iomanip>

using namespace std;

int main (){
	int T, X, S, R, N, t;
	cin >> T;
	for (int c = 0; c < T; c++){
		cin >> X >> S >> R >> t >> N;
		vector <pair <int, int> > dist;
		int sum = 0;
		for (int i = 0; i < N; i++){
			int st, en;
			cin >> st >> en;
			pair <int, int> data;
			data.first = en - st;
			sum += en - st;
			cin >> data.second;
			dist.push_back (data);
		}
		if (sum != X){
			pair <int, int> data;
			data.first = X - sum;
			data.second = 0;
			dist.push_back (data);
			N++;
		}
		for (int i = 1; i < N; i++){
			for (int j = 0; j < N - 1; j++){
				if (dist[j].second > dist[j+1].second){
					pair <int, int> temp;
					temp = dist[j];
					dist[j] = dist[j+1];
					dist[j+1] = temp;
				}
			}
		}
		double C_T = 0;
		double T_T = t;
		int m = 0;
		for (m = 0; m < N; m++){
			if (S >= R){
				break;
			}
			double time = dist[m].first / (1.0 * (dist[m].second + R) );
			if (time > T_T){
				C_T += T_T;
				C_T += (dist[m].first-T_T*(R+dist[m].second)) / (1.0 * (dist[m].second) + S);
				m++;
				break;
			}
			C_T += time;
			T_T -= time;
		}
		for ( ; m < N; m++){
			C_T += (dist[m].first) / (1.0 * (dist[m].second) + S);
		}
		cout << "Case #" << c+1 << ": ";
		cout << setiosflags(ios::fixed) << setprecision(10) << C_T;
		if (c != T-1){
			cout << endl;
		}
	}
}