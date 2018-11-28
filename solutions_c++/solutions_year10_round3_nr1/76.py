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

	int A[1000];
	int B[1000];

	int T;
	scanf("%d", &T);

	for(int i = 0; i < T; i++)
	{
		int N;
		scanf("%d", &N);
		for(int j = 0; j < N; j++) {
			scanf("%d%d", &(A[j]), &(B[j]));
		}

		int res = 0;
		for(int j = 0; j < N; j++) {
			for(int k = j+1; k < N; k++) {
				if((A[j] < A[k]) != (B[j] < B[k])) {
					res ++;
				}
			}
		}
		
		fp << "Case #" << i+1 << ": " << res << endl;
	}

    fp.close();
    return 0;
}