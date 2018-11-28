#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

int Ca, N, M;

bool A[20][20];
bool B[20][20];

int C[20];
bool mark[20];

bool flag;

void find(int i){
	if (flag) return;
	if (i > M){
		for (int x=1;x<=M;++x)
			for (int y=1;y<=M;++y)
				if (B[x][y])
					if (!A[C[x]][C[y]]){
						flag = false;
						return;
					}
		flag = true;
		return;
	}

	for (int k=1;k<=N;++k)
		if (!mark[k]){
			mark[k] = true;
			C[i] = k;
			find(i+1);
			mark[k] = false;
		}
}

int main(){
	ifstream fin("d.in");
	ofstream fout("d.out");

	fin>>Ca;
	for (int Case = 1; Case <= Ca; ++Case){
		fin>>N;

		memset(A, 0, sizeof(A));
		for (int i=1;i<N;++i){
			int x, y;
			fin>>x>>y;
			A[x][y] = true;
			A[y][x] = true;
		}

		fin>>M;
		memset(B, 0, sizeof(B));
		for (int i=1;i<M;++i){
			int x, y;
			fin>>x>>y;
			B[x][y] = true;
			B[y][x] = true;
		}

		fout<<"Case #"<<Case<<": ";

		flag = false;
		memset(mark, 0, sizeof(mark));
		find(1);
		if (flag) fout<<"YES"<<endl;
		else fout<<"NO"<<endl;
	}

	return 0;
}
