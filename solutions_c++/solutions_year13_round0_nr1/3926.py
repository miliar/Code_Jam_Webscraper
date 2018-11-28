#include <iostream>
#include <fstream>


enum values{BLANK, X, O, T, ERRORCODE};//holds value based on board

values getValue(char c)
{
	if(c=='X')
	{
		return X;
	}
	else if(c=='O')
	{
		return O;
	}
	else if(c=='.')
	{
		return BLANK;
	}
	else if(c=='T')
	{
		return T;
	}
	std::cerr<<"Invalid data\n";
	return BLANK;//ERROR HANDLING
}


values getCondition(values *board, int size)
{
	if(size!=16)
		return ERRORCODE;
	//declarations
	values diag[2];
	values rowcol[4][2];
	values out=BLANK;
	//finds each side
	for(int j=0;j<4;j++)
	{
		rowcol[j][0]=values(board[4*j]&board[4*j+1]&board[4*j+2]&board[4*j+3]);
		rowcol[j][1]=values(board[j]&board[j+4]&board[j+8]&board[12+j]);
		out=values(out|rowcol[j][0]|rowcol[j][1]);
		if(out!=BLANK)
			return out;
	}
	diag[0]=values(board[0]&board[5]&board[10]&board[15]);
	diag[1]=values(board[3]&board[6]&board[9]&board[12]);
	out=values(out|diag[0]|diag[1]);
	return out;
}

int main(int argc, char *argv[])
{
	//declare variables
	bool incomplete=true;
	std::string outText[6]={"X won","O won", "Draw", "Game has not completed", "Case #", ": "};
	values board[16];//holds board position
	values outVal;
	char charBuffer[5];
	int testCases;
	testCases=0;

	//get input file name from argument list
	if(argc!=3)
	{
		std::cout<<"start command should read, TicTacTomek inputfile outputfile\n";
		return 1;
		
	}
	
	std::ifstream inFile(argv[1],std::ios_base::in);
	std::ofstream outFile(argv[2],std::ios_base::out);

	//parse input file start
	if(!inFile)
	{
		std::cout<<"Cannot open file "<<argv[1] <<" does not exist.\n";
		inFile.close();
		outFile.close();
		return 2;//exits
	}
	inFile>>testCases;
	std::cout<<testCases<<'\n';
	for(int i=0;i<testCases;i++)
	{
		inFile.getline(charBuffer,5);

		//generates response start
		incomplete=false;
		for(int j=0;j<4;j++)
		{
			inFile.getline(charBuffer,5);
			for(int k=0;k<4;k++)
			{
				std::cout<<charBuffer[k];
				board[4*j+k]=getValue(charBuffer[k]);
				if(board[4*j+k]==BLANK)
					incomplete=true;
				if(board[4*j+k]==ERRORCODE)
				{
					inFile.close();
					outFile.close();
					return 3;
				}
			}
			std::cout<<'\n';

		}//end case read
		std::cout<<'\n';
		outVal=getCondition(board, 16);
		outFile<<"Case #"<<i+1<<": ";
		switch(outVal)
		{
		case X:
			outFile<<"X won";
			break;
		case O:
			outFile<<"O won";
			break;
		case BLANK:
			if(incomplete)
			{
				outFile<<"Game has not completed";
			}
			else
			{
				outFile<<"Draw";
			}
			break;
		default:
			std::cerr<<"Invalid value\n";
			return 4;
		}
		outFile<<'\n';
		//response generation end
	}
	//parse input end
	//close files
	inFile.close();
	outFile.close();
	//end
	return 0;


}