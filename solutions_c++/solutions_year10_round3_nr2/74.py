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
    freopen("A-small.in", "r", stdin);
    ofstream fp("A-small.out");

	int T;
	scanf("%d", &T);

	for(int i = 0; i < T; i++)
	{
		int L, P, C;
		scanf("%d%d%d", &L, &P, &C);

		int cnt = 0;
		long long V = (long long)L * C;
		while(V < P) {
			V *= C;
			cnt ++;
		}

		int res = 0;
		while(cnt >= 1) {
			cnt /= 2;
			res++;
		}

		
		fp << "Case #" << i+1 << ": " << res << endl;
	}

    fp.close();
    return 0;
}