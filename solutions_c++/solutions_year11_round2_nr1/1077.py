#include <iostream>
#include <array>
#include <vector>
#include <cassert>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <iomanip>
#include <list>

using namespace std;

char GAMES[100][100];

vector<double> solve(int N) {
	vector<int> P(N);
	for (int i=0;i < N;++i)
		P[i] = count_if(&GAMES[i][0],&GAMES[i][N],[=](char c) {return c != '.';});
	
	vector<int> WP (N);
	for (int i=0;i < N;++i)
		WP[i] = double(count(&GAMES[i][0],&GAMES[i][N],'1'));
	
	vector<double> OWP (N);
	for (int i=0;i < N;++i) {
		double tot=0;
		for (int j=0;j <N;++j)
			if (GAMES[i][j] != '.')
				tot+=double(WP[j]- (GAMES[j][i] == '1'))/(P[j]-1);
		OWP[i] = tot/P[i];
	}
	
	vector<double> OOWP (N);
	for (int i=0;i < N;++i) {
		double tot= 0;
		for (int j=0;j < N;++j)
			if (GAMES[i][j] != '.')
				tot+=OWP[j];
		OOWP[i] = tot/P[i];
	}
	
// 	cout << "DEBUG data:" << endl;
// 	for (int i=0;i < N;++i)
// 		cout << double(WP[i])/P[i] << " ";
// 	
// 	cout << endl;
// 	for (int i=0;i < N;++i)
// 		cout << double(OWP[i]) << " ";
// 	
// 	cout << endl;
// 	for (int i=0;i < N;++i)
// 		cout << double(OOWP[i]) << " ";
// 	cout << endl;
	
	vector<double> ans(N);
	for (int i=0;i < N;++i)
		ans[i] = 0.25*double(WP[i])/P[i] + 0.50*OWP[i] + 0.25*OOWP[i];
	return ans;
}

int main(int argc, char **argv) {
	cout << fixed << setprecision(12);
	int T;
	cin >> T;

	for(int i=0;i < T;++i) {
		int N;
		cin >> N;
		
		memset(GAMES,0,sizeof(GAMES));
		
		for (int j=0;j < N;++j) {
			cin >> GAMES[j];
		}
		
		cout << "Case #" << i+1 << ":" << endl;
		vector<double> ans = solve(N);
		
		for (int i=0;i < ans.size();++i) 
			cout << ans[i] << endl;
	}
	
    return 0;
}
