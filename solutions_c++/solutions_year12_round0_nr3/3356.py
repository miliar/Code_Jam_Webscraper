#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
using namespace std;

string convertInt(int number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}

string shift(string str,int pos)
{
	int len = str.length();
	return str.substr(pos,len).append(str.substr(0,pos));
}

int check(int i , int A, int B)
{
	int count = 0;
	string str = convertInt(i);

	int len = str.length();
	for ( int j=1;j<len;j++)
	{
		string temp = shift(str,j);
		int num = atoi(temp.c_str());
		if(num <= i)
			continue;
		else if(num >= A && num <= B)
		{
			//cout<<i<<":"<<num<<endl;
			count++;
		}
	}
	return count;
}
void main ()
{
	ifstream input("C-small-attempt0.in",ios::in);
	ofstream output("C-small-attempt0.out",ios::out);
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
		int A;
		int B;
		
		input >>A;
		input >>B;

		if( A > B)
		{
			output << "Case #"<<solvedCases+1 << ": Invalid Input" <<endl; 
			continue;
		}

		int count = 0 ;
		for (int i=A; i <= B;i++)
		{
			count+= check (i,A,B); 
		}
		output << "Case #"<<solvedCases+1<<": "<<count <<endl ;
		solvedCases++;

	}
}