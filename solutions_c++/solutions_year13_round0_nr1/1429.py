#include <iostream>
#include <cstdio>
#include <string>
#include <map>
using namespace std;

const int BOARD_SIZE = 4;
const string STATUS_X_WON = "X won";
const string STATUS_O_WON = "O won";
const string STATUS_DRAW = "Draw";
const string STATUS_NOT_COMPLETED = "Game has not completed";

string board[BOARD_SIZE];

void readInput()
{
    for (int r = 0; r < BOARD_SIZE; r++) 
        cin >> board[r];
}

map<char, int> getSymbolsCount(string str)
{
    map<char, int> symbolsCount;
    for (int i = 0; i < str.size(); i++)
        symbolsCount[str[i]]++;
        
    return symbolsCount;
}

string evaluateSymbols(string str)
{
    map<char, int> symbolsCount = getSymbolsCount(str);   
       
    if (symbolsCount['X'] == 4) return STATUS_X_WON;
    if (symbolsCount['X'] == 3 && symbolsCount['T'] == 1) return STATUS_X_WON;
        
    if (symbolsCount['O'] == 4) return STATUS_O_WON;
    if (symbolsCount['O'] == 3 && symbolsCount['T'] == 1) return STATUS_O_WON;   
    
    return "";
}

string solve()
{
    for (int r = 0; r < BOARD_SIZE; r++)
    {
        string row = board[r];
        string result = evaluateSymbols(row);
        if (result != "") return result;
    }
    
    for (int c = 0; c < BOARD_SIZE; c++)
    {
        string col = "";
        for (int r = 0; r < BOARD_SIZE; r++)
            col += board[r][c];
        
        string result = evaluateSymbols(col);
        if (result != "") return result;
    }
    
    string mainDiag = "";
    for (int r = 0; r < BOARD_SIZE; r++)
        mainDiag += board[r][r];
       
    string resultMainDiag = evaluateSymbols(mainDiag);
    if (resultMainDiag != "") return resultMainDiag;   
    
        
    string secondDiag = "";
    for (int r = 0; r < BOARD_SIZE; r++)
        secondDiag += board[r][BOARD_SIZE - r - 1];
    
    string resultSecondDiag = evaluateSymbols(secondDiag);
    if (resultSecondDiag != "") return resultSecondDiag;
       
    for (int r = 0; r < BOARD_SIZE; r++)
        for (int c = 0; c < BOARD_SIZE; c++)
            if (board[r][c] == '.')
               return STATUS_NOT_COMPLETED;
       
    return STATUS_DRAW;   
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        readInput();
        
        string result = solve();
        printf("Case #%d: %s\n", t, result.c_str());        
    }
    
    return 0;
}
