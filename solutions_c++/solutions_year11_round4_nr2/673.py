#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<string>
#include<cmath>
using namespace std;
#define PII pair<int, int>
#define EPS 1e-9
int main(){
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B0.out");
	int tc;
	fin >> tc;
	int r, c, d;
	for(int i = 0; i < tc; i++){
		fin >> r >> c >> d;
		int m = min(r, c);
		string gr[10];
		for(int i = 0; i < r; i++)
				fin >> gr[i];
		int ans = -1;
		for(int l = m; l > 2 && ans == -1; l--){
			for(int i = 0; i <= r - l && ans == -1; i++){
				for(int j = 0; j <= c - l && ans == -1; j++){
					double midx = l / 2., midy = l / 2.;
					double sx = 0, sy = 0;
					for(int x = i; x < i + l; x ++){
						for(int y = j; y < j + l; y++){
							if(x == i && (y == j || y == j + l - 1))
								continue;
							if(x == i + l - 1 && (y == j || y == j + l - 1))
								continue;
							double kx = x - i + .5, ky = y - j + .5;
							sx += (midx - kx) * (gr[x][y] - '0');
							sy += (midy - ky) * (gr[x][y] - '0');

						}
					}
					if(fabs(sx) < EPS && fabs(sy) < EPS)
						ans = l;
				}
			}
		}
		fout << "Case #"<< i + 1 << ": ";
		if(ans != -1)
			fout << ans << endl;
		else
			fout << "IMPOSSIBLE" << endl;
	}
	return 0;
}