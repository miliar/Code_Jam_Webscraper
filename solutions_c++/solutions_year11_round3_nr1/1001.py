#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>

#define min(a, b) (((a)<(b))?(a):(b))
#define max(a, b) (((a)>(b))?(a):(b))
#define abs(a) ((a)>(0)?(a):(-(a)))

using namespace std;


char mas[300][300];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n, t;

	cin >> t;

	for(int ii = 0; ii < t; ++ii){
		int m;
		cin >> n >> m;
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j)
				cin >> mas[i][j];

		bool pr = true;
		bool pr2 = true;
		while ((pr) && (pr2)){
			pr2 = false;
			for(int i = 0; i < n; ++i){
				for(int j = 0; j < m; ++j){
					if (mas[i][j] == '#'){
						pr2 = true;
						if ((i + 1 < n) && (j + 1 < m)){
							if ((mas[i + 1][j] == '#') && (mas[i][j + 1] = '#') && (mas[i + 1][j + 1] == '#')){
								mas[i + 1][j + 1] = mas[i][j] = '/';
								mas[i][j + 1] = mas[i + 1][j] = '\\';
							}
							else{
								pr = false;
								break;
							}

						}
						else{
							pr = false;
							break;

						}
					}
				}
				if (!pr)
					break;
			}
		}
		cout << "Case #"<< ii + 1 << ':'<<endl;
		if (!pr)
			cout << "Impossible" << endl;
		else{
			for(int i = 0; i < n; ++i){
				for(int j = 0; j < m; ++j)
					cout << mas[i][j];
				cout << endl;
			}


		}
	}



	return 0;
}