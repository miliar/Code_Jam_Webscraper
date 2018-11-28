#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>


using namespace std;


int main(int argc, char* argv[])
{
	ifstream fin ("A-large.in");
	//ifstream fin ("test");
    ofstream fout ("output.out");

    char world[4][4];

	int cases;
	fin >> cases;

	cout<<cases;
	
	string buffer;
	//(fin,buffer); //ignore first line

	for(int i=1;i<=cases;i++){
		fout << "Case #"<<i<<": ";
		for(int x=0;x<4;x++)
			for(int y=0;y<4;y++)
				fin>>world[x][y];

		// for(int x=0;x<4;x++){
		//  	for(int y=0;y<4;y++)
		//  		cout<<world[x][y];
		//  	cout<<endl;
		// }
		
		bool xWon=false,oWon=false;
		int xwonR=0,owonR=0;
		int xwonC=0,owonC=0;
		int xdiag1=0, xdiag2=0;
		int odiag1=0, odiag2=0;
		int dots=0;
		for(int x=0;x<4;x++){
			xwonR=0; owonR=0;
			xwonC=0; owonC=0;



			//diag
			if(world[x][x]=='X' || world[x][x]=='T')
				xdiag1++;
			if(world[x][x]=='O' || world[x][x]=='T')
				odiag1++;

			if(world[x][3-x]=='X' || world[x][3-x]=='T')
				xdiag2++;
			if(world[x][3-x]=='O' || world[x][3-x]=='T')
				odiag2++;

			for(int y=0;y<4;y++){
				//check rows
				if(world[x][y]=='X' || world[x][y]=='T')
					xwonR++;
				if(world[x][y]=='O' || world[x][y]=='T')
					owonR++;

				//check cols
				if(world[y][x]=='X' || world[y][x]=='T')
					xwonC++;
				if(world[y][x]=='O' || world[y][x]=='T')
					owonC++;

				if(world[x][y]=='.')
					dots++;

			}
			if(xwonC==4 || xwonR==4 || xdiag1==4 || xdiag2==4){
				xWon=true;
			}
			if(owonC==4 || owonR==4 || odiag1==4 || odiag2==4){
				oWon=true;
			}
		}

		if(!xWon && !oWon)
			if(dots==0)
				fout<<"Draw";
			else
				fout<<"Game has not completed";
		else if (xWon)
			fout<<"X won";
		else if(oWon)
			fout<<"O won";
		else 
			fout<<"Draw";

		fout<<endl;
	}

	fin.close();
	fout.close();


	return 0;
}

