#include <fstream>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
	ifstream infile("A-small-attempt0.in");
	ofstream outfile("output.out");
	int T;
	string input;

	infile>>T;
	getline(infile,input);
	
	for( int t=1;t<=T;++t ){
		vector<string> board;
		bool busy = false;
		bool bigbroken = false;
		
		if( t != 1 ){
			getline(infile,input);//blank line
		}
		
		for(int i=0;i<4;++i ){
			getline(infile,input);
			board.push_back(input);
		}
		
		//checking rows
		for( int r = 0 ; r < 4 ; ++r ){
			char search;
			bool broken = false;
			int aantal=0;
			
			for( int c = 0 ;  c < 4 ; ++c ){
				if( board[r][c] == '.' ){
					busy = true;
					broken = true;
					break;
				}
				if( board[r][c] == 'T' ) continue;
				
				search = board[r][c];
				break;
			}
			
			if( broken ) continue;
			
			for( int c = 0 ; c < 4 ; ++c) {
				if( board[r][c] == search || board[r][c] == 'T'){
					aantal++;
					continue;
				}
				
				if( board[r][c] == '.' ){
					busy = true;
					break;
				}
				
				break;
			}
			
			//check if this row has won
			if( aantal == 4 ){
				outfile<<"Case #"<<t<<": "<<search<<" won"<<endl;
				bigbroken = true;
				break;
			}
		}
		
		//if a row has won, continue
		if( bigbroken ) continue;
		
		//checking columns
		for( int c = 0 ; c  < 4 ; ++c ){	
			char search;
			bool broken = false;
			int aantal=0;
			
			for( int r = 0 ;  r < 4 ; ++r ){
				if( board[r][c] == '.' ){
					busy=true;
					broken=true;
					break;
				}
				if( board[r][c] == 'T' ) continue;
				
				search = board[r][c];
				break;
			}
			
			if( broken ) continue;
			
			for( int r = 0 ; r < 4 ; ++r ){
				if( board[r][c] == search || board[r][c] == 'T' ){
					aantal++;
					continue;
				}
				
				if( board[r][c] == '.' ){
					busy=true;
					break;
				}
				break;
			}
			
			if( aantal == 4 ){
				outfile<<"Case #"<<t<<": "<<search<<" won"<<endl;
				bigbroken=true;
				break;
			}
		}
		
		//diagonal from upleft to downright
		int aantal=0;
		char search = 'A';
		for( int d = 0 ;  d < 4 ; ++d ){
			if( board[d][d] == 'T' || board[d][d] == search){
				aantal++;
				continue;
			}
			if( board[d][d] == '.' ){
				busy=true;
				break;
			}
			
			if( search == 'A' ){
				search = board[d][d];
				aantal++;
				continue;
			} 
			if( search != board[d][d] ){
				break;
			}
		}
		
		if( aantal == 4 ){
			outfile<<"Case #"<<t<<": "<<search<<" won"<<endl;
			bigbroken=true;
		}
		
		if( bigbroken ) continue;
		
		//diagonal from upright to downleft
		aantal=0;
		search = 'A';
		for( int d = 0 ;  d < 4 ; ++d ){
			if( board[3-d][d] == 'T' || board[3-d][d] == search ){
				aantal++;
				continue;
			}
			if( board[3-d][d] == '.' ){
				busy=true;
				break;
			}
			
			if( search == 'A' ){
				search = board[3-d][d];
				aantal++;
				continue;
			} 
			if( search != board[3-d][d] ){
				break;
			}
		}
		
		if( aantal == 4 ){
			outfile<<"Case #"<<t<<": "<<search<<" won"<<endl;
			bigbroken=true;
		}
		
		if( bigbroken ) continue;
		
		if( busy ){
			outfile<<"Case #"<<t<<": Game has not completed"<<endl;
		} else {
			outfile<<"Case #"<<t<<": Draw"<<endl;
		}
	}
	
	return 0;
}