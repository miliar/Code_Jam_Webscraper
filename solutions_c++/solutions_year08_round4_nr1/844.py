#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using namespace std;

#define Rep(i, a, b) for(int i = (a); i <= (b); i++)
const int INF = 20000;
int f[10010][2][2];
int change[10010];
int gate[10010];
int min(int a, int b){
	if(a < b) return a;
	else return b;
}
int function(int m, int v, int g){
	if(f[m][v][g] != -1){
		return min(f[m][v][g], INF);
	}
	if(g == 0){
		if(gate[m] == 1 && change[m] == 0){
			f[m][0][0] = f[m][1][0] = INF;
			return INF;
		}
		if(v == 0){
			return f[m][0][0] = min((min(function(2*m, 0, 0),function(2*m, 0, 1)) + 
				min(function(2*m+1, 0, 0), function(2*m+1, 0, 1)) + gate[m]), INF);
		}
		else{
			return f[m][1][0] = min((min(min(function(2*m, 1, 0),function(2*m, 1, 1)), 
						min(function(2*m+1, 1, 0), function(2*m+1, 1, 1))) + gate[m]), INF) ;
		}
	}
	else{
		if(gate[m] == 0 && change[m] == 0){
			f[m][0][1] = f[m][1][1] = INF;
			return INF;
		}
		if(v == 1){
			return f[m][1][1] = min((min(function(2*m, 1, 0),function(2*m, 1, 1)) + 
				min(function(2*m+1, 1, 0), function(2*m+1, 1, 1)) + 1 - gate[m]), INF);
		}
		else{
			return f[m][0][1] = min((min(min(function(2*m, 0, 0),function(2*m, 0, 1)), 
						min(function(2*m+1, 0, 0), function(2*m+1, 0, 1))) + 1 - gate[m]), INF);
		}
	}
}
int main(){
	int N, t;
	int M, V, x, y;
	cin >> N;
	Rep(I, 1, N){
		cout<<"Case #"<<I<<": ";
		cin>>M>>V;
		Rep(i, 1, (M-1)/2){
			cin >> x >> y;
			f[i][0][0] = f[i][0][1] = f[i][1][0] = f[i][1][1] = -1;
			gate[i] = x;
			change[i] = y;
		}
		Rep(i, (M+1)/2, M){
			cin >> x;
			f[i][x][0] = f[i][x][1] = 0;
			f[i][1 - x][0] = f[i][1 - x][1] = INF;
		}
		t = min(function(1,V,0), function(1,V,1));
		if(t >= INF){
			cout<<"IMPOSSIBLE\n";
		}
		else
			cout<<t<<endl;
	}
	return 0;
}

