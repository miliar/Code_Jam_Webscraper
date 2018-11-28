#include <stdio.h> // for cin/cout
#include <iostream> // for printf
#include <fstream> // for ifstream and ofstream
#include <math.h>
#include <ctime>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <stack>
#include <map>
#include <unordered_map>
#include <unordered_set>

using namespace std;

bool TicTacToeTomekJudge(string s, string &result){
	bool noX=false;
	bool noO=false;	
	
	unsigned found=s.find('.');
	if(found!=std::string::npos)
		return false;

	found=s.find('X');
	if(found==std::string::npos)
		noX=true;

	found=s.find('O');
	if(found==std::string::npos)
		noO=true;

	if(noO&&!noX){
		result = "X won";
		return true;
	}

	if(!noO&&noX){
		result = "O won";
		return true;
	}

	return false;
}

void TicTacToeTomek(){
	// https://code.google.com/codejam/contest/2270488/dashboard#s=p0

	ifstream ifs ("..\\data\\TicTacToeTomek\\A-large.in");
	FILE *fout = fopen("..\\data\\TicTacToeTomek\\A-large.out", "w+");

	string line;
	getline(ifs,line);
	int T = atoi(line.c_str());

	char Board[4][4];
	for (int i=0;i<T;i++){	
		bool isGameOver = true;
		for(int j=0;j<4;j++){
			getline(ifs,line);
			while(line.length()<4)
				getline(ifs,line);
			Board[j][0]=line[0];
			Board[j][1]=line[1];
			Board[j][2]=line[2];
			Board[j][3]=line[3];
			
			unsigned found=line.find('.');
			if(found!=std::string::npos)
				isGameOver=false;
		}

		string result = "Game has not completed";
		if(isGameOver)
			result = "Draw";

		string s;
		for(int j=0;j<4;j++){
			s =Board[j][0];
			s+=Board[j][1];
			s+=Board[j][2];
			s+=Board[j][3];
			if(TicTacToeTomekJudge(s, result))
				goto winnerfound;
		}

		for(int j=0;j<4;j++){
			s =Board[0][j];
			s+=Board[1][j];
			s+=Board[2][j];
			s+=Board[3][j];
			if(TicTacToeTomekJudge(s, result))
				goto winnerfound;
		}

		s =Board[0][0];
		s+=Board[1][1];
		s+=Board[2][2];
		s+=Board[3][3];
		if(TicTacToeTomekJudge(s, result))
			goto winnerfound;

		s =Board[3][0];
		s+=Board[2][1];
		s+=Board[1][2];
		s+=Board[0][3];
		TicTacToeTomekJudge(s, result);

winnerfound:		
		fprintf(fout, "Case #%d: %s \n",i+1, result.c_str());
	}

	ifs.close();
	std::fclose(fout);
}

void main() {
	time_t start, end;
	time(&start);

	TicTacToeTomek();

	time(&end);
	double duration = difftime(end, start);
	printf("time spent %.f seconds\n", duration);

	cin.get();
}