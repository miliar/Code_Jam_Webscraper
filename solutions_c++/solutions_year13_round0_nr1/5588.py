#include <iostream>
#include <fstream>
using namespace std;

/*
All the code below is written by me.
None of the code has been copied from any sources.
*/

/* Globals */
bool quit = false;
char fullpath[301];
char* buf;

/* Variables */
unsigned int size;
char* output;
char** game;

/* Functions */
bool Read(const char* path)
{
	ifstream file(path, ios::binary);
	if (file.is_open()) // Successfully opened
	{
		// Get size of file
		unsigned long beg, end, length;
		beg = file.tellg();
		file.seekg(0, ios::end);
		end = file.tellg();
		length = end - beg;
		file.seekg(0, ios::beg);
		if (length>0)
		{
			// Allocate array
			buf = new char[length+1];
			// Read file
			file.read(buf, length);
			file.close();
			buf[length]='\0';
			if (file)
			{
				cout << "Successfully read file." << endl;
				return true;
			}
			else
			{
				cout << "Failed to extract all data successfully." << endl;
				delete[] buf;
			}
		}
		else
			cout << "Reading an empty file." << endl;
	}
	else
		cout << "Failed to open this file." << endl;
	return false;
}

int ReadToInt(unsigned int* curpos)
{
	unsigned char count = 0;
	char object[11];
	int result;
	// Make sure to skip the whitespaces
	while (isspace(buf[*curpos]) != 0)
	{
		(*curpos)++;
	}
	// Read first number
	while (isspace(buf[*curpos]) == 0 && buf[(*curpos)] != '\0')
	{
		object[count] = buf[(*curpos)];
		(*curpos)++;
		count++;
	}
	object[count] = '\0';
	sscanf(object, "%d", &result);
	return result;
}

void Process()
{
	unsigned int temp = 0, temp2, count = 2, gamecnt;
	bool won;
	size = ReadToInt(&temp);
	// Assign data to game buffer
	output = new char[size+1];
	output[size] = '\0';
	game = new char*[size];
	for (temp = 0; temp < size; temp++)
	{
		game[temp] = new char[17]; // 4x4 game board
		for (temp2 = 0; temp2 < 16; temp2++)
		{
			while (isspace(buf[count]) != 0)
			{
				count++;
			}
			game[temp][temp2] = buf[count];
			count++;
		}
		game[temp][16] = '\0';
	}
	delete[] buf;
	// output: 0=unfinished, 1=draw, 2=X, 3=O
	for (gamecnt = 0; gamecnt < size; gamecnt++)
	{
		// Horizontals
		for (temp = 0; temp < 4; temp++)
		{
			won = true;
			for (temp2 = 0; temp2 < 4; temp2++)
			{
				count = temp * 4 + temp2;
				if (game[gamecnt][count] != 'X' && game[gamecnt][count] != 'T')
				{
					won = false;
					break;
				}
			}
			if (won)
			{
				output[gamecnt] = 'X';
				break;
			}
		}
		if (!won)
		{
			for (temp = 0; temp < 4; temp++)
			{
				won = true;
				for (temp2 = 0; temp2 < 4; temp2++)
				{
					count = temp * 4 + temp2;
					if (game[gamecnt][count] != 'O' && game[gamecnt][count] != 'T')
					{
						won = false;
						break;
					}
				}
				if (won)
				{
					output[gamecnt] = 'O';
					break;
				}
			}
		}
		// Verticals
		if (!won)
		{
			for (temp = 0; temp < 4; temp++)
			{
				won = true;
				for (temp2 = 0; temp2 < 4; temp2++)
				{	
					count = temp + temp2 * 4;
					if (game[gamecnt][count] != 'X' && game[gamecnt][count] != 'T')
					{
						won = false;
						break;
					}
				}
				if (won)
				{
					output[gamecnt] = 'X';
					break;
				}
			}
		}
		if (!won)
		{
			for (temp = 0; temp < 4; temp++)
			{
				won = true;
				for (temp2 = 0; temp2 < 4; temp2++)
				{	
					count = temp + temp2 * 4;
					if (game[gamecnt][count] != 'O' && game[gamecnt][count] != 'T')
					{
						won = false;
						break;
					}
				}
				if (won)
				{
					output[gamecnt] = 'O';
					break;
				}
			}
		}
		// Diagonal
		if (!won)
		{
			won = true;
			for (temp = 0; temp < 16; temp+=5)
			{
				if (game[gamecnt][temp] != 'X' && game[gamecnt][temp] != 'T')
				{
					won = false;
					break;
				}
			}
			if (won)
				output[gamecnt] = 'X';
		}
		if (!won)
		{
			won = true;
			for (temp = 0; temp < 16; temp+=5)
			{
				if (game[gamecnt][temp] != 'O' && game[gamecnt][temp] != 'T')
				{
					won = false;
					break;
				}
			}
			if (won)
			{
				output[gamecnt] = 'O';
				break;
			}
		}
		// Diagonal
		if (!won)
		{
			won = true;
			for (temp = 3; temp < 13; temp+=3)
			{
				if (game[gamecnt][temp] != 'X' && game[gamecnt][temp] != 'T')
				{
					won = false;
					break;
				}
			}
			if (won)
				output[gamecnt] = 'X';
		}
		if (!won)
		{
			won = true;
			for (temp = 3; temp < 13; temp+=3)
			{
				if (game[gamecnt][temp] != 'O' && game[gamecnt][temp] != 'T')
				{
					won = false;
					break;
				}
			}
			if (won)
				output[gamecnt] = 'O';
		}
		// No one won
		if (!won)
		{
			output[gamecnt] = 'D';
			// Check if there're empty spaces
			for (temp = 0; temp < 16; temp++)
			{
				if (game[gamecnt][temp] == '.')
				{
					output[gamecnt] = '.';
					break;
				}
			}
		}
	}
}

void Output(char*path)
{
	unsigned int temp = 0;
	char msg[23];
	strcat(path,".out");
	ofstream file(path);
	if (file.is_open())
	{
		while (file.good() && temp < size)
		{
			if (output[temp] == 'X')
				strcpy(msg, "X won");
			else if (output[temp] == 'O')
				strcpy(msg, "O won");
			else if (output[temp] == 'D')
				strcpy(msg, "Draw");
			else if (output[temp] == '.')
				strcpy(msg, "Game has not completed");
			file << "Case #" << (temp+1) << ": " << msg << endl;
			temp++;
		}
		file.close();
		cout << "Successfully exported output file." << endl;
	}
	else
		cout << "Failed to create output file." << endl;
	// Clear memory
	for (temp = 0; temp < size; temp++)
	{
		delete[] game[temp];
	}
	delete[] game;
	delete[] output;
}

/* Main */
int main()
{
	while (!quit)
	{
		cout << "Enter full path of file:" << endl;
		cin >> fullpath;
		if (Read(fullpath))
		{
			Process();
			Output(fullpath);
		}
		cout << "Process another file? (Y/N)" << endl;
		cin >> fullpath;
		if (fullpath[0] == 'N')
			quit = true;
	}
	return 0;
}