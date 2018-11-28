#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <iostream>
#include <map>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define MAXN 10240

int l[MAXN];
int d[MAXN];
int s[MAXN];

int main(int argc, char *argv[]){
	unsigned int T;
	int N, D;
	
	if (argc >= 2){
		freopen(argv[1], "r", stdin);
		string outstr(argv[1]);
		int dot_pos = outstr.find_last_of('.');
		outstr = outstr.substr(0, dot_pos) + ".out";
		freopen(outstr.c_str(), "w", stdout);
	}

	cin >> T;
	for (unsigned int k = 1; k <= T; k++){
		cin >> N;
		for (int i = 0; i < N; i++)
			cin >> d[i] >> l[i];
		cin >> D;
		
		for (int i = 0; i < N; i++)
			s[i] = -1;
		
		s[0] = d[0];
		bool result = false;
		for (int i = 0; i < N; i++){
			if (D <= d[i] + s[i]){
				result = true;
				break;
			}
			for (int j = i+1; j < N && d[j] <= d[i] + s[i]; j++)
				s[j] = max(s[j], min(d[j] - d[i], l[j]));
		}
		
		cout << "Case #" << k << ": " << (result ? "YES" : "NO") << endl;
	}
	return 0;
}
