#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>

using namespace std;
//#define SMALL
#define LARGE
#define SIZE 4

int main(){
    FILE *fp, *fpout;
    int T;
    char arr[SIZE][SIZE];
    char empty;
    
    
#ifdef SMALL    
    freopen("A-small-0.in", "rt", stdin);
    freopen("A-small-0.out", "wt", stdout);
#endif    

#ifdef LARGE    
    freopen("A-large-0.in", "rt", stdin);
    freopen("A-large-0.out", "wt", stdout);
#endif    

    cin >> T;

    for(int cur= 0; cur < T; cur ++){
	    for(int i= 0;i< SIZE; i++){
		for(int j=0;j< SIZE; j++){
			cin >> arr[i][j];
		}
	    }
	    int x_won = 0, o_won = 0, dot_found=0;
	    int winner_found = 0;

	    for(int i= 0;i< SIZE && winner_found < 1; i++){
		for(int j=0;j< SIZE; j++){
			if(arr[i][j] == '.')
			{
				dot_found=1;
				continue;
			}
			char player = arr[i][j];
			
			//cout << " Considering " << arr[i][j] << endl;
			// Cheking right hand side 
			//cout << "Right Side Check" << endl;
			int local_count = 0;
			//cout << "player: " << player << endl;
			for(int k = j; k< SIZE; k++)
			{
				if(player == 'T' && k == j)
					player = arr[i][k+1];
				if(player == '.'){
					dot_found = 1;
					break;
				}

				if(arr[i][k] == player || arr[i][k] == 'T')
				{	
					local_count++;
					//cout << "local_count: " << local_count << endl;
				}
				else{
					break;
				}
			}
			if(local_count == SIZE)
			{
	   			if(player == 'X') 
					x_won = 1;
	   			if(player == 'O') 
					o_won = 1;
				winner_found = 1;
				break;
			}

			// Checking down side
			//cout << "Down Side Check" << endl;
			local_count = 0;
			player = arr[i][j];
			//cout << "player: " << player << endl;
			for(int k = i; k< SIZE; k++)
			{
				if(player == 'T' && k==i)
					player = arr[k+1][j];
				if(player == '.'){
					dot_found = 1;
					break;
				}
				if(arr[k][j] == player || arr[k][j] == 'T')
				{	
					local_count++;
					//cout << "local_count: " << local_count << endl;
				}
				else{
					break;
				}
			}
			if(local_count == SIZE)
			{
	   			if(player == 'X') 
					x_won = 1;
	   			if(player == 'O') 
					o_won = 1;
				winner_found = 1;
				break;
			}

			// Checking Diagonal right
			//cout << "Diagonal check right" << endl;
			local_count = 0;
			player = arr[i][j];
			//cout << "player: " << player << endl;
			for(int k = i, l=j; k < SIZE && l < SIZE; k++, l++)
			{
				if(player == 'T' && k==i && l==j)
					player = arr[k+1][l+1];
				if(player == '.'){
					dot_found = 1;
					break;
				}
				if(arr[k][l] == player || arr[k][l] == 'T')
				{	
					local_count++;
					//cout << "local_count: " << local_count << endl;
				}
				else{
					break;
				}
			}
			if(local_count == SIZE)
			{
				//cout << player << " WON" << endl;
	   			if(player == 'X') 
					x_won = 1;
	   			if(player == 'O') 
					o_won = 1;
				winner_found = 1;
				break;
			}

			// Checking Diagonal left 
			//cout << "Diagonal check left" << endl;
			local_count = 0;
			player = arr[i][j];
			//cout << "player: " << player << endl;
			for(int k = i, l=j; k < SIZE && l >= 0; k++, l--)
			{
				if(player == 'T' && k==i && l==j)
					player = arr[k+1][l-1];
				if(player == '.'){
					dot_found = 1;
					break;
				}
				if(arr[k][l] == player || arr[k][l] == 'T')
				{	
					local_count++;
					//cout << "local_count: " << local_count << endl;
				}
				else{
					break;
				}
			}
			if(local_count == SIZE)
			{
				//cout << player << " WON" << endl;
	   			if(player == 'X') 
					x_won = 1;
	   			if(player == 'O') 
					o_won = 1;
				winner_found = 1;
				break;
			}
		}
	    }
	    if(x_won == 1)
		cout << "Case #" << cur+1 << ": X won" << endl;
	    else if(o_won == 1)
		cout << "Case #" << cur+1 << ": O won" << endl;
	    else if(dot_found == 0)
		cout << "Case #" << cur+1 << ": Draw" << endl;
	    else
		cout << "Case #" << cur+1 << ": Game has not completed" << endl;
	    
    }
    
    return 0;
}

