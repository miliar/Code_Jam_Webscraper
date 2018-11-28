#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <ctime>
#include <map>
#include <cmath>
#include <fstream>
#include <iterator>
#include <cstring>
#include <algorithm>
#include <set>
#include <cassert>
#include <list>
#define LL long long
#define ULL unsigned long long
#define UI unsigned int
#define MOD 1000000007
using namespace std;

char board[4][4];
int testCases;
int scoreX,scoreO,scoreT,scoreP;
vector<string> combinations;
char str[4];
bool foundEmpty;

void printBoard()
{
	for(int k=0;k<4;k++){
		for(int l=0;l<4;l++)
			cout << board[k][l];
		cout << endl;
	}
	cout << endl;
}

void printCombinations()
{
	cout << "Printing combinations" << endl;
	for(size_t k=0;k<combinations.size();k++)
		cout << combinations[k] << endl;
		
	cout << endl;
}

string solve()
{
	foundEmpty = false;
	
	for(size_t i=0;i<combinations.size();i++){
		
		scoreO = count(combinations[i].begin(),combinations[i].end(),'O');
		scoreX = count(combinations[i].begin(),combinations[i].end(),'X');
		
		if(scoreO >= 3){
			if(scoreO == 4)
				return "O won";
			scoreT = count(combinations[i].begin(),combinations[i].end(),'T');
			if(scoreT == 1)
				return "O won";
		}
		else if(scoreX >= 3){
			if(scoreX == 4)
				return "X won";
			scoreT = count(combinations[i].begin(),combinations[i].end(),'T');
			if(scoreT == 1)
				return "X won";
		}
		
		scoreP = count(combinations[i].begin(),combinations[i].end(),'.');
		if(scoreP > 0)
			foundEmpty = true;
	
	}
	if(foundEmpty)
		return "Game has not completed";
	else
		return "Draw";
}

int main ()
{

    ofstream fout;
    ifstream fin;
    fin.open("testFile.txt");
    fout.open("output.txt");
    
    fin >> testCases;
    
    for(int i=0;i<testCases;i++){
		
		for(int k=0;k<4;k++)
			for(int l=0;l<4;l++)
				fin >> board[k][l];
		
		for(int k=0;k<4;k++){
			for(int l=0;l<4;l++){
				str[l] = board[k][l];
			}
			string tmp(str);
			combinations.push_back(tmp);
		}
		
		for(int k=0;k<4;k++){
			for(int l=0;l<4;l++){
				str[l] = board[l][k];
			}
			string tmp(str);
			combinations.push_back(tmp);
		}
		

		for(int k=0;k<4;k++)
			str[k] = board[k][k];
		string tmp1(str);
		combinations.push_back(tmp1);
		
		for(int k=3;k>=0;k--)
			str[k] = board[3-k][k];
		string tmp2(str);
		combinations.push_back(tmp2);
		
		fout << "Case #" << i+1 << ": " << solve() << endl;
		
		
		
		//printCombinations();
		combinations.clear();
	}
    
    
    fin.close(); 
    fout.close(); 
}
