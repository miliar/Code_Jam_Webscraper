// MinimumScalarProduct.cpp

#include <windows.h>
#include <tchar.h>
#include <stdio.h>
#include <fstream>
#include <xstring>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
	ifstream ifs("C:\\Users\\Haruaki Hinami\\Desktop\\input.txt");
	ofstream ofs("C:\\Users\\Haruaki Hinami\\Documents\\Visual Studio 2008\\Projects\\Code_Jam\\MinimumScalarProduct\\MinimumScalarProduct\\output.txt");

	char inputBuf[1024] = {0};
	char outputBuf[1024] = {0};

	while (!ifs.eof()) {
		ifs.getline(inputBuf, sizeof(inputBuf));
		int T = atoi(inputBuf);

		for (int i=0; i<T; ++i) {
			ifs.getline(inputBuf, sizeof(inputBuf));
			int n = atoi(inputBuf);

			vector<int> listX;
			for (int j=0; j<n; ++j) {
				if (n-1 == j) {
					ifs.getline(inputBuf, sizeof(inputBuf));
				} else {
					ifs.getline(inputBuf, sizeof(inputBuf), ' ');
				}
				int item = atoi(inputBuf);
				listX.push_back(item);
			}
			sort(listX.begin(), listX.end());

			vector<int> listY;
			for (int j=0; j<n; ++j) {
				if (n-1 == j) {
					ifs.getline(inputBuf, sizeof(inputBuf));
				} else {
					ifs.getline(inputBuf, sizeof(inputBuf), ' ');
				}
				int item = atoi(inputBuf);
				listY.push_back(item);
			}
			sort(listY.begin(), listY.end(), greater<int>());

			int scalar = 0;
			for (int j=0; j<n; ++j) {
				int temp = listX[j] * listY[j];
				scalar += temp;
			}

			printf("Case #%d: %d\n", i+1, scalar);
			_snprintf_s(outputBuf, _TRUNCATE, "Case #%d: %d\n", i+1, scalar);
			ofs.write(outputBuf, strlen(outputBuf));
		}
	}

	getc(stdin);
	exit(0);
}
