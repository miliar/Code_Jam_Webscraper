#include <iostream>
using namespace std;
typedef long long int lli;
#define ZER(X) memset(X,0,sizeof(X));

const int MAX = 50 +1;
int M[MAX][MAX];
int R, C;

int parse(char c){
	switch(c){
	case '.': return 0;
	case '#': return 1;
	}
	cerr << "parse" << endl;
	exit(1);
}

bool isBlue(int i, int j){
	if(i<0 || i>=R)
		return false;
	if(j<0 || j>=C)
		return false;
	return M[i][j]==1;
}

bool color(int i, int j){
	if(!isBlue(i,j) || !isBlue(i+1,j) ||!isBlue(i,j+1) ||!isBlue(i+1,j+1) )
		return false;
	M[i][j] = M[i+1][j+1] = 2;
	M[i+1][j] = M[i][j+1] = 3;
	return true;
}

char print(int i){
	switch(i){
	case 0: return '.';
	case 2: return '/';
	case 3: return '\\';
	}
	cerr << "print" << endl;
	exit(1);
}

int main(){
	int Cases;
	cin >> Cases;
	for(int Case=1; Case <= Cases; ++Case){

		cin >> R >> C;
		for (int i = 0; i < R; ++i){
			for (int j = 0; j < C; ++j){
				char c;
				cin >> c;
				M[i][j] = parse(c);
			}
		}


		bool possible = true;
		for (int i = 0; i < R && possible; ++i){
			for (int j = 0; j < C && possible; ++j){
				if(isBlue(i,j)){
					possible = color(i,j);
				}
			}
		}

		cout << "Case #" << Case << ": \n";
		if(possible){
			for (int i = 0; i < R && possible; ++i){
				for (int j = 0; j < C && possible; ++j){
					cout << print(M[i][j]);
				}
				cout << "\n";
			}
		}
		else
			cout << "Impossible\n";


	}
	return 0;
}