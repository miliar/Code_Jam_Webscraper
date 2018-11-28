#include<iostream>
#include<fstream>
#include<cstring>

using namespace std;

char t[4][4],nex[10];
bool flag=false;

int checkresult(int empspace){
	//CHECK FOR EMPSPACE VALUE BEFORE A DRAW
	int countx=0,counto=0;
	
	//Diagnols
	for(int i=0;i<4;i++){
		if(t[i][i]=='X')
			countx++;
		else if(t[i][i]=='O')
			counto++;
		else if(t[i][i]=='T')
			countx++,counto++;
		else{
			countx=0;
			counto=0;
		}

	}
	if(countx==4)
		return 1;
	else if(counto==4)
		return 2;
	else{
		countx=0;
		counto=0;
	}


	//Diagnol2
	for(int i=0;i<4;i++){
		if(t[i][3-i]=='X')
			countx++;
		else if(t[i][3-i]=='O')
			counto++;
		else if(t[i][3-i]=='T'){
			countx++;
			counto++;
		}
		else{
			countx=0;		//even one empty space makes life hard :P
			counto=0;
		}

			//count=0;
	}

	if(countx==4)
		return 1;
	else if(counto==4)
		return 2;
	else{
		countx=0;
		counto=0;
	}


	//ROWS
	for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				//DO SOMETHING
				if(t[i][j]=='X')
					countx++;
				else if(t[i][j]=='O')
					counto++;
				else if(t[i][j]=='T'){
					countx++;
					counto++;
				}
				else{
					countx=0;		//even one empty space makes life hard :P
					counto=0;
				}
			}
			//Row iteration complete... check now
			if(countx==4)
				return 1;
			else if(counto==4)
				return 2;
			else{
				countx=0;
				counto=0;
			}
		}
	//COLUMNS
	//ROWS
	for(int j=0;j<4;j++){
			for(int i=0;i<4;i++){
				//DO SOMETHING
				if(t[i][j]=='X')
					countx++;
				else if(t[i][j]=='O')
					counto++;
				else if(t[i][j]=='T'){
					countx++;
					counto++;
				}
				else{
					countx=0;		//even one empty space makes life hard :P
					counto=0;
				}
			}
			//Column iteration complete... check now
			if(countx==4)
				return 1;
			else if(counto==4)
				return 2;
			else{
				countx=0;
				counto=0;
			}
		}
	//IF code reaches here, nobody is a winner... game is either draw or NOT complete
	if(empspace==0)
		return 3;	//DRAW
	else
		return 4;	//NOT COMPLETE

}

int main(){

	ifstream in("inp.in");		//Change the name!!!
	ofstream out("A-small-attempt.out");	//doesn't matter
	int test,sno;
	
	in>>test;
	in.getline(nex,10);      //GO TO THE NEXT LINE
	for(int z=0;z<test;z++){
		int emp=0;
		//Main code is here...

		for(int i=0;i<4;i++){
					//INPUT the values
			for(int j=0;j<4;j++){
				in>>t[i][j];
				//count empty spaces before hand
				if(t[i][j]=='.')
					emp++;
			}
			in.getline(nex,10);		//bring the file cursor to next line //This may be buggy
		}

		//Check for result
		
		sno=checkresult(emp);

		//put a switch case here for the result
		switch(sno){
		case 1: out<<"Case #";
				out<<z+1;
				out<<": X won";
				out<<"\n";
				break;
		case 2: out<<"Case #";
				out<<z+1;
				out<<": O won";
				out<<"\n";
				break;
		case 3: out<<"Case #";
				out<<z+1;
				out<<": Draw";
				out<<"\n";
				break;
		case 4: out<<"Case #";
				out<<z+1;
				out<<": Game has not completed";
				out<<"\n";
				break;
				
		}
		in.getline(nex,10);			// THERE is an extra line at the end of each test case

	}

	in.close();
	out.close();
	return 0;
}