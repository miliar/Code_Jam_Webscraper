#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <string>
#include <queue>
#include <cmath>
#include <numeric>
#include <list>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <climits>
#include <set>
#include <memory.h>
#include <memory>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <map>
#include <cassert>
#include <time.h>
#define _USE_MATH_DEFINES
using namespace std;

typedef long long ll;
typedef pair<int, int> P;
typedef pair<int, P> PP;
typedef pair<string, int > Ps;
typedef vector<int> vec;
typedef vector<vec> mat;
const int INF = 1 << 30;
const double EPS = 1e-9;

char table[200][200];

P wp[200];

double owp[200];

double oowp[200];

int main(){
	
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	
	int n, T;
	cin >> T;
	for(int t = 0; t < T; t++){
		cin >> n;

		for(int i = 0; i < n; i++){
			int w = 0;
			int l = 0;
			for(int j = 0; j < n; j++){
				cin >> table[i][j];
				if(table[i][j] == '1'){
					w++;
				}else if(table[i][j] == '0')
					l++;
			}
			wp[i] = P(w, w + l);
		}
		for(int i = 0; i < n; i++){
			double sum = 0;
			int c = 0;
			for(int j = 0; j < n; j++){
				if(table[i][j] == '1' || table[i][j] == '0'){
					c++;
					if(table[i][j] == '1'){
						sum += (double)(wp[j].first) / (wp[j].second - 1);
					}else{
						sum += (double)(wp[j].first - 1) / (wp[j].second - 1);
					}
				}
			}
			owp[i] = sum / c;
		}
		for(int i = 0; i < n; i++){
			double sum = 0;
			int c = 0;
			for(int j = 0; j < n; j++){
				if(table[i][j] == '1' || table[i][j] == '0'){
					sum += owp[j];
					c++;
				}
			}
			oowp[i] = sum / c;
		}
		cout << "Case #" << t + 1 << ":" << endl;
		for(int i = 0; i < n; i++){

			cout << fixed << setprecision(9) <<  0.25 * (double)wp[i].first / wp[i].second + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
		}
	}

	
	cin.close();
	cout.close();
	
	return 0;
}