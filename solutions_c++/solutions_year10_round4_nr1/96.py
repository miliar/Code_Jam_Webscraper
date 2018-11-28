#include <iostream>
#include <vector>
#include <algorithm>

#define INFTY 10000
#define VI vector<int>

using namespace std;

int tests;

int K;
vector<vector<int> > data;

long long res;

void read_test(){
	cin >> K;
	data = vector<vector<int> >(4*K,vector<int>(4*K,-1));
	for(int i=0; i<2*K-1; i++){
		if (i < K)
			for(int j=0;j<i+1;j++)
				cin >> data[i][K-i-1+2*j];
		else
			for(int j=0; j<2*K-i-1; j++)
				cin >> data[i][i-K+1+2*j];
	}
/*
	for(int i=0; i < 2*K-1; i++){
		for(int j=0; j < 2*K-1; j++)
			if (data[i][j] == -1)
				cout << " ";
			else
				cout << data[i][j];
		cout << endl;
	}*/
}

int hor_sym(int a){
	for(int x=0; x<a; x++)
	for(int y=0; y<2*K-1; y++)
		if (data[x][y] != -1 && data[2*a-x][y] != -1 && data[x][y] != data[2*a-x][y])
			return 0;
	return 1;
}

int vert_sym(int a){
	for(int y=0; y<a; y++)
	for(int x=0; x<2*K-1; x++)
		if (data[x][y] != -1 && data[x][2*a-y] != -1 && data[x][y] != data[x][2*a-y])
			return 0;
	return 1;
}

void solve_test(){
	vector<int> hor_axis(2*K);
	vector<int> vert_axis(2*K);
	int min_hor = INFTY;
	int min_vert = INFTY;
	for(int i=0; i < 2*K-1; i++){
		hor_axis[i] = hor_sym(i);
	//	cout << "HOR: " << i << " " << hor_axis[i] << endl;
		if (hor_axis[i])
			min_hor = min(min_hor,K+(int)abs(K-1-i)); 
		vert_axis[i] = vert_sym(i);
	//	cout << "VER: " << i << " " << vert_axis[i] << endl;
		if (vert_axis[i])
			min_vert = min(min_vert,K+(int)abs(K-1-i));
	}
	int m = min_hor+min_vert-K;
	//cout << min_hor << " " << min_vert << " " << m << endl;	
	res = m*m-K*K;
}

void dump_sol(int i){
	cout << "Case #" << i << ": " ;
	cout << res << endl;
}

int main(){
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
		solve_test();
		dump_sol(i+1);
	}
}
