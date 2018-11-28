#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <stdio.h>
#include <math.h>

using namespace std;

char buffer[1024];

int main() {
	int numtests;
	int mat[52][502];
	char we[] = "welcome to code jam";
	scanf("%d\n",&numtests);
	for(int t = 1; t <= numtests; ++t) {
		gets(buffer);
		memset(mat,0,sizeof(mat));
		mat[0][0] = (buffer[0] == we[0]);
		for(int i = 1; i < strlen(buffer); i++) {
			mat[0][i] = mat[0][i-1];
			if(buffer[i] == we[0])
				mat[0][i]++;
		}
		for (int i = 1; i < strlen(we); i++) {
			for (int j = 1; j < strlen(buffer); j++) {
				mat[i][j] = mat[i][j-1] % 10000;
				if (buffer[j] == we[i]) {
					mat[i][j] = (mat[i][j] + mat[i-1][j-1]) % 10000;
				}
			}
		}
		cout << "Case #" << t << ": " << setfill('0') << setw(4) << mat[strlen(we)-1][strlen(buffer)-1] << endl;
	}
	return 0;
}
