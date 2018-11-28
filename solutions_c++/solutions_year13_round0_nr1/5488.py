#include <iostream>
#include <fstream>
#include <conio.h>
#include <ios>
#include <string>

using namespace std;

void main()
{
	cout << "Press any key to execute." << endl;
	_getch();

	/*loading file section*/
	ifstream inFile;
	inFile.open("A-Small.in");
	if (!inFile.is_open())
	{
		cout << "Input File dose not exist." << endl;
		return;
	}

	/*reading file section*/
	//pre-reading
	ofstream outFile;
	outFile.open("A-Small.out", ios_base::out|ios_base::trunc);
	if (!inFile.is_open())
	{
		cout << "Output File could not open." << endl;
		return;
	}
	int case_Count;
	//add parameter to be used here

	//reading procedure
	inFile >> case_Count;
	for (int i=0; i<case_Count; i++)
	{
		char Board[4][4]; // Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board
		//输入
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				inFile >> Board[j][k];
			}
		}
		//操作区

		char check_state = 'D';

		// check rows
		for (int j = 0; j < 4; j++)
		{
			char current_state = Board[j][0];
			for (int k = 0; k < 4; k++)
			{
				if (Board[j][k] == '.')
				{
					current_state = '.'; // the row has not complete if has '.'
					break;
				}
				else if (Board[j][k] == current_state)
				{
					current_state = Board[j][k]; // case [X][X] and [O][O]
				}
				else if (Board[j][k] == 'T')
				{
					current_state = current_state; // case [X][T] and [O][T]
				} 
				else if (current_state == 'T')
				{
					current_state = Board[j][k]; // case [T][X] and [T][O]
				}
				else
				{
					current_state = 'D'; // [X][O] and [O][X], draw
					break;
				}
			}
			// row result
			switch (current_state)
			{
			case 'X':
			case 'O':
				check_state = current_state;
				goto print_result;
				break;
			case '.':
				check_state = current_state;
				break;
			}
		}
		// check columns
		for (int k = 0; k < 4; k++)
		{
			char current_state = Board[0][k];
			for (int j = 0; j < 4; j++)
			{
				if (Board[j][k] == '.')
				{
					current_state = '.'; // the column has not complete if has '.'
					break;
				}
				else if (Board[j][k] == current_state)
				{
					current_state = Board[j][k]; // case [X][X] and [O][O]
				}
				else if (Board[j][k] == 'T')
				{
					current_state = current_state; // case [X][T] and [O][T]
				} 
				else if (current_state == 'T')
				{
					current_state = Board[j][k]; // case [T][X] and [T][O]
				}
				else
				{
					current_state = 'D'; // [X][O] and [O][X], draw
					break;
				}
			}
			// column result
			switch (current_state)
			{
			case 'X':
			case 'O':
				check_state = current_state;
				goto print_result;
				break;
			case '.':
				check_state = current_state;
				break;
			}
		}
		// check diagonal 1
		{
			char current_state = Board[0][0];
			for (int j = 0; j < 4; j++)
			{
				if (Board[j][j] == '.')
				{
					current_state = '.'; // the diagonal has not complete if has '.'
					break;
				}
				else if (Board[j][j] == current_state)
				{
					current_state = Board[j][j]; // case [X][X] and [O][O]
				}
				else if (Board[j][j] == 'T')
				{
					current_state = current_state; // case [X][T] and [O][T]
				} 
				else if (current_state == 'T')
				{
					current_state = Board[j][j]; // case [T][X] and [T][O]
				}
				else
				{
					current_state = 'D'; // [X][O] and [O][X], draw
					break;
				}
			}
			// diagonal result
			switch (current_state)
			{
			case 'X':
			case 'O':
				check_state = current_state;
				goto print_result;
				break;
			case '.':
				check_state = current_state;
				break;
			}
		}
		// check diagonal 2
		{
			char current_state = Board[0][3];
			for (int j = 0; j < 4; j++)
			{
				if (Board[j][3-j] == '.')
				{
					current_state = '.'; // the diagonal has not complete if has '.'
					break;
				}
				else if (Board[j][3-j] == current_state)
				{
					current_state = Board[j][3-j]; // case [X][X] and [O][O]
				}
				else if (Board[j][3-j] == 'T')
				{
					current_state = current_state; // case [X][T] and [O][T]
				} 
				else if (current_state == 'T')
				{
					current_state = Board[j][3-j]; // case [T][X] and [T][O]
				}
				else
				{
					current_state = 'D'; // [X][O] and [O][X], draw
					break;
				}
			}
			// diagonal result
			switch (current_state)
			{
			case 'X':
			case 'O':
				check_state = current_state;
				goto print_result;
				break;
			case '.':
				check_state = current_state;
				break;
			}
		}

print_result:
		string result;
		switch (check_state)
		{
		case '.':
			result = "Game has not completed";
			break;
		case 'X':
			result = "X won";
			break;
		case 'O':
			result = "O won";
			break;
		default:
			result = "Draw";
			break;
		}


		
		//输出
		outFile << "Case #" << i+1 << ": " << result << endl;
		outFile.flush();
	}

	/*exit section*/
	cout << "Press any key to exit." << endl;
	_getch();
	inFile.close();
	outFile.close();
	return;
}