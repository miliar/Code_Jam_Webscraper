/*
	Author : Subhasis Dutta
*/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;



int main()
{
	ofstream fout ("tic-tac-toe-tomek.out");
	ifstream fin ("tic-tac-toe-tomek.in");
	int T;
	fin>> T;	
	for(int i=0;i<T;i++){		
		char input;
		int tr=-10;
		int tc=-20;
		int rows[4]={0,0,0,0},columns[4]={0,0,0,0},digonal[2]={0,0};
		bool isEmpty=false;
		for(int r=0;r<4;r++){
			for(int c=0;c<4;c++){
				fin>>input;
				if(input=='O'){
					rows[r]+=-4;
					columns[c]+=-4;
					if(r==c)digonal[0]+=-4;
					else if(r==3-c)digonal[1]+=-4;
				}
				else if(input=='X'){
					rows[r]+=4;
					columns[c]+=4;
					if(r==c)digonal[0]+=+4;
					else if(r==3-c)digonal[1]+=+4;
				}
				else if(input=='T'){
					tr=r;
					tc=c;
				} 
				else{
					isEmpty=true;
				}
			}
		}
		fout<<"Case #"<<i+1<<": ";
		int all[10]={rows[0],rows[1],rows[2],rows[3],
					 columns[0],columns[1],columns[3],columns[3],
					 digonal[0],digonal[1]};		
		//Check rows,cols,digonal
		bool isWon=false;
		for(int j=0;j<10;j++){
			//fout<<all[j]<<" ";
			if(all[j]==16){
				fout<<"X won";
				//fout<<all[j]<<" ";
				isWon=true;
				break;
			}
			else if(all[j]==-16){
				fout<<"O won";
				isWon=true;
				break;
			}
			if(all[j]==12){
				if((j<4 && tr==j)||(j>3 && j<8 && tc==j-4)||(j==8 && tr==tc)||(j==9 && tr==3-tc)){					
					fout<<"X won";
					isWon=true;
					break;
				}
			}
			if(all[j]==-12){
				if((j<4 && tr==j)||(j>3 && j<8 && tc==j-4)||(j==8 && tr==tc)||(j==9 && tr==3-tc)){
					fout<<"O won";
					isWon=true;
					break;
				}
			}
		}	
		if(isWon==false){
			if(isEmpty==false){
				fout<<"Draw";
			}
			else{
				fout<<"Game has not completed";
			}
		}	
		fout<<endl;
	}
	fout<<endl;
	return 0;
}
