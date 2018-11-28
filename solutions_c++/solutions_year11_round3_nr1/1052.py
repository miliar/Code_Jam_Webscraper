#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip.h>
#include <string>
using namespace std;

int main(int argc, char *argv[]){
		ifstream ins;
		ins.open(argv[1]);
		int Ncase;
		ins>>Ncase;
		int the_case = 0;
		while (the_case++ < Ncase){
				vector<vector<char> > matrix;
				int row, col;
				ins>>row>>col;
				for (int i=0; i<row; ++i){
						vector<char> line;
						for (int j=0; j<col; j++){
								char temp;
								ins>>temp;
								line.push_back(temp);
						}
						matrix.push_back(line);
				}
				bool possible = true;
				for (int i=0; i<row; ++i){
						for (int j=0; j<col; j++){
								if (matrix[i][j]=='#'){//find a #, try replace to /
										if (i==row-1 || j==col-1){
												possible =  false;
												break;
										}
										if (matrix[i+1][j]=='#' && matrix[i][j+1]=='#' && matrix[i+1][j+1]=='#'){
												matrix[i][j]='/';
												matrix[i+1][j]='\\';
												matrix[i][j+1]='\\';
												matrix[i+1][j+1]='/';
										} else {
												possible = false;
												break;
										}
								} else continue;
						}
						if (possible == false){
								break;
						}
				}
				cout<<"Case #"<<the_case<<":"<<endl;
				if (possible==false){
						cout<<"Impossible"<<endl;
				} else {
						for (int i=0; i<row; ++i){
								for (int j=0; j<col; j++){
										cout<<matrix[i][j];
								}
								cout<<endl;
						}
				}
		}
		ins.close();
		return 0;
}

