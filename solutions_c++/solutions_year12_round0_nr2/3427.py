/** Librerias **/
#include <iostream>
#include <iomanip>
#include <limits>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstdio>
#include <ctime>
#include <cmath>
#include <cstring>
#include <cctype>
#include <sstream>

/** Namespaces **/
using namespace std;

/** Cuerpo principal **/
int main(){
	int T;
	cin >> T;

	for (int caso = 1; caso <= T; caso++){
		int N, S, p;
		cin >> N >> S >> p;

		vector<int> vec_tp(N);
		for (int ii = 0; ii < N; ii++)
			cin >> vec_tp[ii];

		int cont_s = 0, cont_g = 0;
		for (int ii = 0; ii < N; ii++){
			int mod = vec_tp[ii] % 3;
			int best = vec_tp[ii] / 3;
			if (mod > 0)
				best++;

			if (best >= p)
				cont_g++;
			else if ((cont_s < S) && (best > 0) && (mod != 1) && ((p - best) == 1)){
				cont_g++;
				cont_s++;
			}
		}
		cout << "Case #" << caso << ": " << cont_g << endl;
	}

	//FIN
	return 0;
}
