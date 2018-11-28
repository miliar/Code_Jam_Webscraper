#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <ctime>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <queue>
#include <utility>
using namespace std;

int h,w;
int data[100][100];
int res[100][100];

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

void replace(int x, int y)
{
	if (x == y) return;
	for (int i=0;i<h;i++) {
		for (int j=0;j<w;j++) {
			if (res[i][j] == x)
				res[i][j] = y;
		}
	}
}

void solve()
{
	for (int i=0;i<100;i++) {
		for (int j=0;j<100;j++) {
			res[i][j] = -1;
		}
	}
	int num = 0;

	for (int i=0;i<h;i++) {
		for (int j=0;j<w;j++) {
			int height = data[i][j];
			int low = -1, small = 100000;
			for (int k=0;k<4;k++) {
				int a = i + dx[k];
				int b = j + dy[k];

				if (a < 0 || b < 0 || a >= h || b >= w)
					continue;

				if (data[a][b] < small) {
					small = data[a][b];
					low = k;
				}
			}

			int resij = res[i][j];
			if (low == -1)
			{
				if (resij == -1) res[i][j] = num++;
				continue;
			}

			int a = i + dx[low];
			int b = j + dy[low];
			int c = data[a][b];
			if (c < height) {
				int resab = res[a][b];
				if (resab == -1) {
					if (resij == -1) {
						res[i][j] = num;
						res[a][b] = num++;
					}
					else
						res[a][b] = resij;
				}
				else if (res[i][j] == -1) {
					res[i][j] = resab;
				}
				else 
					replace(resab, resij);
			}
			else if (resij == -1) {
				res[i][j] = num++;
			}
		}
	}
}

void main()
{
	string str;

	fstream fin("C:\\Projects\\codejam\\Release\\input.txt",std::ios::in);
	fstream fout("C:\\Projects\\codejam\\Release\\output.txt",std::ios::out);

	int n;
	fin >> n;
	getline(fin, str, '\n');

	for (int z=0;z<n;z++)
	{
		fin >> h >> w;
		getline(fin, str, '\n');

		for (int x=0;x<h;x++) {
			for (int y=0;y<w;y++) {
				int temp;
				fin >> temp;
				data[x][y] = temp;
			}
		}

		solve();
		fout << "Case #" << (z+1) << ": " << "\n";
		
		map<int, char> pick;
		int num = 0;
		for (int i=0;i<h;i++) {
			for (int j=0;j<w;j++) {
				map<int, char>::iterator it = pick.find(res[i][j]);
				if (it == pick.end()) {
					fout << (char)('a' + num) << " ";
					pick[res[i][j]] = 'a' + num++;
				}
				else
					fout << pick[res[i][j]] << " ";
			}
			fout << endl;
		}
	}
	fin.close();
	fout.close();
}