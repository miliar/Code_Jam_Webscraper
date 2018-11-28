#include <iostream>
#include <list>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>

#define ASCII_SPACE 32
#define ASCII_NEWLINE 10


using namespace std;




#define PRINT_TOKEN(token)\
	do{\
		cout<<#token<<" is "<<token<<endl; \
	}while(0)


#define READ(arg)\
	do{\
		long long arg;\
		cin>>arg;\
	}while(0)

//#define PRINT_ARR()
typedef long long ll;

#define X_WIN 1
#define O_WIN 2
#define DRAW 3


int countEmptyCell(char b[4][4])
{
	
	int count_dot = 0;
	for(int a=0;a<4;a++){
		for(int r=0;r<4;r++){
			if(b[a][r] == '.'){
				count_dot++;
			}
		}
	}

	return count_dot;
}

int getWinWithCount(int cX, int cO, int cT)
{
	if( cX + cT == 4)
		return X_WIN;
	else if(cO +cT == 4)
		return O_WIN;
	else 
		return -1;
}
int getShortWithCount(char symbol,int cX, int cO, int cT, int cDOT)
{
	if( symbol == 'X' && cX + cT + cDOT== 4)
		return cDOT;
	else if( symbol == 'O' && cO +cT +cDOT == 4)
		return cDOT;
	else 
		return -1;
}


int checkRowWin(char b[4][4], int* shortest_X, int* shortest_O)
{
	
	for(int r=0;r<4;r++){
		int count_X=0;
		int count_O=0;
		int count_T=0;
		int count_DOT=0;
		for(int col=0;col<4;col++){
			if(b[r][col] == 'X')
				count_X++;
			else if(b[r][col] == 'O')
				count_O++;
			else if(b[r][col] == 'T')
				count_T++;
			else if(b[r][col] == '.')
				count_DOT++;
			else
				printf("Error: unrecognized symbo(%c)l!\n",b[r][col]);
		}
		//cout<<"X:"<<count_X<<",O:"<<count_O<<",T:"<<count_T<<",.:"<<count_DOT<<endl;
			int result=getWinWithCount(count_X, count_O, count_T);
			if(result != -1)
				return result;
			int temp_shortest_X = getShortWithCount('X', count_X, count_O, count_T, count_DOT);
			int temp_shortest_O = getShortWithCount('O', count_X, count_O, count_T, count_DOT);
			if( temp_shortest_X != -1 && (*shortest_X == -1 ||temp_shortest_X < *shortest_X)){
				*shortest_X = temp_shortest_X;
			}
			if( temp_shortest_O != -1 && (*shortest_O == -1 ||temp_shortest_O < *shortest_O)){
				*shortest_O = temp_shortest_O;
			}
		
	}

	return -1;
}

int checkColWin(char b[4][4],int* shortest_X, int* shortest_O)
{
	for(int col=0;col<4;col++){
		int count_X=0;
		int count_O=0;
		int count_T=0;
		int count_DOT=0;
		for(int r=0;r<4;r++){
			if(b[r][col] == 'X')
				count_X++;
			else if(b[r][col] == 'O')
				count_O++;
			else if(b[r][col] == 'T')
				count_T++;
			else if(b[r][col] == '.')
				count_DOT++;
			else
				printf("Error: unrecognized symbol!\n");
		}
			int result=getWinWithCount(count_X, count_O, count_T);
		
		//cout<<"X:"<<count_X<<",O:"<<count_O<<",T:"<<count_T<<",.:"<<count_DOT<<endl;
			if(result != -1)
				return result;
			int temp_shortest_X = getShortWithCount('X', count_X, count_O, count_T, count_DOT);
			int temp_shortest_O = getShortWithCount('O', count_X, count_O, count_T, count_DOT);
			if( temp_shortest_X != -1 && (*shortest_X == -1 ||temp_shortest_X < *shortest_X)){
				*shortest_X = temp_shortest_X;
			}
			if( temp_shortest_O != -1 && (*shortest_O == -1 ||temp_shortest_O < *shortest_O)){
				*shortest_O = temp_shortest_O;
			}
		
	}

	return -1;
}

