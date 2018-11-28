#include <vector>
#include <set>
#include <map>
#include <queue>
#include <iostream>
using namespace std;

int X;
vector<vector<bool> > M;

vector<int> swap(vector<int> e, int a, int b){
	int c = e[a];
	e[a] = e[b];
	e[b] = c;
	return e;
}

bool solucion(vector<int> &e){
	for(int i = 0; i < X; i++){
		for(int j = i+1; j < X; j++)
			if (M[e[i]][j]) return false;
	}
	return true;
}

void print(vector<int> &e){
	cout << "Imprimiendo :";
	for(int i = 0; i < X; i++) cout << e[i] << ' ';
	cout << endl;
	for(int i = 0; i < X; i++){
		for(int j = 0; j < X; j++){
			cout << M[e[i]][j] << ' ';
		}
		cout << endl;
	}
	cout << endl;
}

queue<pair<vector<int>,int> > Q;
set<vector<int> > visto;

int main(){
	int Cases;
	ios::sync_with_stdio(false);
	cin >> Cases;
	for(int caso = 1; caso <= Cases; caso++){
		Q = queue<pair<vector<int>,int> > ();
		visto = set<vector<int> >();
		cin >> X;
		M = vector<vector<bool> >(X,vector<bool>(X,0));
		for(int i = 0; i < X; i++)
			for(int j = 0; j < X; j++){
				char a;
				cin >> a;
				M[i][j] = bool(a-'0');
			}
		int solv = 987654322;
		vector<int> inicial(X);
		for(int i = 0; i < X; i++)
			inicial[i] = i;
		Q.push(pair<vector<int>,int>(inicial, 0));
		while(!Q.empty()){
			vector<int> N = Q.front().first;
			//print(N);
			int d = Q.front().second;
			if (solucion(N)){
				solv = d;
				break;
			}
			Q.pop();
			for(int i = 0; i < X-1; i++){
				vector<int> NN = swap(N, i, i+1);
				if (!visto.count(NN)){
					Q.push(pair<vector<int>,int >(NN, d+1));
					visto.insert(NN);
				}
			}
		}
		cout << "Case #" << caso << ": " << solv << endl;
	}
	return 0;
}
