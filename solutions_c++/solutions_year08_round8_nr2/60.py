# include <cstdio>
# include <cstdlib>
# include <set>
# include <map>
# include <vector>
# include <algorithm>
# include <cmath>
# include <fstream>
# include <iomanip>
# include <sstream>
# include <string>
# include <iostream>
# include <memory>

using namespace std;

ifstream fin ("input.txt");
ofstream fout ("output.txt");

int l [20];
int r [20];
int c [20];

int cnt [2][1 << 14];

int main () {

	int tests; 

	fin >> tests;
	
	for (int test = 1; test <= tests; ++ test) {
	
		map  <string, int> color ;
	
		int n ; 
		fin >> n ;

		for (int i = 0; i < n; ++ i) {
		
			string c ;

			fin >> c >> l[i] >> r[i];

			if (color[c] !=  0) {
				:: c[i] = color[c];
			}
			else {
				color [c] = color.size();
				:: c[i] = color.size();
			}
		}
			int ccnt = color.size();

			int res = -1;

			for (int c1 = 1; c1 <= ccnt; ++ c1)
			for (int c2 = c1; c2 <= ccnt; ++ c2)
				for (int c3 = c2; c3 <= ccnt; ++ c3) {
				
					memset (cnt, 0xff, sizeof (cnt));

					for (int i = 0; i < n; ++ i) 
						if (c[i] == c1 || c[i] == c2 || c[i] == c3)
						if (l[i] == 1) {
							cnt [0][i] = 1;
						}

					int curr = 0;

					for (int i = 2; i <= 10000; ++ i) {
					
						for (int j = 0; j < n; ++ j) 
							if (c[j] == c1 || c[j] == c2 || c[j] == c3)
							{
						
							if (l[j] > i)
							{
								cnt [1 - curr][j] = -1;	
								continue ;
							}
							if (r[j] < i){
								cnt [1 - curr][j] = -1;		
								continue ;
							}

							cnt [1 - curr][j] = cnt [curr][j];
						
							for (int q = 0; q < n; ++ q)
								if (c[q] == c1 || c[q] == c2 || c[q] == c3)
							{
								if (cnt [curr][q] != -1){
								
									if (cnt [1 - curr][j] == -1 || cnt [1 - curr][j] > cnt [curr][q] + 1) {
									
										cnt [1 - curr][j] = cnt [curr][q] + 1;
									}
								}
							}
						}

						curr = 1 - curr;
					}

					for (int i = 0; i < n; ++ i)
						if (cnt [curr][i] != -1)
							if (res == -1 || res > cnt [curr][i]) res = cnt [curr][i];
				}

				fout << "Case #" << test << ": ";

				if (res == -1) fout << "IMPOSSIBLE";
				else fout << res;

				fout << endl;
	}


	return 0;
}
