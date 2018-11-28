#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int N;
	cin >> N;
	for(int i = 0; i < N; i++){
		int r,s;
		bool ok = true;
		cin >> r >> s;
		vector < vector <char> > V;
		V.resize(r);
		for(int y = 0; y < r; y++){
			V[y].resize(s);
			for(int x = 0; x < s; x++){
				cin >> V[y][x];
			}
		}
		for(int y = 0; y < r; y++){
			for(int x = 0; x < s; x++){
				if(V[y][x] == '#'){
					if( x+1 == s ) ok = false;
					if( y+1 == r ) ok = false;
					if( ok ) {
						if( V[y][x+1] != '#' ) ok = false;
						if( V[y+1][x] != '#' ) ok = false;
						if( V[y+1][x+1] != '#' ) ok = false;
					}
					if(ok){
						V[y][x] = '/';
						V[y][x+1] = 92;
						V[y+1][x] = 92;
						V[y+1][x+1] = '/';
					}
				}
			}	
		}
		cout << "Case #" << i+1 << ":" << endl;
		if(ok){
			for(int y = 0; y < r; y++){
				for(int x = 0; x < s; x++){
					//if (V[y][x] == '*') cout << '\';
					 cout << V[y][x];
				}
				cout << endl;
			}
		}
		else{
			cout << "Impossible" << endl; 
		}
	}
    //system("PAUSE");
    return 0;
}
