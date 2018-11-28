#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
using namespace std;

bool check(int Num, int score,int &surprise,int remaining)
{
	if(score-Num > 2)
		return false;
	else if(Num <  0)
		return false;
	else if((Num/remaining) >= score )
		return true;
	else if(((score - (Num/remaining)) <= 1) && remaining == 2)
		return true;
	else if(((score - (Num/remaining)) == 2) && remaining == 2 && surprise >0)
	{
		surprise--;
		return true;
	}
	else if(score - Num == 2 && remaining ==1 && surprise >0)
	{
		surprise--;
		return true;
	}
	else
	{
		check(Num-score,score,surprise,remaining-1);
	}
}
void main ()
{
	ifstream input("B-large.in",ios::in);
	ofstream output("B-large.out",ios::out);
	if(!input)
	{
		cout << "Error Opening File";
		exit(1);
	}
	int cases;
	input >> cases;

	int solvedCases =0;

	while(solvedCases < cases)
	{
		int numOfGooglers;
		input >> numOfGooglers;

		int surprise;
		input >> surprise;

		int p;
		input >>p;

		int *list = new int[numOfGooglers];
		
		int count =0;
		for (int i=0;i<numOfGooglers;i++)
		{
			input >>list[i];

			if(check(list[i],p,surprise,3))
				count++;
		}
		
		output << "Case #"<<solvedCases+1<<": "<<count<<endl;
		solvedCases++;
	}
	output.close();
	input.close();
}