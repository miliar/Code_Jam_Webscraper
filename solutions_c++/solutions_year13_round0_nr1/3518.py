
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
using namespace std;

void checkWin(char arr[32][32], bool &xWon, bool &oWon)
{
       int i;
	//check Rows
     xWon = oWon = false;
       for (i = 0; i < 4; i++){
       if (arr[i][0] == arr[i][1] && arr[i][1] == arr[i][2] && arr[i][2] == arr[i][3]){
		if(arr[i][0] == 'X') {xWon =  true; return;}
		if(arr[i][0] == 'O') {oWon =  true; return;}
       }
       }
       for (i = 0; i < 4; i++){
       if (arr[0][i] == arr[1][i] && arr[1][i] == arr[2][i] && arr[2][i] == arr[3][i]){
		if(arr[0][i] == 'X') {xWon =  true; return;}
		if(arr[0][i] == 'O') {oWon =  true; return;}
       }
       }
	if(arr[0][0] == arr[1][1] && arr[1][1] == arr[2][2] && arr[2][2] == arr[3][3]){
		if(arr[0][0] == 'X') {xWon = true; return;}
		if(arr[0][0] == 'O') {oWon = true; return;}
	}
	if(arr[3][0] == arr[2][1] && arr[2][1] == arr[1][2] && arr[1][2] == arr[0][3]){
		if(arr[3][0] == 'X') {xWon = true; return;}
		if(arr[3][0] == 'O') {oWon = true; return;}
       }	       
}


int main()
{
char arr[32][32];
int numOfCases, count = 0, caseCount= 0;
char input[32];
bool dotsFound = false;
char output[512];
std::vector<std::string> finalOutput;
int tposx = -1;
int tposy = -1;
bool xWon, oWon;
scanf("%d", &numOfCases);
//std::cout<< "\nNumber = " << numOfCases;
//cin.getline(input, 32);
//numOfCases = atoi(input);

//while (cin.getline(input, 32) && caseCount <= numOfCases)
while (scanf("%s", input) != EOF && caseCount <= numOfCases)
{ 
	if(input[0] != 'X' && input[0] != 'O' && input[0] != '.' && input[0] != 'T')
		continue;
	//std::cout<< "\nInput " << count << ": " << input; 
	//int j = 0;
	for (int i = 0; i<4; i++){
		arr[count][i] = input[i];
		if(input[i] == 'T'){
			tposx = count;
			tposy = i;
		}
		if(input[i] == '.')
			dotsFound = true;
	}
	count++;
	if (count == 4){
		count = 0;
		caseCount++;
	if(tposy != -1){
		arr[tposx][tposy] = 'X';
	}
	checkWin(arr, xWon, oWon);
	if(!xWon && !oWon && tposy != -1){
		arr[tposx][tposy] = 'O';
		checkWin(arr, xWon, oWon);
	}
	if(xWon)
		sprintf(output, "Case #%d: X won", caseCount);
	else if(oWon)
		sprintf(output, "Case #%d: O won", caseCount);
	else if(dotsFound)
		sprintf(output, "Case #%d: Game has not completed", caseCount);
	else
		sprintf(output, "Case #%d: Draw", caseCount);
	//std::cout << output;
	finalOutput.push_back(output);
	tposy = tposx = -1;
	dotsFound = false;
	}

}
for (size_t i = 0; i< finalOutput.size(); i++){
	std::cout<<finalOutput[i] <<"\n";
}
return 0;
}
