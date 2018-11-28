#include <string>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;


char combineWord(char a, char b,string[],int);
bool clearWord(string word, char let,string[],int);

int main()
{
	ifstream input;
	input.open("input.txt");
	ofstream out;
	out.open("a.txt");

	int numCases;

	input >> numCases;

	
	for (int i=0; i<numCases;i++)
	{
		int numCom=1;
		input >> numCom;
		

		string* comArr = new string[numCom];
		for(int j=0;j<numCom;j++)
		{
			input >> comArr[j];
		}

		int numRe;
		input >> numRe;

		string* reArr = new string[numRe];
		
		for (int k=0;k<numRe;k++)
		{
			input >> reArr[k];
		}

		int lengthWord;
		input >>lengthWord;

		string word;
		input >> word;
		
		string output;
		output = word[0];
		for(int l=1;l<lengthWord;l++)
		{

			//combine word
			//cout << combineWord(word[l],output[output.length()-1],comArr,numCom) << endl;
			if (output.length() >0 && combineWord(word[l],output[output.length()-1],comArr,numCom) != '0')
			{
				int z = output.length();
				output = output.substr(0,z-1) + combineWord(word[l],word[l-1],comArr,numCom);
			}
			//clear
			else if (clearWord(output,word[l],reArr,numRe) == true)
			{
				output = "";
			}
			//add letter
			else
				output += word[l] ;
		}

		out << "Case #" << i+1 << ": " << "[";
		for (int y=0;y<output.length();y++)
		{
			if (y==0)
				out << output[y];
			else
				out << ", " << output[y];
		}
		out << "]" << endl;
	}

	return 0;
}

char combineWord(char a, char b,string arr[],int length)
{
	
	for(int i=0;i<length;i++)
	{
		if (a==arr[i][0] && b == arr[i][1])
			return arr[i][2];
		else if (a==arr[i][1] && b == arr[i][0])
			return arr[i][2];
	}
	return '0';
}

bool clearWord(string word, char let, string arr[],int length)
{
	for (int i=0;i<length;i++)
	{
		if ( arr[i][0] == let && word.find(arr[i][1]) != -1)
			return true;
		else if (arr[i][1] == let && word.find(arr[i][0]) != -1)
			return true;
	}
	return false;
}