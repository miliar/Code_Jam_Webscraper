#include <fstream>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
	ofstream out("ttt.out");
	ifstream in("ttt.in");
	
	int t;
	in >> t;
	
	vector<string> grid(4);
	
	int i = -1;
	
	loop:
	i++;
	if(i < t){
		for(int j = 0; j < 4; j++){
			in >> grid[j];
		}
		
		for(int j = 0; j < 4; j++){
			if((grid[j][0]=='X' || grid[j][0]=='T')&&
			   (grid[j][1]=='X' || grid[j][1]=='T')&&
			   (grid[j][2]=='X' || grid[j][2]=='T')&&
			   (grid[j][3]=='X' || grid[j][3]=='T')){
				out << "Case #" << i+1 << ": X won" << endl;
				goto loop;
			}
		}
		
		for(int j = 0; j < 4; j++){
			if((grid[j][0]=='O' || grid[j][0]=='T')&&
			   (grid[j][1]=='O' || grid[j][1]=='T')&&
			   (grid[j][2]=='O' || grid[j][2]=='T')&&
			   (grid[j][3]=='O' || grid[j][3]=='T')){
				out << "Case #" << i+1 << ": O won" << endl;
				goto loop;
			}
		}
		
		for(int j = 0; j < 4; j++){
			if((grid[0][j]=='X' || grid[0][j]=='T')&&
			   (grid[1][j]=='X' || grid[1][j]=='T')&&
			   (grid[2][j]=='X' || grid[2][j]=='T')&&
			   (grid[3][j]=='X' || grid[3][j]=='T')){
				out << "Case #" << i+1 << ": X won" << endl;
				goto loop;
			}
		}
		
		for(int j = 0; j < 4; j++){
			if((grid[0][j]=='O' || grid[0][j]=='T')&&
			   (grid[1][j]=='O' || grid[1][j]=='T')&&
			   (grid[2][j]=='O' || grid[2][j]=='T')&&
			   (grid[3][j]=='O' || grid[3][j]=='T')){
				out << "Case #" << i+1 << ": O won" << endl;
				goto loop;
			}
		}
		
		if((grid[0][0]=='X' || grid[0][0]=='T')&&
		   (grid[1][1]=='X' || grid[1][1]=='T')&&
		   (grid[2][2]=='X' || grid[2][2]=='T')&&
		   (grid[3][3]=='X' || grid[3][3]=='T')){
			out << "Case #" << i+1 << ": X won" << endl;
			goto loop;
		}
		
		if((grid[0][0]=='O' || grid[0][0]=='T')&&
		   (grid[1][1]=='O' || grid[1][1]=='T')&&
		   (grid[2][2]=='O' || grid[2][2]=='T')&&
		   (grid[3][3]=='O' || grid[3][3]=='T')){
			out << "Case #" << i+1 << ": O won" << endl;
			goto loop;	   
		}
		
		if((grid[0][3]=='X' || grid[0][3]=='T')&&
		   (grid[1][2]=='X' || grid[1][2]=='T')&&
		   (grid[2][1]=='X' || grid[2][1]=='T')&&
		   (grid[3][0]=='X' || grid[3][0]=='T')){
			out << "Case #" << i+1 << ": X won" << endl;
			goto loop;
		}
		
		if((grid[0][3]=='O' || grid[0][3]=='T')&&
		   (grid[1][2]=='O' || grid[1][2]=='T')&&
		   (grid[2][1]=='O' || grid[2][1]=='T')&&
		   (grid[3][0]=='O' || grid[3][0]=='T')){
			out << "Case #" << i+1 << ": O won" << endl;
			goto loop;
		}
		
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				//out << grid[j][k];
				if(grid[j][k]=='.'){
				out << "Case #" << i+1 << ": Game has not completed" << endl;
					goto loop;
				}
			}
			//out << endl;
		}
		
		out << "Case #" << i+1 << ": Draw" << endl;
		goto loop;
	}
	
	return 0;
}

