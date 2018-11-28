#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin ("C-small-attempt0.in");
	
	int T, k, N, g[N], R;
	fin >> T;
	for(int i = 0; i < T; i++){
		fin >> R >> k >> N;
		for(int j = 0; j < N; j ++){
			fin >> g[j];
		}
		
		int money = 0;
		int total = 0;
		for(int l = 0; l < N; l++){
			total = total + g[l];
		}
		
		if(total < k){
			money = R * total;
		}else{
			int current = 0;
			for ( int l = 0; l < R; l++){
				total = 0;
				while ( total + g[current]<= k){
					total = total + g[current];
					current = (current + 1) % N;
				}
				money = money + total;	
			}
		}
		
		cout << "Case #" << i + 1 <<": " << money << endl;
	}
	
	fin.close();
	system("pause");
	return 0;
}
