#include<iostream>
#include<fstream>
#include<string>
#include<stdlib.h>

#define fill(a,n) memset(a,n,sizeof(n));

#define For(i, start, stop) for(i = start; i < stop; i++)
#define ForN(i, n) for( i = 0; i < n; i++)

using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("out.txt");

int main(){
	
	int i,j,k,l,Case, x,y;
	char start;

	string junk;
	string board[4];
	
	fin>>Case;
	getline(fin, junk);
	ForN( i, Case){

		ForN(j, 4){
			getline(fin, board[j]);
		}

		getline(fin, junk);
		bool finished = true;
		bool xWon = false;
		bool oWon = false;

		for( j = 0; j < 4; j++){
			ForN(k, (j >= 2 ? 1 : 4)){
				x = (j == 3 ? 3 : 0);
				y = 0;
				if( j == 0){
					y = k;
				}else if(j == 1){
					x = k;
				}

				if( board[y][x] == '.'){
					finished = false;
					continue;
				}else{
					start = board[y][x];
				}

				ForN(l, 4){
					if(board[y][x] == '.'){
						finished = false;
					}
					if( start == 'T'){
						start = board[y][x];
					}else if( board[y][x] != 'T' && board[y][x] != start){
						break;
					}
					x += (j == 0 || j == 2 ? 1: 0);
					if( j == 3){
						x--;
					}
					y += (j == 1 || j >= 2 ? 1 : 0);
				}

				if( l == 4){
					if( start == 'O')
						oWon = true;
					else if(start == 'X')
						xWon = true;
				}
			}

		}
		if( oWon){
			fout<<"Case #"<<(i + 1)<<": "<<"O won"<<"\n";					
		}else if(xWon){
			fout<<"Case #"<<(i + 1)<<": "<<"X won"<<"\n";							
		}else if(!finished){
			fout<<"Case #"<<(i + 1)<<": "<<"Game has not completed"<<"\n";
		}else if( !xWon && !oWon){
			fout<<"Case #"<<(i + 1)<<": "<<"Draw"<<"\n";		
		}

	}

}