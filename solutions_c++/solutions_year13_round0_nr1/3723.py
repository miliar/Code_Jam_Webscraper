
#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <math.h>
#include <set>
#include <sstream>
#include <algorithm>

#include <memory.h>

#ifdef _WIN32
#include <time.h>
#endif

using namespace std;

#ifdef _WIN32
typedef __int64 n64;
typedef unsigned __int64 u64;
#else
typedef long long n64;
typedef unsigned long long u64;
#endif

#if !defined( _WIN32 )
#define _itoa itoa

char * itoa( int _Val, char * _DstBuf, int _Radix)
{
	sprintf( _DstBuf, "%d", _Val );
	return _DstBuf;
}

#endif
string convertInt(int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

#define INF 0x3FFFFFFF

char board[4][4];
bool drawn = false;
bool won =false;





void increase(char d,int *a, int *b,int *c){
	if(d=='X'){
		*a = *a +1;
	}
	else if(d=='O'){
		*b = *b +1;
	}
	else if(d=='T'){
		*c = *c +1;
	}
	else{
		drawn = true;
	}
}


char check(int a, int b, int c){
	if(a==4 || (a==3 & c==1)){
		won = true;
		return 'X';
	}
	else if(b==4 || (b==3 & c==1)){
		won = true;
		return 'O';
	}
	return 'D';
}

int main(){
		
	ifstream fin("a.in");

	int n;

	fin >> n;
	// cout << n << endl;
	for(int i=1;i<=n;i++){
		// cout << "---------------------" << i << "                     " << endl;
		won=false;
		drawn = false;

		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				fin >> board[j][k];
			}
		}

		// check for winner;
		int count_T = 0;
		int count_X=0;
		int count_O =0;
		for(int p=0;(p<4 && !won);p++){

			// rows
			count_T = 0;
			count_X=0;
			count_O =0;
			
			// check rows and check columns

			for(int x = 0;x<4;x++){
				increase(board[p][x],&count_X,&count_O,&count_T);
			}

			if(check(count_X,count_O,count_T) == 'X'){
				cout << "Case #"<<(i)<<": X won" << endl ;
				break;
			}
			else if(check(count_X,count_O,count_T) == 'O'){
				cout << "Case #"<<(i)<<": O won" << endl;
				break;
			}


			// columns
			count_T = 0;
			count_X=0;
			count_O =0;
			
			// check rows and check columns

			for(int x = 0;x<4;x++){
				increase(board[x][p],&count_X,&count_O,&count_T);
			}

			if(check(count_X,count_O,count_T) == 'X'){
				cout << "Case #"<<(i)<<": X won" << endl ;
				break;
			}
			else if(check(count_X,count_O,count_T) == 'O'){
				cout << "Case #"<<(i)<<": O won" << endl;
				break;
			}

		}

		// cout <<" reached here "<< i << endl;

		if(!won){
			count_T = 0;
			count_X=0;
			count_O =0;
			
			// check rows and check columns

			for(int x = 0;x<4;x++){
				increase(board[x][x],&count_X,&count_O,&count_T);
			}

			if(check(count_X,count_O,count_T) == 'X'){
				cout << "Case #"<<(i)<<": X won" << endl ;
				
			}
			else if(check(count_X,count_O,count_T) == 'O'){
				cout << "Case #"<<(i)<<": O won" << endl;
				
			}


			count_T = 0;
			count_X=0;
			count_O =0;
			
			// check rows and check columns

			for(int x = 0;x<4;x++){
				increase(board[x][3-x],&count_X,&count_O,&count_T);
			}

			if(check(count_X,count_O,count_T) == 'X'){
				cout << "Case #"<<(i)<<": X won" << endl ;
				
			}
			else if(check(count_X,count_O,count_T) == 'O'){
				cout << "Case #"<<(i)<<": O won" << endl;
				
			}
		}

		if(!won && !drawn){
			cout << "Case #"<<(i)<<": Draw" << endl;
		}
		else if(!won && drawn){
			cout << "Case #"<<(i)<<": Game has not completed" << endl;

		}





	}
	


}