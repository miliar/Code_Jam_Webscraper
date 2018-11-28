#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
using namespace std;

int main(){
	int N;
	ifstream fin("A-small.in");
	ofstream fout("A-small.out");
	
	fin >> N;	
	
	for (int k = 0; k  < N; ++k) {
		//vector < pair <long long, long long> > all;
		long long res = 0;
		long long table[3][3];
		for (int i = 0; i < 3; ++i)
			for (int j = 0; j < 3; ++j)
				table[i][j] = 0;
		
		long long  n, A, B, C, D, x0, y0, M;
		fin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		long long X = x0, Y = y0;
		
		table[X % 3][Y % 3]++;		
		//all.push_back(make_pair(X, Y));
		
		for (int i = 1; i <= n-1; ++i) {
		  X = (A * X + B) % M;
		  Y = (C * Y + D) % M;
		  table[X % 3][Y % 3]++;
		  //all.push_back(make_pair(X, Y));
		}	
	
		int subb, subc, div;
		for (int a = 0; a < 9; ++a) {			
			for (int b = a; b < 9; ++b) {
				subb = 0; div = 1;				
				if (a == b) {subb = -1; div = 2; }			
				
				for (int c = b; c < 9; ++c) {
					//check if correct					
					if (((a/3) + (b/3) + (c/3)) % 3 != 0) continue;
					if (((a%3) + (b%3) + (c%3)) % 3 != 0) continue;
					
					subc = 0;
					if (a != b && b == c) {subc = -1; div = 2;}
					if (a == b && b == c) {subc = -2; div = 6;}
					long long tmp1 = table[a/3][a%3];
					long long tmp2 = (table[b/3][b%3] + subb);					
					long long tmp3 = (table[c/3][c%3] + subc);
					if (tmp2 < 0 || tmp3 < 0) continue;
				
					res += tmp1*tmp2*tmp3/div;
				}
			}
		}
		
//		long long res2 = 0;
//		//cout << all.size() << endl;
//		for (int i = 0; i < all.size(); ++i)
//			for (int j = i + 1; j < all.size(); ++j)
//				for (int t = j + 1; t < all.size(); ++t) {
//					if ((all[i].first + all[j].first + all[t].first) % 3 != 0) continue;
//					if ((all[i].second + all[j].second + all[t].second) % 3 != 0) continue;
//					//cout << all[i].first + all[j].first + all[t].first << " " << all[i].second + all[j].second + all[t].second << endl; 
//					res2++;
//				}

		fout << "Case #" << k + 1 << ": " << res << endl;
	}
	
	
	fin.close();
	fout.close();
	return 0;
}