#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;

int main() 
{
    freopen("A-large.in", "r", stdin);
    ofstream fp("A-large.out");

	int f[31] = {};
	f[1] = 1;
	for(int i = 2; i <= 30; i++) {
		f[i] = 2 * f[i-1] + 1;
		//cout << f[i] << endl; 
	}

	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		fp << "Case #" << i+1 << ": ";
		int diff = K - f[N];
		if(diff < 0 || diff % (f[N]+1) != 0) {
			fp << "OFF";
		}
		else {
			fp << "ON";
		}
		fp << endl;
	}

    fp.close();
    return 0;
}
