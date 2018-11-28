#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>

#define min(a, b) (((a)<(b))?(a):(b))
#define max(a, b) (((a)>(b))?(a):(b))

using namespace std;
int mas[200][200];
double scores[200];
double wp[200];
double wp1[200][200];
double oowp[200];
double owp[200];
int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t, n;

	cin >> t;
	for(int ii = 0; ii < t; ++ii){
		cin >> n;
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < n; ++j){
				char c;
				cin >> c;
				if (c == '.')
					mas[i][j] = -1;
				else
					mas[i][j] = c - '0';

			}
	
			for(int i = 0; i < n; ++i){
				int stch = 0;
				wp[i] = 0;
				for(int j = 0; j < n; ++j)
					wp1[i][j] = 0;
				for(int j = 0; j < n; ++j){
					if (mas[i][j] != -1){
						stch++;
						wp[i] += mas[i][j];
					}

				}
				
				for(int j = 0; j < n; ++j)
					if (mas[i][j] != -1){
						wp1[i][j] = wp[i] - mas[i][j];
						wp1[i][j] /= (double) stch - 1;
					}

				wp[i] /= (double) stch;
				//wp[i] *= 0.25;

			}
			for(int i = 0; i < n; ++i){
				int stch = 0;
				owp[i] = 0;
				for(int j = 0; j < n; ++j){
					if (mas[i][j] != -1){
						stch++;
						owp[i] += wp1[j][i];
					}

				}
				owp[i] /= (double) stch;
				//owp[i] *= 0.5;
			}

			for(int i = 0; i < n; ++i){
				int stch = 0;
				oowp[i] = 0;
				for(int j = 0; j < n; ++j){
					if (mas[i][j] != -1){
						stch++;
						oowp[i] += owp[j];
					}

				}
				oowp[i] /= (double) stch;
				//oowp[i] *= 0.25;
			}
			cout << "Case #" << ii + 1 <<':'<< endl;
			for(int i = 0; i < n; ++i)
				printf("%.6f\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);

	}



	return 0;
}