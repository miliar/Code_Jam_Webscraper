#include<iostream>
#include<climits>
#include<cstring>
#include<string>
#define FOR(a, b, c) for(int a=b; a<=c; a++)

using namespace std;

int R , C;
const int MaxRC = 100;
int Matrix[MaxRC + 1][MaxRC + 1];
char Output[MaxRC + 1][MaxRC + 1];
int Visit[MaxRC + 1][MaxRC + 1];
int basin;

void init(void){
	memset(Matrix, 0 , sizeof(Matrix));
	memset(Output, 0 , sizeof(Output));
	cin >> R >> C;
	FOR(i, 1, R){
		FOR(j, 1, C){
			cin >> Matrix[i][j];
		}
	}
	basin = 0;
}

const int pn = 4;
const int py[pn + 1] = {0 , -1 , 0 , 0 , 1};
const int px[pn + 1] = {0 , 0 , -1 , 1 , 0};

char det(int i , int j){
	int M = Matrix[i][j];
	int ii = - 1, jj = -1;
	FOR(k, 1, pn){
		int y = i + py[k];
		int x = j + px[k];
		if(y > 0 && y <= R && x > 0 && x <= C && M > Matrix[y][x]){
			M = Matrix[y][x];
			ii = y;
			jj = x;
		}
	}
	if (ii == -1){
		return char('a' + (basin++));
	} else{
		if (!Output[ii][jj]){
			Output[ii][jj] = det(ii,jj);
		}
		return Output[ii][jj];
	}
}

void process(void){
	FOR(i, 1, R){
		FOR(j, 1, C){
			if(Output[i][j] == 0){
				Output[i][j] = det(i, j);
			}
		}
	}
}

void out(void){
	FOR(i, 1, R){
		FOR(j,1 ,C){
			cout << Output[i][j] << ' ' ;
		}
		cout << endl;
	}
}

int main(void){
	int N;
	cin >> N;
	FOR(i, 1, N){
		init();
		process();
		cout << "Case #" << i << ":" << endl;
		out();
	}
	return 0;
}
