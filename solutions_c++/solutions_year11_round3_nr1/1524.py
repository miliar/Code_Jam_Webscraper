#include<cstdio>
#include<iostream>
using namespace std;

int T, R, C;
char matrix[51][51];

void displayMatrix() {
	int i;
	for (i = 0; i < R; i++)
		cout<<matrix[i]<<"\n";
}

int changeMatrix() {
	int i,j;
	int ok = 0;
	for (i = 0; i < R - 1; i++)
		for (j = 0; j < C - 1; j++) {
			if (matrix[i][j] == '#') {
				if ((matrix[i+1][j] == '#') && (matrix[i][j+1] == '#') && (matrix[i+1][j+1] == '#')) {
					matrix[i][j] = '/';
					matrix[i][j + 1] = '\\';
					matrix[i + 1][j] = '\\';
					matrix[i + 1][j + 1] = '/';
																		
				}
				else ok = 1;
			}
		}
	for (i = 0; i < R; i++)
		if (matrix[i][C -1] == '#') ok = 1;
	for (i = 0; i < C; i++)
		if (matrix[R - 1][i] == '#') ok = 1;

	return ok;
}

int main() {
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int k,i,j;
	cin>>T;
	for (k = 0; k < T; k++) {
		cin>>R>>C;
		for (i = 0; i < R; i++)
			cin>>matrix[i];
		cout<<"Case #"<<(k+1)<<":\n";
		int ret = changeMatrix();
		if (!ret) displayMatrix();
			else cout<<"Impossible"<<"\n";	
	
	}

	


	return 0;
}
