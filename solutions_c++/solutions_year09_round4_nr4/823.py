#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

double dist(int x1, int y1, int x2, int y2){
	return sqrt(double((x2-x1)*(x2-x1))+double((y2-y1)*(y2-y1)));
}

struct planta{
	int x, y, r;
};

double solution(vector<planta> P, vector<int> V){
	if (P.size() < 3) return 0;
	if (P[V[0]].x == P[V[1]].x && P[V[0]].y == P[V[1]].y)
		return double(max(P[V[0]].r, max(P[V[1]].r, P[V[2]].r)));
	return max((dist(P[V[0]].x, P[V[0]].y, P[V[1]].x, P[V[1]].y)+double(P[V[0]].r+P[V[1]].r))/2, double(P[V[2]].r));
}

int main(){
	int Cases;
	ios::sync_with_stdio(false);
	cin >> Cases;
	for(int caso = 1; caso <= Cases; caso++){
		int N;
		double solucion = 987654321.0;
		cin >> N;
		vector<planta> P(N);
		for(int i = 0; i < N; i++)
			cin >> P[i].x >> P[i].y >> P[i].r;
		if (N < 3) solucion = 0;
		else{
			vector<int> Perm(3);
			Perm[0] = 0, Perm[1] = 1, Perm[2] = 2;
			do{
				solucion = min(solucion, solution(P, Perm));
			}while(next_permutation(Perm.begin(), Perm.end()));
		}
		cout << "Case #" << caso << ": " << solucion << endl;
	}
	return 0;
}
