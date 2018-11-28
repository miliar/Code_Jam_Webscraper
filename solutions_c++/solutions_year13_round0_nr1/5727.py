#include<iostream>
#include<fstream>
#include<string>

using namespace std ; 

int main(){
	ifstream fin ("A-small-practice.in");
	ofstream fout ("A-small-practice.out");
	int  x  ;
	char u ;
	bool s = false; 
	fin>>x ; 
	for(int q=1 ; q<=x ; q++){

		s= false ; 
		char array[4][4] = {0};

		for (int i = 0 ; i < 4 ; i++) {
			for (int y = 0 ; y < 4 ; y++) {
				fin>>u;
				array[i][y]=u; 
		}
	}
		
		for(int i = 0 ; i < 4 ; i++ ){

			if((array[i][0]!='.') && (array[i][1]!='.') && (array[i][2]!='.') && (array[i][3]!='.') &&
			(array[i][0] == array[i][1] || (array[i][0] =='T') ) && 
			(array[i][1] == array[i][2]) && 
			(array[i][2] == array[i][3] || (array[i][3] =='T') ) ){

				fout<<"Case #"<<q<<":"<<" "<<array[i][1]<<" won"<<endl;
				break ; 
			}
					

			else if ((array[0][i]!='.')&& (array[1][i]!='.') && (array[2][i]!='.') && (array[3][i]!='.') && 
			(array[0][i] == array[1][i] || (array[0][i] =='T') ) && 
			(array[1][i] == array[2][i]) && 
			(array[2][i] == array[3][i] || (array[3][i] =='T') )){
				fout<<"Case #"<<q<<":"<<" "<<array[1][i]<<" won"<<endl;
				break ;
			}
			if(i>=3)
				s= true ; 
		}

		if ((array[0][0]!='.')&& (array[1][1]!='.') && (array[2][2]!='.') && (array[3][3]!='.') && 
		(array[0][0] == array[1][1] || (array[0][0] =='T') ) && 
		(array[1][1] == array[2][2]) && 
		(array[2][2] == array[3][3] || (array[3][3] =='T') )){
			fout<<"Case #"<<q<<":"<<" "<<array[1][1]<<" won"<<endl;
		}
		else if ((array[0][3]!='.')&& (array[1][2]!='.') && (array[2][1]!='.') && (array[3][0]!='.') && 
		(array[0][3] == array[1][2] || (array[0][3] =='T') ) && 
		(array[1][2] == array[2][1]) && 
		(array[2][1] == array[3][0] || (array[3][0] =='T') )){
			fout<<"Case #"<<q<<":"<<" "<<array[1][2]<<" won"<<endl;
		}
		else{
			int count = 0 ;
			for(int r = 0 ; r<4 ;r++)
				for(int f = 0 ; f<4 ; f++)
					if(array[r][f]=='.')
						count++;
			if(count  > 0 && s== true )			
				fout<<"Case #"<<q<<":"<<" Game has not completed"<<endl ; 
			else if(s == true && count == 0 )	
				fout<<"Case #"<<q<<":"<<" Draw"<<endl ; 
		}
	}
return 0 ;
}