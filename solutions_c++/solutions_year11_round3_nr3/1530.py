#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <map>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int f[10240];

int main(int argc, char *argv[]){
	unsigned int T;

	if (argc >= 2){
		freopen(argv[1], "r", stdin);
		string outstr(argv[1]);
		int dot_pos = outstr.find_last_of('.');
		outstr = outstr.substr(0, dot_pos) + ".out";
		freopen(outstr.c_str(), "w", stdout);
	}

	cin >> T;
	for (unsigned int k = 0; k < T; k++){
		int N;
		int L, H;
		cin >> N >> L >> H;
		
		for (int i = 0; i < N; i++)
			cin >> f[i];
		
		bool finished = false;
		for (int d = L; d <= H; d++){
			bool d_works = true;
			for(int i = 0; i < N; i++){
				//cout << f[i] << "  " << d << endl;
				if ((f[i] % d != 0) && (d % f[i] != 0)){
					d_works = false;
					break;
				}
			}

			if (d_works){
				cout << "Case #" << k+1 << ": " << d << endl;	
				finished = true;
				break;		
			}
		}

		if (!finished)
			cout << "Case #" << k+1 << ": " << "NO" << endl;
	}
	return 0;
}
