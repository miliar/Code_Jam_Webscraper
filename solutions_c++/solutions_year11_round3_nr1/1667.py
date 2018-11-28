#include <iostream>
#include <fstream>

using namespace std;

fstream in("in.txt", fstream::in);
fstream out("out.txt", fstream::out);

void SolveCase(int t){
	int R, C; in >> R >> C;
	bool possible = true;
	char **pic = new char* [R];
	for(int row = 0; row < R; row++){
		pic[row] = new char [C + 1];
		in >> pic[row];
	}
	for(int row = 0; row < R - 1; row++){
		for(int col = 0; col < C - 1; col++){
			if((pic[row][col] == '#') && (pic[row][col+1] == '#')
				&& (pic[row+1][col] == '#') && (pic[row+1][col+1] == '#')){
					pic[row][col]			= '/';
					pic[row][col+1]		= '\\';
					pic[row+1][col]		= '\\';
					pic[row+1][col+1] = '/';
			}
			if(pic[row][col] == '#'){
				possible = false;
				col = C;
			}
		}
		if(pic[row][C - 1] == '#')
			possible = false;
		if(!possible)
			row = R;
	}
	if(possible){
		for(int col = 0; col < C; col++){
			if(pic[R - 1][col] == '#'){
				possible = false;
				col = C;
			}
		}
	}

	out << "Case #" << t << ":" << endl;

	if(!possible){
		out << "Impossible" << endl;
	}
	else{
		for(int row = 0; row < R; row++){
			out << pic[row] << endl;
		}
	}

	for(int row = 0; row < R; row++){
		delete[] pic[row];
	}
	delete[] pic;
}

int main(){
	int T; in >> T;
	for(int t = 0; t < T; t++)
		SolveCase(t+1);
	return 0;
}
