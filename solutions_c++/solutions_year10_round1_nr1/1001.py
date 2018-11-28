#include <iostream>
#include <string>
#include <vector>

using namespace std;

enum Case {
	R, B, RIEN
};

string rotate(int dim, int nb, vector< vector<Case> > map) {
	vector< vector<int> > lines(dim, vector<int>(dim, 0)), diags(dim, vector<int>(dim, 0)),
		diags2(dim, vector<int>(dim, 0));

	bool r = false, b = false;

	for(int y=dim-1 ; y>=0 ; y--) {
		int bottom = dim-1;
		for(int x=dim-1 ; x>=0 ; x--) {
			if(map[y][x] == RIEN)
				continue;
			map[y][bottom] = map[y][x];
			bottom--;
		}
		while(bottom >= 0) {
			map[y][bottom] = RIEN;
			bottom--;
		}

		// DEBUG
		/*for(int x=0 ; x<dim ; x++) {
			cout << (map[y][x] == R ? 'R' : (map[y][x] == B ? 'B' : '.'));
		}
		cout << endl;
		*/

		int vert = 0;
		for(int x=dim-1 ; x>=0 ; x--) {
			if(map[y][x] == RIEN)
				break;

			// Check vertical
			if(x<dim-1) {
				if(map[y][x+1] == map[y][x])
					vert++;
				else
					vert = 0;
				if(vert+1 >= nb) {
					switch(map[y][x]) {
						case R:
							r = true;
							break;
						case B:
							b = true;
							break;
					}
					if(r && b)
						break;
				}
			}

			// Check horizontal
			if(y<dim-1) {
				if(map[y+1][x] == map[y][x]) {
					lines[y][x] = lines[y+1][x]+1;
					if(lines[y][x]+1 >= nb) {
						switch(map[y][x]) {
							case R:
								r = true;
								break;
							case B:
								b = true;
								break;
						}
						if(r && b)
							break;
					}
				}
			}

			// Check diagonal 1
			if(y<dim-1 && x<dim-1) {
				if(map[y+1][x+1] == map[y][x]) {
					diags[y][x] = diags[y+1][x+1]+1;
					if(diags[y][x]+1 >= nb) {
						switch(map[y][x]) {
							case R:
								r = true;
								break;
							case B:
								b = true;
								break;
						}
						if(r && b)
							break;
					}
				}
			}

			// Check diagonal 2
			if(y<dim-1 && x>0) {
				if(map[y+1][x-1] == map[y][x]) {
					diags2[y][x] = diags2[y+1][x-1]+1;
					if(diags2[y][x]+1 >= nb) {
						switch(map[y][x]) {
							case R:
								r = true;
								break;
							case B:
								b = true;
								break;
						}
						if(r && b)
							break;
					}
				}
			}
		}
		if(r && b)
			break;
	}

	if(r && b)
		return "Both";
	else if(r)
		return "Red";
	else if(b)
		return "Blue";
	else
		return "Neither";
}

int main() {
	int cases;
	cin >> cases ;

	for(int i=1 ; i<= cases ; i++) {
		int n, k;
		cin >> n >> k;
		cin.ignore();

		vector< vector<Case> > map(n, vector<Case>(n, RIEN));
		char* tmp = new char[n+1];
		for(int l=0 ; l<n ; l++) {
			cin.getline(tmp, n+1);
			for(int c=0 ; c<n ; c++) {
				map[l][c] = (tmp[c] == '.' ? RIEN : (tmp[c] == 'R' ? R : B));
			}
		}

		string res = rotate(n, k, map);
		cout << "Case #" << i << ": " << res << endl;
	}
}
