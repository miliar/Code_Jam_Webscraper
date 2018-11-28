// CodeJam 2011 - Qualification Round - Bot trust
#include <fstream>
#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main()
{
   int T, N;
   queue<int> Red, Blue;
   queue<char> seq;
   char turn;
   ifstream infile("A-small-attempt0.in");
   ofstream outfile("A-small.out");
   char ch; int non;
   
   infile >> T;
   for(int i=1; i<=T; i++)
   {
	infile >> N;
	for(int j=1; j<=N; j++)
	{
		infile >> ch; infile >> non;
		//cout << "ch=" << ch <<"   non="<<non<<endl;
		seq.push(ch);
		if(ch == 'O') Red.push(non);
		else Blue.push(non);
	}
	ch = seq.front();
	if(ch == 'O') turn = 'O';
	else turn = 'B';
	int cur_red = 1, cur_blue = 1;
	int no_of_seconds = 0;
	while(!Red.empty() || !Blue.empty())
	{
		no_of_seconds++;
		if(!Red.empty() && cur_red == Red.front() && turn == 'O')
		{
			Red.pop(); seq.pop();
			if(seq.empty()) continue;
			if(seq.front() == 'B') turn = 'B';
			if(!Blue.empty() && cur_blue < Blue.front()) cur_blue++;
			if(!Blue.empty() && cur_blue > Blue.front()) cur_blue--;
			continue;
		}
		if(!Blue.empty() && cur_blue == Blue.front() && turn == 'B')
		{
			Blue.pop(); seq.pop();
			if(seq.empty()) continue;
			if(seq.front() == 'O') turn = 'O';
			if(!Red.empty() && cur_red < Red.front()) cur_red++;
			if(!Red.empty() && cur_red > Red.front()) cur_red--;
			continue;
		}

		if(!Red.empty() && cur_red < Red.front()) cur_red++;
		if(!Red.empty() && cur_red > Red.front()) cur_red--;
		if(!Blue.empty() && cur_blue < Blue.front()) cur_blue++;
		if(!Blue.empty() && cur_blue > Blue.front()) cur_blue--;
	}

	outfile << "Case #" << i << ": " << no_of_seconds << endl;
   }
   infile.close();
   outfile.close();
   return 0;
}

