#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;
#define ST first
#define ND second
#define LD (long double)
int C, N, K, B, T;
pair<int, long double > chicks[100];
int main(){
	cin >> C;
	for(int z=1; z<=C; z++){
		cin >> N >> K >> B >> T;
		for(int i=0; i<N; i++)
			cin >> chicks[i].ST;
		for(int i=0; i<N; i++){
			int tmpl;
			cin >> tmpl;
			chicks[i].ND = LD(B-chicks[i].ST)/tmpl;
		}
		int result = 0;
		for(int i=N-1; i>=0; i--){
			if(chicks[i].ND>T) result += K;
			else K--; 
			if(K==0) break;
		}
		if(K>0) cout << "Case #" <<z<<": IMPOSSIBLE" <<endl;
		else cout << "Case #" << z<<": " <<result << endl;
	}



	return 0;
}


