#include <iostream>
#include <fstream>
#include <string.h>
#include <iomanip>

using namespace std;

const int maxwid = 200;
const int dx[4] = {-1,0,0,1};
const int dy[4] = {0,-1,1,0};
int alt[maxwid][maxwid], r[maxwid][maxwid];
int res[maxwid*maxwid];
int m,n;
	
int root(int j)
{
	if (r[j/n][j % n] == j) return j;
	r[j/n][j%n] = root(r[j/n][j%n]);
	return  r[j/n][j%n];
}

int main(int argc, char ** argv)
{
	//cout << argv[2] << endl;
	fstream fin;
	ofstream fout;
	fin.open(argv[1]);
	fout.open(argv[2]);
	
	int i,j,k,t, tmp, nx, ny, oroot, d;
	fin >> t;
	//cout << n << endl;
	for (i = 1;i <= t;i ++)
	{
		fin >> m >> n;
		for (j = 0;j < m;j ++)
			for (k = 0;k < n;k ++)
			{
				fin >> alt[j][k];
				r[j][k] = j * n + k;
			}
		for (j = 0;j < m;j ++)
			for (k = 0;k < n;k ++){
				tmp = alt[j][k];
				for (d = 0;d < 4;d ++) {
					nx = dx[d] + j;
					ny = dy[d] + k;
					if (nx < m && nx >= 0 && ny >=0 && ny <n && alt[nx][ny]< tmp) {
						r[j][k] = root(r[nx][ny]);
					//fout << j << " " << k << " " << oroot << " " << r[oroot/n][oroot%n]<<endl;
						tmp = alt[nx][ny];
					}
				}
			}
		memset(res,0,sizeof(res));
		tmp = 0;
		fout << "Case #" << i << ": " << endl;
		for (j = 0;j < m;j ++) {
			for (k = 0;k < n;k ++) {
				//cout << j << " " << k << " " << root(r[j][k])<<endl;
				if (res[root(r[j][k])] == 0) {
					tmp ++;
					res[root(r[j][k])] = tmp;
				}
				fout << char('a'+(res[root(r[j][k])] - 1)) << ' ';
			}
			fout << endl;
		}
	}
	fout.close();
	fin.close();
}
