#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("fin.txt");
	fout.open("fout.txt");
	int T;
	char board[4][4];
	fin >> T;
	for(int where=0;where<T;where++){
		for(int a=0;a<4;a++){
		   for(int b=0;b<4;b++){
			 fin >> board[a][b];
	       }
		}
		char current;
		char winner=0;
		
		//Columns
		for(int a=0;(a<4)&&(winner==0);a++){
			current=board[0][a];
			if((current!='X')&&(current!='O')) continue;
		   	for(int b=1;b<4;b++){
			   if((board[b][a]!=current)&&(board[b][a]!='T')) break;
			   else if(b==3) winner=current;
	        }
		}
		if(winner!=0){
		   fout << "Case #" << where+1 << ": " << winner << " won\n";
		   continue;
	    }
		
		
		//Rows
		for(int a=0;(a<4)&&(winner==0);a++){
			current=board[a][0];
			if((current!='X')&&(current!='O')) continue;
		   	for(int b=1;b<4;b++){
			   if((board[a][b]!=current)&&(board[a][b]!='T')) break;
			   else if(b==3) winner=current;
	        }
		}
		
		if(winner!=0){
		   fout << "Case #" << where+1 << ": " << winner << " won\n";
		   continue;
	    }
	    
	    
	    //First diagonal
	    current=board[0][0];
		if((current=='X')||(current=='O')){
		   if(((board[1][1]==current)||(board[1][1]=='T'))&&((board[2][2]==current)||(board[2][2]=='T'))&&((board[3][3]==current)||(board[3][3]=='T'))){
	         fout << "Case #" << where+1 << ": " << current << " won\n";
		     continue;
	       }
	    }
	    
	    else if((current=='T')&&((board[1][1]=='X')||(board[1][1]=='O'))){
	       current=board[1][1];
		   if(((board[2][2]==current)||(board[2][2]=='T'))&&((board[3][3]==current)||(board[3][3]=='T'))){
	         fout << "Case #" << where+1 << ": " << current << " won\n";
		     continue;
	       }
	    }
	    
	    //Second diagonal
	    current=board[0][3];
		if((current=='X')||(current=='O')){
		   if(((board[1][2]==current)||(board[1][2]=='T'))&&((board[2][1]==current)||(board[2][1]=='T'))&&((board[3][0]==current)||(board[3][0]=='T'))){
	         fout << "Case #" << where+1 << ": " << current << " won\n";
		     continue;	
	       }
	    }
	    
		else if((current=='T')&&((board[1][2]=='X')||(board[1][2]=='O'))){
		   if(((board[2][1]==current)||(board[2][1]=='T'))&&((board[3][0]==current)||(board[3][0]=='T'))){
	         fout << "Case #" << where+1 << ": " << current << " won\n";
		     continue;	
	       }
	    }		
		
		bool draw=true;
		for(int a=0;(a<4)&&(draw==true);a++){
		   for(int b=0;b<4;b++){
			 if(board[a][b]=='.'){
			   draw=false;
			   break;
			 }
	       }
		}
		
		
		
		if(draw==true){
		   fout << "Case #" << where+1 << ": Draw\n";
		   continue;
	    }
		else if(draw==false){
		   fout << "Case #" << where+1 << ": Game has not completed\n";
		   continue;
	    }
	}	
}
