#include <iostream>
#include <string>
using namespace std;

    struct linea {
	int x;
	int o;
    };

    int punto;
    linea h[3];
    linea v[3];
    linea d[3];
  
    void Eval (int i, int j, char pos) {
	if (pos == '.') {
	    punto = 1;
	    
	}
	
	if (pos == 'T') {
	    h[i].x++;
	    v[j].x++;
	    h[i].o++;
	    v[j].o++;
	    if (i == j) {
		d[0].x++;
		d[0].o++;
		
	    }
	    if (i + j == 3) {
		d[1].o++;
		d[1].x++;
	    }
	}

	if (pos == 'X') {
	    h[i].x++;
	    v[j].x++;
	    if (i == j) {
		d[0].x++;
	    }
	    if ((i + j) == 3) {
		d[1].x++;
	    }
	}

	if (pos == 'O') {
	    h[i].o++;
	    v[j].o++;
	    if (i == j) {
		d[0].o++;
	    }
	    if ((i + j) == 3) {
		d[1].o++;
	    }
	}
    }

    int main () {
	
	int T, result;
	int i,j,k = 0;
	string line;
	string caso;
	cin >> T;
	while (k < T) {
	    for (int z=0; z<4; z++) {
		h[z].x=0;
		v[z].x=0;
		d[z].x=0;
		h[z].o=0;
		v[z].o=0;
		d[z].o=0;
	    }
	    result = 0;
	    i = 0;
	    punto = 0;
	    while (i<4) {
		cin >> line;
		j = 0;
		while (j<4) {
		    Eval(i,j,line[j]);
		    if (j == 3) {
			if (h[i].o > 3) {
			    result = 1;
			}
			if (h[i].x > 3) {
			    result = 2;
			}
		    }
		    if (i == 3) {
			if (v[j].o > 3) {
			    result = 1;
			}
			if (v[j].x > 3) {
			    result = 2;
			}
			if (i == j) {
			    if (d[0].o > 3) {
				result = 1;
			    }
			    if (d[0].x > 3) {
				result = 2;
			    }
			}
			if (j == 0) {
			    if (d[1].o > 3) {
				result = 1;
			    }
			    if (d[1].x > 3) {
				result = 2;
			    }
			}
		    }
		    j++;
		}
		i++;
	    }
	    
	    if (result == 0) {
		if (punto == 0) {
		    caso = "Draw";
		} else {
		    caso = "Game has not completed";
		}
	    }
	    if (result == 1) {
		caso = "O won";
	    }
	    if (result == 2) {
		caso = "X won";
	    }

	    cout << "Case #" << k+1 << ": ";
	    cout << caso << "\n";
	    k++;
	}
    }









