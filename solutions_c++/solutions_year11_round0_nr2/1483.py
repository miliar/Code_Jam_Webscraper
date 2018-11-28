#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <sstream>
#include <stack>
#include <vector>

#include <limits.h>
#include <math.h>
#include <stdio.h>

using namespace std;

#define foreach(k, b, N) for (int k = b; k <= N; k++)
#define foreach_r(k, b, N) for (int k = b; k >= N; k--)

int
main()
{
	int cases; 
	int result = 0;
	char inv[50][2];
	char res[50];

	char opp1[50];
	char opp2[50];

	string tmp;

	cin >> cases;

	getline(cin, tmp);
	foreach(i, 1, cases) {
		getline(cin, tmp);
		istringstream ss(tmp);

		int C;
		ss >> C;
		foreach(j, 0, C - 1) {
			string c;

			ss >> c;
			foreach(k, 0, 1)
				inv[j][k] = c[k];
			res[j] = c[2];
		}

		int D;
		ss >> D;
		foreach(j, 0, D - 1) {
			string c;

			ss >> c;
			opp1[j] = c[0];
			opp2[j] = c[1];
		}

		int N;
		ss >> N;

		string str;
		ss >> str;

		int cur = 0;
		string output = "";

		int flag = 0;
		foreach(j, 0, N - 1) {
			char invoke = str[j];
			flag = 0;

			foreach(k, 0, C - 1) {
				if (output.length() > 0 &&
						((inv[k][0] == output[output.length() - 1] &&
						inv[k][1] == invoke) ||
						(inv[k][1] == output[output.length() - 1] &&
						 inv[k][0] == invoke))) {
					output.replace(output.length() - 1, 1, 1, res[k]);
					flag = 1;
					break;
				}
			}

			if (flag == 1)
				continue;

			foreach(k, 0, D - 1) {
				if (opp1[k] == str[j] && output.length() > 0) {
					foreach(l, 0, output.length() - 1) {
						if (output[l] == opp2[k]) {
							output.erase();
							flag = 1;
							break;
						}
					}
					if (flag == 1)
						break;
				}
				else if (opp2[k] == str[j] && output.length() > 0) {
					foreach(l, 0, output.length() - 1) {
						if (output[l] == opp1[k]) {
							output.erase();
							flag = 1;
							break;
						}
					}
					if (flag == 1)
						break;
				}
			}

			if (flag == 0)
				output.append(1, str[j]);
		}

		printf("Case #%d: [", i);
		if (output.length() > 0)
		foreach(j, 0, output.length() - 1) {
			printf("%c", *(output.c_str() + j)); 

			if (j != output.length() - 1)
				printf(", ");
		}

		printf("]\n");
	}

	return 0;
}
