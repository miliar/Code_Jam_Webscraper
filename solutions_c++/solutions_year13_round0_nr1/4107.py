#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <fstream>

using namespace std;

int main() {
	int T;
	int C=1;
	ifstream file("in.txt");
	ofstream out("out.txt");
	
	file >> T;
	while(T-- > 0) {
    	int n=4;
    	char mat[n][n];
    	char c;
    	
    	for(int i=0;i<n;i++) {
    		for(int j=0;j<n;j++) {
    			file >> c;
    			mat[i][j] = c;
    			
    		}
    	}
    	
    	// checa se uma linha ganhou
    	bool xwin=false, owin=false, draw=false;
    	bool respx = false, respo = false;
    	
    	for(int i=0;i<n;i++) {
    		owin=true;
    		xwin=true;
    		for(int j=0;j<n;j++) {
    			if(mat[i][j] == '.' || mat[i][j] == 'X') owin=false;
    			if(mat[i][j] == '.' || mat[i][j] == 'O') xwin=false;
    		}
    		if(owin==true) { respo = true; break; }
    		if(xwin==true) { respx = true; break; }
    	}
    	
    	// coluna ganhou
		if(!respo && !respx)
    	for(int j=0;j<n;j++) {
    		owin=true;
    		xwin=true;
    		for(int i=0;i<n;i++) {
    			if(mat[i][j] == '.' || mat[i][j] == 'X') owin=false;
    			if(mat[i][j] == '.' || mat[i][j] == 'O') xwin=false;
    		}
    		if(owin==true) { respo = true; break; }
    		if(xwin==true) { respx = true; break; }
    	}
    	
    	// diagonais
		if(!respo && !respx) {
			owin=true;
			xwin=true;
			for(int i=0;i<n;i++) {
				if(mat[i][i] == '.' || mat[i][i] == 'X') owin=false;
				if(mat[i][i] == '.' || mat[i][i] == 'O') xwin=false;
			}
			if(owin==true) respo = true;
			if(xwin==true) respx = true;
		}
		
		if(!respo && !respx) {
			owin=true;
			xwin=true;
			for(int i=0;i<n;i++) {
				if(mat[i][n-1-i] == '.' || mat[i][n-1-i] == 'X') owin=false;
				if(mat[i][n-1-i] == '.' || mat[i][n-1-i] == 'O') xwin=false;
			}		
			if(owin==true) respo = true;
			if(xwin==true) respx = true;
		}
    	
    	//draw
		if(!respo && !respx) {
			draw=true;
			for(int j=0;j<n;j++) {
				for(int i=0;i<n;i++) {
					if(mat[i][j] == '.') { draw=false; break; }
				}
			}
    	}

    	if(respx) out << "Case #" << C++ << ": X won"<<endl;
    	else if(respo) out << "Case #" << C++ << ": O won"<<endl;
    	else if(draw) out << "Case #" << C++ << ": Draw"<<endl;
    	else  out << "Case #" << C++ << ": Game has not completed"<<endl;
    		
	}
	return 0;
}