int checkDiagonalWin(char b[4][4],int* shortest_X, int* shortest_O)
{
		int count_X =0;
		int count_O =0;
		int count_T =0;
		int count_DOT=0;
	for(int r=0,col=0;r<4 &&col<4;r++,col++){
		if(b[r][col] == 'X')
			count_X++;
		else if(b[r][col] == 'O')
			count_O++;
		else if(b[r][col] == 'T')
			count_T++;
		else if(b[r][col] == '.')
			count_DOT++;
		else
			printf("Error: unrecognized symbol!\n");
	}
	
		int result=getWinWithCount(count_X, count_O, count_T);
		//cout<<"X:"<<count_X<<",O:"<<count_O<<",T:"<<count_T<<",.:"<<count_DOT<<endl;
		if(result != -1)
			return result;
		int temp_shortest_X = getShortWithCount('X', count_X, count_O, count_T, count_DOT);
		int temp_shortest_O = getShortWithCount('O', count_X, count_O, count_T, count_DOT);
		if( temp_shortest_X != -1 && (*shortest_X == -1 ||temp_shortest_X < *shortest_X)){
				*shortest_X = temp_shortest_X;
		}
		if( temp_shortest_O != -1 && (*shortest_O == -1 ||temp_shortest_O < *shortest_O)){
				*shortest_O = temp_shortest_O;
		}
	

		 count_X =0;
		 count_O =0;
		 count_T =0;
		 count_DOT=0;
	for(int r=0,col=3;r<4 &&col>=0;r++,col--){
		if(b[r][col] == 'X')
			count_X++;
		else if(b[r][col] == 'O')
			count_O++;
		else if(b[r][col] == 'T')
			count_T++;
		else if(b[r][col] == '.')
			count_DOT++;
		else
			printf("Error: unrecognized symbol!\n");
	}
	
		result=getWinWithCount(count_X, count_O, count_T);
		//cout<<"X:"<<count_X<<",O:"<<count_O<<",T:"<<count_T<<",.:"<<count_DOT<<endl;
		if(result != -1)
			return result;
		temp_shortest_X = getShortWithCount('X', count_X, count_O, count_T, count_DOT);
		temp_shortest_O = getShortWithCount('O', count_X, count_O, count_T, count_DOT);
		if( temp_shortest_X != -1 && (*shortest_X == -1 ||temp_shortest_X < *shortest_X)){
			*shortest_X = temp_shortest_X;
		}
		if( temp_shortest_O != -1 && (*shortest_O == -1 ||temp_shortest_O < *shortest_O)){
			*shortest_O = temp_shortest_O;
		}
	

	return -1;
}

int main()
{
	long long T;

	cin>>T;

	char temp[10];
	char board[4][4];
	for(long long i=0;i<T;i++){
		long long result=0 ;
		cin.getline(temp,10);
		for(int l=0;l<4;l++){
			cin.getline(temp,10);
			board[l][0]=temp[0];
			board[l][1]=temp[1];
			board[l][2]=temp[2];
			board[l][3]=temp[3];
			
		}
		
		int sh_X=-1;
		int sh_O=-1;
		result = checkRowWin(board,&sh_X, &sh_O);

		if(result == X_WIN){
			cout<<"Case "<<"#"<<i+1<<": X won";
			cout<<endl;
			continue;
		}else if(result == O_WIN){
			cout<<"Case "<<"#"<<i+1<<": O won";
			cout<<endl;
			continue;
		}

		result = checkColWin(board, &sh_X, &sh_O);
		if(result == X_WIN){
			cout<<"Case "<<"#"<<i+1<<": X won";
			cout<<endl;
			continue;
		}else if(result == O_WIN){
			cout<<"Case "<<"#"<<i+1<<": O won";
			cout<<endl;
			continue;
		}

		result = checkDiagonalWin(board, &sh_X, &sh_O);
		if(result == X_WIN){
			cout<<"Case "<<"#"<<i+1<<": X won";
			cout<<endl;
			continue;
		}else if(result == O_WIN){
			cout<<"Case "<<"#"<<i+1<<": O won";
			cout<<endl;
			continue;
		}

		int numEmpty = countEmptyCell(board);
		//cout << "Empty Cells: "<<numEmpty<<endl;

		int EmptyForX = numEmpty/2;
		int EmptyForO = numEmpty/2 + numEmpty%2;

		if(sh_X != -1 && EmptyForX >= sh_X){
		
			cout<<"Case "<<"#"<<i+1<<": Game has not completed";
			cout<<endl;
		}
		else if(sh_O != -1 && EmptyForO >= sh_O){
		
			cout<<"Case "<<"#"<<i+1<<": Game has not completed";
			cout<<endl;
		} else {
			cout<<"Case "<<"#"<<i+1<<": Draw";
			cout<<endl;
		
		}
//		for(int a=0;a<4;a++){
//			for(int h=0;h<4;h++){
//				cout<<board[a][h];
//			}
//			cout<<endl;
//		}


	}
	return 0;
}


