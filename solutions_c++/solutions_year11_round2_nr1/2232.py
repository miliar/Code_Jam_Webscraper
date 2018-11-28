#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
#define For(I,A,B) for(int I = A; I < B; ++I)
using namespace std;

int main (){
	ifstream cin ("A-large.in");
	ofstream cout ("output.txt");
	int T,t = 0;
	cout.precision(8);
	cin >> T;
	while (t<T){
		int N;
		cout << "Case #" << ++t << ": " << endl;
		cin  >> N;
		vector <string> a;
		string s;
		For(i,0,N){
			cin >> s;
			a.push_back(s);
		}
		vector <pair <int,int> > wp(N);
		For(i,0,N){
			int g=0;int w = 0;
			For(j,0,N)
				if (a[i][j] != '.'){
					++g;
					if (a[i][j] == '1') ++w;
				}
			wp[i].first = g;
			wp[i].second = w;
		}
		vector <double> owp(N),oowp(N);
		For(i,0,N){
			double q = 0;
			For(j,0,N){
				if (a[j][i] != '.')
					if (a[j][i] == '1') q += ((double)wp[j].second - 1)/((double)wp[j].first -1);
					else				q += (double)wp[j].second/((double)wp[j].first - 1); 
			}
			owp[i] = q / (wp[i].first);
		}
		For(i,0,N){
			double q = 0;
			For(j,0,N)
				if (a[i][j] != '.')
					q += owp[j];
			oowp[i] = q / wp[i].first;
		}
		vector<double> WP(N);
		For(i,0,N)
			WP[i] = (double)wp[i].second/(double)wp[i].first;
		For(i,0,N)
			cout << 0.25 * WP[i] + 0.50 * owp[i] + 0.25 * oowp[i] <<endl;
	}
	return 0;
}