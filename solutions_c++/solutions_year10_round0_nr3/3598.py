#include <iostream>
#include <fstream>
using namespace std;


int main(){
	ifstream Filein;
	ofstream Fileout;
	Filein.open("testq.in");
	Fileout.open("output.txt");
	int T;
	unsigned __int64 j;
	unsigned __int64 R;
	unsigned __int64 k;
	int N;
	unsigned __int64 g;
	unsigned __int64 totalppl = 0;
	unsigned __int64 riders = 0;
	unsigned __int64 money = 0;
	Filein >> T;
	for (int i = 0; i < T; i++){
		Filein >> R >> k >> N;
		unsigned __int64 * arr = new unsigned __int64[N + 1];
		arr[N] = 0;
		unsigned __int64 * point = arr;
		for (j = 0; j < N; j++){
			Filein >> g;
			arr[j] = g;
			totalppl += g;
		}


		for (j = 0; j < R; j++){
			riders = 0;
			while (riders < k && riders < totalppl){
				g = *point;
				if (g == 0){
					point = arr;
					g = *point;
				}
				if (g + riders <= k && g + riders <= totalppl){
					riders += g;
					point++;
				}
				else {
					break;
				}
			}
			money += riders;
		}
		Fileout << "Case #" << (i+1) << ": " << money << endl;
		money = 0;
		riders = 0;
		totalppl = 0;
	}
	return 0;
}